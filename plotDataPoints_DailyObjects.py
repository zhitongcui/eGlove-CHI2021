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

def draw(plotMaxLength, df0, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13):
    fig = plt.figure(figsize=(16,10))
    xmin = 1
    xmax = plotMaxLength
    ymin = 1
    ymax = 1024
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax.set_title('Amplitude Response', fontsize=18)
    ax.set_xlabel('Frequency (KHz)', fontsize=16)
    ax.set_ylabel('Amplitude Raw Reading (V)', fontsize=16)

    lineLabel0 = 'df_Nothing'
    lineLabel1 = 'df_AirPods'
    lineLabel2 = 'df_Stainless_steel_cup_full_water'
    lineLabel3 = 'df_Stainless_steel_cup_empty_water'
    lineLabel4 = 'df_Plastic_cup_full_water'
    lineLabel5 = 'df_Plastic_cup_empty_water'
    lineLabel6 = 'df_Popcan'
    lineLabel7 = 'df_318Key_cui'
    lineLabel8 = 'df_Bowl'
    lineLabel9 = 'df_Dookknob'
    lineLabel10 = 'df_Glass_cui'
    lineLabel11 = 'df_Oneplus'
    lineLabel12 = 'df_iPhoneXR'
    lineLabel13 = 'df_Soundbox'

    # one of the Tableau Colors from the 'T10' categorical palette (the default color cycle): {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}
    lines0 = ax.plot([], [], label=lineLabel0, color='tab:purple')[0]
    lines0.set_data(range(plotMaxLength), df0)
    # lines1 = ax.plot([], [], label=lineLabel1, color='tab:red')[0]    # Airpods无法识别
    # lines1.set_data(range(plotMaxLength), df1)
    lines2 = ax.plot([], [], label=lineLabel2, color='tab:blue')[0]
    lines2.set_data(range(plotMaxLength), df2)
    lines3 = ax.plot([], [], label=lineLabel3, color='tab:green')[0]
    lines3.set_data(range(plotMaxLength), df3)
    lines4 = ax.plot([], [], label=lineLabel4, color='tab:orange')[0]
    lines4.set_data(range(plotMaxLength), df4)
    # lines5 = ax.plot([], [], label=lineLabel5, color='tab:brown')[0]    # df_Plastic_cup_empty_water 塑料杯没有水无法识别
    # lines5.set_data(range(plotMaxLength), df5)
    lines6 = ax.plot([], [], label=lineLabel6, color='tab:gray')[0]
    lines6.set_data(range(plotMaxLength), df6)
    lines7 = ax.plot([], [], label=lineLabel7, color='tab:red')[0]
    lines7.set_data(range(plotMaxLength), df7)
    lines8 = ax.plot([], [], label=lineLabel8, color='tab:blue')[0]
    lines8.set_data(range(plotMaxLength), df8)
    lines9 = ax.plot([], [], label=lineLabel9, color='tab:pink')[0]
    lines9.set_data(range(plotMaxLength), df9)
    lines10 = ax.plot([], [], label=lineLabel10, color='tab:cyan')[0]
    lines10.set_data(range(plotMaxLength), df10)
    lines11 = ax.plot([], [], label=lineLabel11, color='tab:brown')[0]
    lines11.set_data(range(plotMaxLength), df11)
    lines12 = ax.plot([], [], label=lineLabel12, color='tab:olive')[0]
    lines12.set_data(range(plotMaxLength), df12)
    lines13 = ax.plot([], [], label=lineLabel13, color='tab:cyan')[0]
    lines13.set_data(range(plotMaxLength), df13)

    ax.legend(loc="upper right", fontsize='large')
    plt.show()


