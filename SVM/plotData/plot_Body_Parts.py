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

def draw(plotMaxLength, df0, df1, df2, df3, df4, df5, df6, df7, df8):
    fig = plt.figure(figsize=(12,8))
    xmin = 1
    xmax = plotMaxLength
    ymin = 1
    ymax = 900
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax.set_title('Body Parts', fontsize=28)
    ax.set_xlabel('Frequency (KHz)', fontsize=24)
    ax.set_ylabel('Amplitude Raw Reading (V)', fontsize=24)
    ax.xaxis.set_major_formatter(FuncFormatter(xaxis_update_scale_value))
    ax.yaxis.set_major_formatter(FuncFormatter(yaxis_update_scale_value))
    ax.tick_params(axis='both', labelsize=14)

    lineLabel0 = 'Clothes' #这里添加了只通过衣服的信号作为一个对照组，因为有评委认为电流通过了衣服而非身体
    lineLabel1 = 'Ear'
    lineLabel2 = 'Chin'
    lineLabel3 = 'Chest'
    lineLabel4 = 'Elbow'
    lineLabel5 = 'Righthand'
    lineLabel6 = 'Waist'
    lineLabel7 = 'Knee'
    lineLabel8 = 'Mid-air' # 这里是不接触任何衣服或者身体部位的对照组

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
    # lines5 = ax.plot([], [], label=lineLabel5, color='tab:brown')[0]
    # lines5.set_data(range(plotMaxLength), df5)
    lines6 = ax.plot([], [], label=lineLabel6, color='tab:gray')[0]
    lines6.set_data(range(plotMaxLength), df6)
    lines7 = ax.plot([], [], label=lineLabel7, color='tab:cyan')[0]
    lines7.set_data(range(plotMaxLength), df7)
    lines8 = ax.plot([], [], label=lineLabel8, color='tab:brown')[0]
    lines8.set_data(range(plotMaxLength), df8)

    ax.legend(loc="upper right", fontsize='16')
    plt.show()

def yaxis_update_scale_value(temp, position):
    result = temp/1024*5
    return "{}".format(round(result))

def xaxis_update_scale_value(temp, position):
    result = temp*5
    return "{}".format(round(result))

def plotDataPoints():

    df_No_Contact = loadFile('../data/BPR/BodyParts_No_Contact.csv')
    df_BodyParts_Ear = loadFile('../data/BPR/BodyParts_Ear.csv')
    df_BodyParts_Chin = loadFile('../data/BPR/BodyParts_Chin.csv')
    df_BodyParts_Chest = loadFile('../data/BPR/BodyParts_Chest.csv')
    df_BodyParts_Elbow = loadFile('../data/BPR/BodyParts_Elbow.csv')
    df_BBodyParts_Righthand = loadFile('../data/BPR/BodyParts_Righthand.csv')
    df_BodyParts_Waist = loadFile('../data/BPR/BodyParts_Waist.csv')
    df_BodyParts_Knee = loadFile('../data/BPR/BodyParts_Knee.csv')
    df_through_clothing = loadFile('../data/BPR/Clothing_Control_Size_64.csv')  # 加载只通过衣服的对照组数据

    df_No_Contact.drop(axis=1, columns='BodyParts', inplace=True)
    df_BodyParts_Ear.drop(axis=1, columns='BodyParts', inplace=True)
    df_BodyParts_Chin.drop(axis=1, columns='BodyParts', inplace=True)
    df_BodyParts_Chest.drop(axis=1, columns='BodyParts', inplace=True)
    df_BodyParts_Elbow.drop(axis=1, columns='BodyParts', inplace=True)
    df_BBodyParts_Righthand.drop(axis=1, columns='BodyParts', inplace=True)
    df_BodyParts_Waist.drop(axis=1, columns='BodyParts', inplace=True)
    df_BodyParts_Knee.drop(axis=1, columns='BodyParts', inplace=True)
    df_through_clothing.drop(axis=1, columns='Size', inplace=True)

    # print(df_BodyParts_Knee.shape)
    # print(df_Plants_Greenbasket.shape)

    df_No_Contact = df_No_Contact.mean(axis=0)
    df_BodyParts_Ear = df_BodyParts_Ear.mean(axis=0)
    df_BodyParts_Chin = df_BodyParts_Chin.mean(axis=0)
    df_BodyParts_Chest = df_BodyParts_Chest.mean(axis=0)
    df_BodyParts_Elbow = df_BodyParts_Elbow.mean(axis=0)
    df_BBodyParts_Righthand = df_BBodyParts_Righthand.mean(axis=0)
    df_BodyParts_Waist = df_BodyParts_Waist.mean(axis=0)
    df_BodyParts_Knee = df_BodyParts_Knee.mean(axis=0)
    df_through_clothing = df_through_clothing.mean(axis=0)
    # print(df0_Size0)

    # 画图
    plotMaxLength = 300
    draw(plotMaxLength,
         df_No_Contact,
         df_BodyParts_Ear,
         df_BodyParts_Chin,
         df_BodyParts_Chest,
         df_BodyParts_Elbow,
         df_BBodyParts_Righthand,
         df_BodyParts_Waist,
         df_BodyParts_Knee,
         df_through_clothing)

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    plotDataPoints()
