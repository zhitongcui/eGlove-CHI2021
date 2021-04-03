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

def draw(plotMaxLength, df0, df1, df2, df3, df4):
    fig = plt.figure(figsize=(16,10))
    xmin = 1
    xmax = plotMaxLength
    ymin = 1
    ymax = 800
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax.set_title('Amplitude Response', fontsize=18)
    ax.set_xlabel('Frequency (KHz)', fontsize=16)
    ax.set_ylabel('Amplitude Raw Reading (V)', fontsize=16)


    lineLabel1 = 'df_pureCotton'
    lineLabel2 = 'df_jean'
    lineLabel3 = 'df_terylene'
    lineLabel4 = 'df_leather'
    lineLabel5 = 'df_ourband'

    # one of the Tableau Colors from the 'T10' categorical palette (the default color cycle): {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}
    lines1 = ax.plot([], [], label=lineLabel1, color='tab:red')[0]
    lines1.set_data(range(plotMaxLength), df0)
    lines2 = ax.plot([], [], label=lineLabel2, color='tab:blue')[0]
    lines2.set_data(range(plotMaxLength), df1)
    lines3 = ax.plot([], [], label=lineLabel3, color='tab:green')[0]
    lines3.set_data(range(plotMaxLength), df2)
    lines4 = ax.plot([], [], label=lineLabel4, color='tab:orange')[0]
    lines4.set_data(range(plotMaxLength), df3)
    lines5 = ax.plot([], [], label=lineLabel5, color='tab:gray')[0]
    lines5.set_data(range(plotMaxLength), df4)

    ax.legend(loc="upper right", fontsize='large')
    plt.show()


def plotDataPoints():
    # 1: 迷彩，纯棉；2: 牛仔布；3: 涤纶；4: 人造皮革; 5: 我们目前使用的腕带，黑色的
    df_pureCotton = loadFile('Exploration/SkinLayer/SkinLayer_pureCotton.csv')
    df_jean = loadFile('Exploration/SkinLayer/SkinLayer_jean.csv')
    df_terylene = loadFile('Exploration/SkinLayer/SkinLayer_terylene.csv')
    df_leather = loadFile('Exploration/SkinLayer/SkinLayer_leather.csv')
    df_ourband = loadFile('Exploration/SkinLayer/SkinLayer_ourband.csv')

    df_pureCotton.drop(axis=1, columns='SkinLayer', inplace=True)
    df_jean.drop(axis=1, columns='SkinLayer', inplace=True)
    df_terylene.drop(axis=1, columns='SkinLayer', inplace=True)
    df_leather.drop(axis=1, columns='SkinLayer', inplace=True)
    df_ourband.drop(axis=1, columns='SkinLayer', inplace=True)

    # print(df0_Triangle.shape)

    df_pureCotton = df_pureCotton.mean(axis=0)
    df_jean = df_jean.mean(axis=0)
    df_terylene = df_terylene.mean(axis=0)
    df_leather = df_leather.mean(axis=0)
    df_ourband = df_ourband.mean(axis=0)
    # print(df0_Size0)
    # print(df0_Size4)

    # 画图
    plotMaxLength = 180
    draw(plotMaxLength, df_pureCotton, df_jean, df_terylene, df_leather, df_ourband)

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    plotDataPoints()
