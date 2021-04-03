import numpy as np
import serial
import serial.tools.list_ports
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import struct   # converting data type from bytes to double or integer in python is really simple using the struct library
import pandas as pd   # Python数据分析库，这里用来将数据存储为csv文件

class serialPlot:
    def __init__(self, serialPort = '/dev/ttyUSB0', serialBaud = 115200, plotLength = 200, dataNumBytes = 2):
        self.port = serialPort
        self.baud = serialBaud
        self.plotMaxLength = plotLength
        self.dataNumBytes = dataNumBytes
        self.rawData = bytearray(dataNumBytes)  # 如果初始值为整数，则返回长度为source的初始化数组
        self.data = collections.deque([0] * plotLength, maxlen=plotLength)  # 返回一个新的双向队列对象，从左到右初始化(用方法 append()) ，从 iterable 迭代对象创建, [0]*plotLength 表示将队列全部初始化为 0
        self.plotDataPoints = collections.deque([0] * plotLength, maxlen=plotLength)
        self.isRun = True   # default to true, if serialClose(), change to false
        self.isReceiving = False
        # self.csvData = []
        self.results = [0]*self.plotMaxLength

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

    def readSerialPlot(self, lines):
        time.sleep(1.0)  # give some buffer time for retrieving data
        self.serialConnection.reset_input_buffer()
        plotInteval = 0
        while (self.isRun):
            self.serialConnection.readinto(self.rawData)
            value, = struct.unpack('h', self.rawData)  # 如果加逗号，则返回一个具体数值，如果不加逗号，则返回一个元组。use 'h' for a 2 byte integer, 'f' for a 4 byte integer, 根据格式fmt从缓冲区解压出数据，以tuple形式返回
            # 判断是否从Arduino获得标示值
            if (value == 1024):
                for i in range(self.plotMaxLength):
                    self.serialConnection.readinto(self.rawData)
                    value, = struct.unpack('h', self.rawData)
                    value = self.smoothingData(i, value)   # 平滑数据
                    self.data.append(value)
                self.isReceiving = True
                print(self.data)
                data_av = self.movingAverage(self.data, 3)
                lines.set_data(range(self.plotMaxLength), data_av)
                plt.draw()
                plt.pause(0.01)
                # self.csvData.append(self.data[-1])

                # 成功采集到所需的200个数据点
                plotInteval += 1
                if (plotInteval % 200 == 0):  # 每获得100次画个图
                    plotInteval = 0
                    print(self.data)
                    lines.set_data(range(self.plotMaxLength), self.data)
                    plt.draw()
                    plt.pause(0.01)

    def smoothingData(self, i, value):
        self.results[i] = self.results[i]*0.5 + value*0.5
        return self.results[i]

    def movingAverage(self, interval, windowsize):  # 滑动平均滤波法
        window = np.ones(int(windowsize)) / float(windowsize)
        returnData = np.convolve(interval, window, 'same')
        return returnData   # 返回的数据类型为 ndarray

    def serialConnectionClose(self):
        self.isRun = False
        self.serialConnection.close()
        print('Disconnected...')
        # df = pd.DataFrame(self.csvData)
        # df.to_csv('/user/cuizhitong/Desktop/frequencyData.csv')

def main():
    # 设置类初始化所需的变量
    portName = '/dev/cu.usbmodem14101'  # teensy port name
    baudRate = 38400
    maxPlotLength = 150
    dataNumBytes = 2      # number of bytes of 1 data point, 1byte = 8bit, 0 ~ 255
    s = serialPlot(portName, baudRate, maxPlotLength, dataNumBytes)

    fig = plt.figure(figsize=(15,10))
    xmin = 1
    xmax = maxPlotLength
    ymin = 1
    ymax = 600
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))    # Add an axes to the current figure and make it the current axes.
    ax.set_title('Amplitude Of All Frequencies', fontsize=18)
    ax.set_xlabel('Frequency Steps')
    ax.set_ylabel('Amplitude Anolog Value')
    # ax.legend(loc="upper left")
    lineLabel = '200 frequencies'
    lines = ax.plot([], [], label=lineLabel)[0]    # 返回一个Line2D对象

    # 读取串口数据的同时画图
    s.readSerialPlot(lines)

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == '__main__':
    main()
