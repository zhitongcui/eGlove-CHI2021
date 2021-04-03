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

def draw(plotMaxLength, df0, df1, df2, df3):
    fig = plt.figure(figsize=(8,6))
    xmin = 1
    xmax = plotMaxLength
    ymin = 1
    ymax = 900
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax.set_title('Shape Test', fontsize=24)
    ax.set_xlabel('Frequency (KHz)', fontsize=18)
    ax.set_ylabel('Amplitude Raw Reading (V)', fontsize=18)
    ax.xaxis.set_major_formatter(FuncFormatter(xaxis_update_scale_value))
    ax.yaxis.set_major_formatter(FuncFormatter(yaxis_update_scale_value))
    ax.tick_params(axis='both', labelsize=12)

    lineLabel0 = 'Rectangle'
    lineLabel1 = 'Triangle'
    lineLabel2 = 'Square'
    lineLabel3 = 'Circle'

    lines0 = ax.plot([], [], label=lineLabel0, color='tab:red')[0]
    lines0.set_data(range(plotMaxLength), df0)
    lines1 = ax.plot([], [], label=lineLabel1, color='tab:blue')[0]
    lines1.set_data(range(plotMaxLength), df1)
    lines2 = ax.plot([], [], label=lineLabel2, color='tab:green')[0]
    lines2.set_data(range(plotMaxLength), df2)
    lines3 = ax.plot([], [], label=lineLabel3, color='tab:orange')[0]
    lines3.set_data(range(plotMaxLength), df3)

    ax.legend(loc="upper right", fontsize='18')
    plt.show()

def yaxis_update_scale_value(temp, position):
    result = temp/1024*5
    return "{}".format(round(result))

def xaxis_update_scale_value(temp, position):
    result = temp*5
    return "{}".format(round(result))

def plotDataPoints():
    df0_Rectangle = loadFile('Exploration/Shape/Shape_Rectangle.csv')
    df0_Triangle = loadFile('Exploration/Shape/Shape_Triangle.csv')
    df0_Square = loadFile('Exploration/Shape/Shape_Square.csv')
    df0_Circle = loadFile('Exploration/Shape/Shape_Circle.csv')

    df0_Rectangle.drop(axis=1, columns='Shape', inplace=True)
    df0_Triangle.drop(axis=1, columns='Shape', inplace=True)
    df0_Square.drop(axis=1, columns='Shape', inplace=True)
    df0_Circle.drop(axis=1, columns='Shape', inplace=True)

    # print(df0_Triangle.shape)

    df0_Rectangle = df0_Rectangle.mean(axis=0)
    df0_Triangle = df0_Triangle.mean(axis=0)
    df0_Square = df0_Square.mean(axis=0)
    df0_Circle = df0_Circle.mean(axis=0)
    # print(df0_Rectangle)

    # 画图
    plotMaxLength = 300
    draw(plotMaxLength, df0_Rectangle, df0_Triangle, df0_Square, df0_Circle)

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    plotDataPoints()
