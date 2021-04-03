'''
一、物体检测: 100khz起步，步进300次，每次5khz
1: 水果类：苹果、香蕉、橘子、梨
2: 植物：多肉、绿箩
3: 食物类：
4: 日常生活办公物品：易拉罐、水杯、手机、钥匙、AirPods
'''

'''
二、身体部位识别
额头、下巴、耳朵、手、胳膊肘、胸口、叉腰、膝盖
'''

import numpy as np
import serial
import serial.tools.list_ports
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import struct   # converting data type from bytes to double or integer in python is really simple using the struct library
import pandas as pd   # Python数据分析库，这里用来将数据存储为csv文件
import sklearn
from sklearn import svm

# 实时训练模型并导入
import sys
sys.path.append('trainingModel/')   # 调整文件路径
# import trainModel_OR_Fruits_Group1    # 分类第一组水果
# import trainModel_OR_Fruits_Group2    # 分类第二组水果
import trainModel_OR_Fruits_Group3    # 分类猫
# import trainModel_OR_Fruits_Group4      # 分类不同的日常物体
# import trainModel_OR_Fruits_Group5      # 分类不同的身体部位

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
        # 按照字典的格式存储到文件中
        self.topCsvData = []
        self.clfDataFrame = pd.DataFrame(np.arange(18000).reshape(60, 300))

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

    def readSerialPlot(self, lines, clf_text, clf):
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
                    self.data.append(value)
                self.isReceiving = True
                # self.csvData.append(self.data[-1])

                # 成功采集到所需的数据点，存储连续50组的数据点到dataframe中
                plotInteval += 1
                oneSideData_av = self.movingAverage(self.data, 20)  # 平滑
                self.clfDataFrame.loc[plotInteval-1] = oneSideData_av.values
                # print(self.clfDataFrame)

                if (plotInteval % 60 == 0):  # 每获得n次画个图，显示分类结果
                    plotInteval = 0
                    clfdata = self.clfDataFrame.mean(axis=0)    # 取平均值
                    # print(clfdata.values)
                    # 使用SVM对实时数据分类
                    clf_result = trainModel_OR_Fruits_Group3.objectConverter(clf.predict([clfdata])[0])
                    lines.set_data(range(self.plotMaxLength), clfdata)
                    clf_text.set_text(clf_result)   # 在图中显示文字
                    plt.draw()
                    plt.pause(0.01)

    def movingAverage(self, interval, windowsize):  # 滑动平均滤波法
        window = np.ones(int(windowsize)) / float(windowsize)
        returnData = np.convolve(interval, window, 'same')
        returnData = pd.Series(returnData)
        return returnData   # 返回的数据类型为 ndarray

    def serialConnectionClose(self):
        self.isRun = False
        self.serialConnection.close()
        print('串口已断开连接...')
        dfTop = pd.DataFrame(self.topCsvData)
        dfTop['Fruits'] = 'Nothing'
        print(dfTop)
        # dfTop.to_csv('/Users/cuizhitong/Desktop/Fruits_Nothing.csv')
        # dfBottom = pd.DataFrame(self.bottomCsvData)
        # dfBottom['Gesture'] = 'one_finger_bot'
        # print(dfBottom)
        # dfBottom.to_csv('/Users/cuizhitong/Desktop/one_finger_bot.csv')
        print('Real-time classification has been stopped!')


def main():
    # 设置类初始化所需的变量
    portName = '/dev/cu.usbmodem42949672951'  # teensy port name
    baudRate = 9600
    maxPlotLength = 300
    dataNumBytes = 2      # number of bytes of 1 data point, 1byte = 8bit, 0 ~ 255
    s = serialPlot(portName, baudRate, maxPlotLength, dataNumBytes)

    fig = plt.figure(figsize=(16,8))
    xmin = 1
    xmax = maxPlotLength
    ymin = 1
    ymax = 1024
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))    # Add an axes to the current figure and make it the current axes.
    ax.set_title('Amplitude Of Sweep Frequencies', fontsize=18)
    ax.set_xlabel('Frequency Steps')
    ax.set_ylabel('Amplitude Anolog Value')
    text = ax.text(140, 820, '', fontsize=108)
    # ax.legend(loc="upper left")
    lineLabel = '200 frequencies'
    lines = ax.plot([], [], label=lineLabel)[0]    # 返回一个Line2D对象

    # 读取串口数据的同时画图，键盘输入[Control+C]后，暂停接收串口数据，并保存文件
    try:
        clf = trainModel_OR_Fruits_Group3.trainSVM()
        s.readSerialPlot(lines, text, clf)
    except KeyboardInterrupt:   # 输入 [Control+C]
        s.serialConnectionClose()   # 关闭串口，保存文件

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == '__main__':
    main()