def plotDataPoints():

    df_Nothing = loadFile('Exploration/DailyObjects/Objects_Nothing.csv')
    df_AirPods = loadFile('Exploration/DailyObjects/Objects_AirPods.csv')
    df_Stainless_steel_cup_full_water = loadFile('Exploration/DailyObjects/Objects_Stainless_steel_cup_full_water.csv')
    df_Stainless_steel_cup_empty_water = loadFile('Exploration/DailyObjects/Objects_Stainless_steel_cup_empty_water.csv')
    df_Plastic_cup_full_water = loadFile('Exploration/DailyObjects/Objects_Plastic_cup_full_water.csv')
    df_Plastic_cup_empty_water = loadFile('Exploration/DailyObjects/Objects_Plastic_cup_empty_water.csv')
    df_Popcan = loadFile('Exploration/DailyObjects/Objects_Popcan.csv')
    df_318Key_cui = loadFile('Exploration/DailyObjects/Objects_318Key_cui.csv')
    df_Bowl = loadFile('Exploration/DailyObjects/Objects_Bowl.csv')
    df_Dookknob = loadFile('Exploration/DailyObjects/Objects_Dookknob.csv')
    df_Glass_cui = loadFile('Exploration/DailyObjects/Objects_Glass_cui.csv')
    df_Oneplus = loadFile('Exploration/DailyObjects/Objects_Oneplus.csv')
    df_iPhoneXR = loadFile('Exploration/DailyObjects/Objects_iPhoneXR.csv')
    df_Soundbox = loadFile('Exploration/DailyObjects/Objects_Soundbox.csv')


    df_Nothing.drop(axis=1, columns='Objects', inplace=True)
    df_AirPods.drop(axis=1, columns='Objects', inplace=True)
    df_Stainless_steel_cup_full_water.drop(axis=1, columns='Objects', inplace=True)
    df_Stainless_steel_cup_empty_water.drop(axis=1, columns='Objects', inplace=True)
    df_Plastic_cup_full_water.drop(axis=1, columns='Objects', inplace=True)
    df_Plastic_cup_empty_water.drop(axis=1, columns='Objects', inplace=True)
    df_Popcan.drop(axis=1, columns='Objects', inplace=True)
    df_318Key_cui.drop(axis=1, columns='Objects', inplace=True)
    df_Bowl.drop(axis=1, columns='Objects', inplace=True)
    df_Dookknob.drop(axis=1, columns='Objects', inplace=True)
    df_Glass_cui.drop(axis=1, columns='Objects', inplace=True)
    df_Oneplus.drop(axis=1, columns='Objects', inplace=True)
    df_iPhoneXR.drop(axis=1, columns='Objects', inplace=True)
    df_Soundbox.drop(axis=1, columns='Objects', inplace=True)

    # print(df0_Triangle.shape)

    df_Nothing = df_Nothing.mean(axis=0)
    df_AirPods = df_AirPods.mean(axis=0)
    df_Stainless_steel_cup_full_water = df_Stainless_steel_cup_full_water.mean(axis=0)
    df_Stainless_steel_cup_empty_water = df_Stainless_steel_cup_empty_water.mean(axis=0)
    df_Plastic_cup_full_water = df_Plastic_cup_full_water.mean(axis=0)
    df_Plastic_cup_empty_water = df_Plastic_cup_empty_water.mean(axis=0)
    df_Popcan = df_Popcan.mean(axis=0)
    df_318Key_cui = df_318Key_cui.mean(axis=0)
    df_Bowl = df_Bowl.mean(axis=0)
    df_Dookknob = df_Dookknob.mean(axis=0)
    df_Glass_cui = df_Glass_cui.mean(axis=0)
    df_Oneplus = df_Oneplus.mean(axis=0)
    df_iPhoneXR = df_iPhoneXR.mean(axis=0)
    df_Soundbox = df_Soundbox.mean(axis=0)
    # print(df0_Size0)

    # 画图
    plotMaxLength = 300
    draw(plotMaxLength,
         df_Nothing,
         df_AirPods,
         df_Stainless_steel_cup_full_water,
         df_Stainless_steel_cup_empty_water,
         df_Plastic_cup_full_water,
         df_Plastic_cup_empty_water,
         df_Popcan,
         df_318Key_cui,
         df_Bowl,
         df_Dookknob,
         df_Glass_cui,
         df_Oneplus,
         df_iPhoneXR,
         df_Soundbox)

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    plotDataPoints()
