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

def draw(plotMaxLength, df0, df1, df2, df3, df4, df5, df6, df7, df8):
    fig = plt.figure(figsize=(16,10))
    xmin = 1
    xmax = plotMaxLength
    ymin = 1
    ymax = 1024
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax.set_title('Amplitude Response', fontsize=18)
    ax.set_xlabel('Frequency (KHz)', fontsize=16)
    ax.set_ylabel('Amplitude Raw Reading (V)', fontsize=16)


    lineLabel0 = 'df_Ear'
    lineLabel1 = 'df_Righthand'
    lineLabel2 = 'df_Elbow'
    lineLabel3 = 'df_Chest'
    lineLabel4 = 'df_Waist'
    lineLabel5 = 'df_Knee'
    lineLabel6 = 'df_Forehead'
    lineLabel7 = 'df_Xiaba'
    lineLabel8 = 'df_Nothing'

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
    lines8 = ax.plot([], [], label=lineLabel8, color='tab:pink')[0]
    lines8.set_data(range(plotMaxLength), df8)

    ax.legend(loc="upper right", fontsize='large')
    plt.show()


def plotDataPoints():

    df_Nothing = loadFile('Exploration/DailyObjects/Objects_Nothing.csv')
    df_Xiaba = loadFile('Exploration/BodyParts/BodyParts_Xiaba.csv')
    df_Ear = loadFile('Exploration/BodyParts/BodyParts_Ear.csv')
    df_Righthand = loadFile('Exploration/BodyParts/BodyParts_Righthand.csv')
    df_Elbow = loadFile('Exploration/BodyParts/BodyParts_Elbow.csv')
    df_Chest = loadFile('Exploration/BodyParts/BodyParts_Chest.csv')
    df_Waist = loadFile('Exploration/BodyParts/BodyParts_Waist.csv')
    df_Knee = loadFile('Exploration/BodyParts/BodyParts_Knee.csv')
    df_Forehead = loadFile('Exploration/BodyParts/BodyParts_Forehead.csv')

    df_Nothing.drop(axis=1, columns='Objects', inplace=True)
    df_Xiaba.drop(axis=1, columns='BodyParts', inplace=True)
    df_Ear.drop(axis=1, columns='BodyParts', inplace=True)
    df_Righthand.drop(axis=1, columns='BodyParts', inplace=True)
    df_Elbow.drop(axis=1, columns='BodyParts', inplace=True)
    df_Chest.drop(axis=1, columns='BodyParts', inplace=True)
    df_Waist.drop(axis=1, columns='BodyParts', inplace=True)
    df_Knee.drop(axis=1, columns='BodyParts', inplace=True)
    df_Forehead.drop(axis=1, columns='BodyParts', inplace=True)

    # print(df0_Triangle.shape)

    df_Nothing = df_Nothing.mean(axis=0)
    df_Xiaba = df_Xiaba.mean(axis=0)
    df_Ear = df_Ear.mean(axis=0)
    df_Righthand = df_Righthand.mean(axis=0)
    df_Elbow = df_Elbow.mean(axis=0)
    df_Chest = df_Chest.mean(axis=0)
    df_Waist = df_Waist.mean(axis=0)
    df_Knee = df_Knee.mean(axis=0)
    df_Forehead = df_Forehead.mean(axis=0)
    # print(df0_Size0)

    # 画图
    plotMaxLength = 300
    draw(plotMaxLength, df_Ear, df_Righthand, df_Elbow, df_Chest, df_Waist, df_Knee, df_Forehead, df_Xiaba, df_Nothing)

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    plotDataPoints()
