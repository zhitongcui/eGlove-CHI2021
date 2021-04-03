import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
from pandas import Series, DataFrame

def loadFile(path):
    # pandas默认把第一行作为列属性，第一行不能用
    # index_col=0将第一列作为索引
    df = pd.read_csv(path, index_col=0, converters={'Object': typeConverter})
    # print(df.iloc[0]   # iloc通过行号索引来确定行
    # print(df.shape)
    return df

def typeConverter(type):
    # 字符串前面加 'r'，表示这是个普通字符串
    fruits_type = {r'NoObject_Top': 0,
                   r'NoObject_Bottom': 0,
                   r'Apple_Top': 1,
                   r'Apple_Bottom': 1,
                   r'Banana_Top': 2,
                   r'Banana_Bottom': 2,
                   r'Cucumber_Top': 3,
                   r'Cucumber_Bottom': 3}
    # 这个函数返回数组，数组包含水果的7种类型
    return fruits_type[type]

def draw(plotMaxLength, df0, df1, df2, df3, df4, df5, df6, df7, df8, df9):
    fig = plt.figure(figsize=(12,8))
    xmin = 1
    xmax = plotMaxLength
    ymin = 1
    ymax = 900
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax.set_title('Fruits and Plants', fontsize=28)
    ax.set_xlabel('Frequency (KHz)', fontsize=24)
    ax.set_ylabel('Amplitude Raw Reading (V)', fontsize=24)
    ax.xaxis.set_major_formatter(FuncFormatter(xaxis_update_scale_value))
    ax.yaxis.set_major_formatter(FuncFormatter(yaxis_update_scale_value))
    ax.tick_params(axis='both', labelsize=14)

    lineLabel0 = 'No objects'
    lineLabel1 = 'Apple'
    lineLabel2 = 'Banana'
    lineLabel3 = 'Corn'
    lineLabel4 = 'Tomata'
    lineLabel5 = 'Orange'
    lineLabel6 = 'Pear'
    lineLabel7 = 'Green Date'
    lineLabel8 = 'Succulent'
    lineLabel9 = 'Greenbasket'

    # one of the Tableau Colors from the 'T10' categorical palette (the default color cycle): {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}
    lines0 = ax.plot([], [], label=lineLabel0, color='tab:purple')[0]
    lines0.set_data(range(plotMaxLength), df0)
    lines1 = ax.plot([], [], label=lineLabel1, color='tab:red')[0]
    lines1.set_data(range(plotMaxLength), df1)
    lines2 = ax.plot([], [], label=lineLabel2, color='tab:blue')[0]
    lines2.set_data(range(plotMaxLength), df2)
    lines3 = ax.plot([], [], label=lineLabel3, color='tab:green')[0]
    lines3.set_data(range(plotMaxLength), df3)
    lines4 = ax.plot([], [], label=lineLabel4, color='tab:orange')[0]
    lines4.set_data(range(plotMaxLength), df4)
    lines5 = ax.plot([], [], label=lineLabel5, color='tab:brown')[0]
    lines5.set_data(range(plotMaxLength), df5)
    lines6 = ax.plot([], [], label=lineLabel6, color='tab:gray')[0]
    lines6.set_data(range(plotMaxLength), df6)
    lines7 = ax.plot([], [], label=lineLabel7, color='tab:cyan')[0]
    lines7.set_data(range(plotMaxLength), df7)
    lines8 = ax.plot([], [], label=lineLabel8, color='tab:olive')[0]
    lines8.set_data(range(plotMaxLength), df8)
    lines9 = ax.plot([], [], label=lineLabel9, color='tab:pink')[0]
    lines9.set_data(range(plotMaxLength), df9)

    ax.legend(loc="upper right", fontsize='16')
    plt.show()

def yaxis_update_scale_value(temp, position):
    result = temp/1024*5
    return "{}".format(round(result))

def xaxis_update_scale_value(temp, position):
    result = temp*5
    return "{}".format(round(result))

def plotDataPoints():

    df_Fruits_Nothing = loadFile('../data/OR_Daily/Objects_Nothing.csv')
    df_Fruits_Apple = loadFile('../data/OR_Fruits/Fruits_Apple.csv')
    df_Fruits_Banana = loadFile('../data/OR_Fruits/Fruits_Banana.csv')
    df_Fruits_Corn = loadFile('../data/OR_Fruits/Fruits_Corn.csv')
    df_Fruits_Tomata = loadFile('../data/OR_Fruits/Fruits_Tomata.csv')
    df_Fruits_Orange = loadFile('../data/OR_Fruits/Fruits_Orange.csv')
    df_Fruits_Pear = loadFile('../data/OR_Fruits/Fruits_Pear.csv')
    df_Fruits_Date = loadFile('../data/OR_Fruits/Fruits_Date.csv')
    df_Plants_Succulent = loadFile('../data/OR_Plants/Fruits_Succulent.csv')
    df_Plants_Greenbasket = loadFile('../data/OR_Plants/Fruits_Greenbasket.csv')

    df_Fruits_Nothing.drop(axis=1, columns='Objects', inplace=True)
    df_Fruits_Apple.drop(axis=1, columns='Fruits', inplace=True)
    df_Fruits_Banana.drop(axis=1, columns='Fruits', inplace=True)
    df_Fruits_Corn.drop(axis=1, columns='Fruits', inplace=True)
    df_Fruits_Tomata.drop(axis=1, columns='Fruits', inplace=True)
    df_Fruits_Orange.drop(axis=1, columns='Fruits', inplace=True)
    df_Fruits_Pear.drop(axis=1, columns='Fruits', inplace=True)
    df_Fruits_Date.drop(axis=1, columns='Fruits', inplace=True)
    df_Plants_Succulent.drop(axis=1, columns='Fruits', inplace=True)
    df_Plants_Greenbasket.drop(axis=1, columns='Fruits', inplace=True)

    # print(df_Fruits_Date.shape)
    # print(df_Plants_Greenbasket.shape)

    df_Fruits_Nothing = df_Fruits_Nothing.mean(axis=0)
    df_Fruits_Apple = df_Fruits_Apple.mean(axis=0)
    df_Fruits_Banana = df_Fruits_Banana.mean(axis=0)
    df_Fruits_Corn = df_Fruits_Corn.mean(axis=0)
    df_Fruits_Tomata = df_Fruits_Tomata.mean(axis=0)
    df_Fruits_Orange = df_Fruits_Orange.mean(axis=0)
    df_Fruits_Pear = df_Fruits_Pear.mean(axis=0)
    df_Fruits_Date = df_Fruits_Date.mean(axis=0)
    df_Plants_Succulent = df_Plants_Succulent.mean(axis=0)
    df_Plants_Greenbasket = df_Plants_Greenbasket.mean(axis=0)
    # print(df0_Size0)

    # 画图
    plotMaxLength = 300
    draw(plotMaxLength,
         df_Fruits_Nothing,
         df_Fruits_Apple,
         df_Fruits_Banana,
         df_Fruits_Corn,
         df_Fruits_Tomata,
         df_Fruits_Orange,
         df_Fruits_Pear,
         df_Fruits_Date,
         df_Plants_Succulent,
         df_Plants_Greenbasket)

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    plotDataPoints()
