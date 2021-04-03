import numpy as np
import matplotlib.pyplot as plt
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
    fig = plt.figure(figsize=(16,10))
    xmin = 1
    xmax = plotMaxLength
    ymin = 1
    ymax = 800
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax.set_title('Amplitude Response', fontsize=18)
    ax.set_xlabel('Frequency (KHz)', fontsize=16)
    ax.set_ylabel('Amplitude Raw Reading (V)', fontsize=16)


    lineLabel1 = 'df0_foil'
    lineLabel2 = 'df0_small_resistence'
    lineLabel3 = 'df0_medium_resistence'
    lineLabel4 = 'df0_high_resistence'

    # one of the Tableau Colors from the 'T10' categorical palette (the default color cycle): {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}
    lines1 = ax.plot([], [], label=lineLabel1, color='tab:red')[0]
    lines1.set_data(range(plotMaxLength), df0)
    lines2 = ax.plot([], [], label=lineLabel2, color='tab:blue')[0]
    lines2.set_data(range(plotMaxLength), df1)
    lines3 = ax.plot([], [], label=lineLabel3, color='tab:green')[0]
    lines3.set_data(range(plotMaxLength), df2)
    lines4 = ax.plot([], [], label=lineLabel4, color='tab:orange')[0]
    lines4.set_data(range(plotMaxLength), df3)

    ax.legend(loc="upper right", fontsize='large')
    plt.show()


def plotDataPoints():
    df0_foil = loadFile('Exploration/Material/Material_foil.csv')
    df0_small = loadFile('Exploration/Material/Material_small.csv')
    df0_medium = loadFile('Exploration/Material/Material_medium.csv')
    df0_large = loadFile('Exploration/Material/Material_large.csv')

    df0_foil.drop(axis=1, columns='Material', inplace=True)
    df0_small.drop(axis=1, columns='Material', inplace=True)
    df0_medium.drop(axis=1, columns='Material', inplace=True)
    df0_large.drop(axis=1, columns='Material', inplace=True)

    # print(df0_Triangle.shape)

    df0_foil = df0_foil.mean(axis=0)
    df0_small = df0_small.mean(axis=0)
    df0_medium = df0_medium.mean(axis=0)
    df0_large = df0_large.mean(axis=0)
    # print(df0_Size0)
    # print(df0_Size4)

    # 画图
    plotMaxLength = 180
    draw(plotMaxLength, df0_foil, df0_small, df0_medium, df0_large)

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    plotDataPoints()
