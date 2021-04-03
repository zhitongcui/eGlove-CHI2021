import numpy as np
import serial
import serial.tools.list_ports
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import struct   # converting data type from bytes to double or integer in python is really simple using the struct library
import pandas as pd   # Python数据分析库，这里用来将数据存储为csv文件
from pandas import Series, DataFrame
import sklearn
from sklearn import svm

import model_OR_sevenfruits

class serialPlot:
    def __init__(self, serialPort = '/dev/ttyUSB0', serialBaud = 115200, plotLength = 200, dataNumBytes = 2):
        self.port = serialPort
        self.baud = serialBaud
        self.plotMaxLength = plotLength
        self.dataNumBytes = dataNumBytes
        self.rawData = bytearray(dataNumBytes)  # 如果初始值为整数，则返回长度为source的初始化数组
        # 返回一个新的双向队列对象，从左到右初始化(用方法 append()) ，从 iterable 迭代对象创建, [0]*plotLength 表示将队列全部初始化为 0
        self.oneSideData = collections.deque([0] * plotLength, maxlen=plotLength)
        self.dualSideData = collections.deque([0] * plotLength, maxlen=plotLength)
        self.isRun = True   # default to true, if serialClose(), change to false
        self.isReceiving = False
        # 按照字典的格式存储到文件中
        self.topCsvData = []
        self.bottomCsvData = []

        print('Trying to connect to: ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
        try:
            ports_list = list(serial.tools.list_ports.comports())    # 获取当前可用串口
            for p in ports_list:
                print(p.device)     # /dev/cu.usbmodem42949672951
            print(len(ports_list), 'ports found')   # 2 ports found
            self.serialConnection = serial.Serial(serialPort, serialBaud, timeout=5)    # get a reference to the serial connection in self.serialConnection
            print('Connected to ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
        except:
            print("Failed to connect with " + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')

    def readSerialPlot(self, linesOneSide, linesDualSide):
        time.sleep(1.0)  # give some buffer time for retrieving data
        self.serialConnection.reset_input_buffer()
        plotInteval = 0  # 由于串口数据传输太快，这里设置画图的间隔
        while (self.isRun):
            self.serialConnection.readinto(self.rawData)
            value, = struct.unpack('h', self.rawData)  # 如果加逗号，则返回一个具体数值，如果不加逗号，则返回一个元组。use 'h' for a 2 byte integer, 'f' for a 4 byte integer, 根据格式fmt从缓冲区解压出数据，以tuple形式返回
            # 判断是否从Arduino获得标示值
            if (value == 1024):
                self.isReceiving = True
                for i in range(self.plotMaxLength):
                    self.serialConnection.readinto(self.rawData)
                    value, = struct.unpack('h', self.rawData)
                    self.oneSideData.append(value)
                for i in range(self.plotMaxLength):
                    self.serialConnection.readinto(self.rawData)
                    value, = struct.unpack('h', self.rawData)
                    self.dualSideData.append(value)

                # 成功采集到两部分分别 200 个 data points
                plotInteval += 1
                if (plotInteval % 20 == 0):  # 每获得多少帧画个图
                    plotInteval = 0
                    # 滑动平均滤波降噪
                    oneSideData_av = self.movingAverage(self.oneSideData, 50)
                    dualSideData_av = self.movingAverage(self.dualSideData, 40)
                    # 将平滑后的信号数据存入文件，Ctrl+C则关闭串口存取文件，Ctrl+Z关闭串口不存文件
                    self.topCsvData.append(oneSideData_av)
                    self.bottomCsvData.append(dualSideData_av)
                    # 画图
                    linesOneSide.set_data(range(self.plotMaxLength), oneSideData_av)
                    linesDualSide.set_data(range(self.plotMaxLength), dualSideData_av)
                    plt.draw()
                    plt.pause(0.01)

    def movingAverage(self, interval, windowsize):  # 滑动平均滤波法
        window = np.ones(int(windowsize)) / float(windowsize)
        returnData = np.convolve(interval, window, 'same')
        return returnData   # 返回的数据类型为 ndarray

    def serialConnectionClose(self):
        self.isRun = False
        self.serialConnection.close()
        print('串口已断开连接...')
        dfTop = pd.DataFrame(self.topCsvData)
        dfTop['Gesture'] = 'one_finger_top'
        print(dfTop)
        dfTop.to_csv('/Users/cuizhitong/Desktop/one_finger_top.csv')
        dfBottom = pd.DataFrame(self.bottomCsvData)
        dfBottom['Gesture'] = 'one_finger_bot'
        print(dfBottom)
        dfBottom.to_csv('/Users/cuizhitong/Desktop/one_finger_bot.csv')
        print('数据点保存成功')

def main():
    # 设置类初始化所需变量
    portName = '/dev/cu.usbmodem42949672951'  # teensy port name
    baudRate = 38400
    maxPlotLength = 225
    dataNumBytes = 2   # number of bytes of 1 data point, 1byte = 8bit, 0 ~ 255
    s = serialPlot(portName, baudRate, maxPlotLength, dataNumBytes)

    fig = plt.figure(figsize=(20,10))
    xmin = 1
    xmax = maxPlotLength
    ymin = 1
    ymax = 400
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))    # Add an axes to the current figure and make it the current axes.
    ax.set_title('Amplitude Of All Frequencies', fontsize=18)
    ax.set_xlabel('Frequency Steps')
    ax.set_ylabel('Amplitude Anolog Value')
    # ax.legend(loc="upper left")
    linesOneSide = ax.plot([], [], label='FrontSide', color='tab:blue')[0]
    linesDualSide = ax.plot([], [], label='BackSide', color='tab:orange')[0]

    # 读取串口数据的同时画图，键盘输入[Control+C]后，暂停接收串口数据，并保存文件
    try:
        s.readSerialPlot(linesOneSide, linesDualSide)
    except KeyboardInterrupt:   # 输入 [Control+C]
        s.serialConnectionClose()   # 关闭串口，保存文件

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == '__main__':
    main()
