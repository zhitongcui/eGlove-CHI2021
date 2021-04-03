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

def draw(plotMaxLength, df0, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11):
    fig = plt.figure(figsize=(12,8))
    xmin = 1
    xmax = plotMaxLength
    ymin = 1
    ymax = 900
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax.set_title('Daily Objects', fontsize=28)
    ax.set_xlabel('Frequency (KHz)', fontsize=24)
    ax.set_ylabel('Amplitude Raw Reading (V)', fontsize=24)
    ax.xaxis.set_major_formatter(FuncFormatter(xaxis_update_scale_value))
    ax.yaxis.set_major_formatter(FuncFormatter(yaxis_update_scale_value))
    ax.tick_params(axis='both', labelsize=14)

    lineLabel0 = 'Bluetooth speaker'
    lineLabel1 = 'Glasses'
    lineLabel2 = 'df_OnePlus_Phone'
    lineLabel3 = 'iPhone XR'
    lineLabel4 = 'Metal key'
    lineLabel5 = 'Pop can'
    lineLabel6 = 'Plastic cup with water'
    lineLabel7 = 'AirPods Charging Case'
    lineLabel8 = 'Stainless steel cup without water'
    lineLabel9 = 'Stainless steel cup with water'
    lineLabel10 = 'Porcelain bowl'
    lineLabel11 = 'No objects'

    # one of the Tableau Colors from the 'T10' categorical palette (the default color cycle): {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}
    lines11 = ax.plot([], [], label=lineLabel11, color='tab:pink')[0]
    lines11.set_data(range(plotMaxLength), df11)
    lines0 = ax.plot([], [], label=lineLabel0, color='tab:purple')[0]
    lines0.set_data(range(plotMaxLength), df0)
    lines1 = ax.plot([], [], label=lineLabel1, color='tab:red')[0]
    lines1.set_data(range(plotMaxLength), df1)
    # lines2 = ax.plot([], [], label=lineLabel2, color='tab:blue')[0]
    # lines2.set_data(range(plotMaxLength), df2)
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
    lines10 = ax.plot([], [], label=lineLabel10, color='tab:blue')[0]
    lines10.set_data(range(plotMaxLength), df10)

    ax.legend(loc="upper right", fontsize='16')
    plt.show()

def yaxis_update_scale_value(temp, position):
    result = temp/1024*5
    return "{}".format(round(result))

def xaxis_update_scale_value(temp, position):
    result = temp*5
    return "{}".format(round(result))

def plotDataPoints():

    df_Soundbox = loadFile('../data/OR_Daily/Objects_Soundbox.csv')
    df_Glasses = loadFile('../data/OR_Daily/Objects_Glasses.csv')
    df_OnePlus_Phone = loadFile('../data/OR_Daily/Objects_OnePlus_Phone.csv')
    df_iPhoneXR = loadFile('../data/OR_Daily/Objects_iPhoneXR.csv')
    df_Key = loadFile('../data/OR_Daily/Objects_Key.csv')
    df_Popcan = loadFile('../data/OR_Daily/Objects_Popcan.csv')
    df_Plastic_full_water = loadFile('../data/OR_Daily/Objects_Plastic_full_water.csv')
    df_AirPods_Chargebox = loadFile('../data/OR_Daily/Objects_AirPods_Chargebox.csv')
    df_Stainless_Cup_No_Water = loadFile('../data/OR_Daily/Objects_Stainless_Cup_No_Water.csv')
    df_Stainless_Cup_Full_Water = loadFile('../data/OR_Daily/Objects_Stainless_Cup_Full_Water.csv')
    df_Bowl = loadFile('../data/OR_Daily/Objects_Bowl.csv')
    df_Nothing = loadFile('../data/OR_Daily/Objects_Nothing.csv')

    df_Soundbox.drop(axis=1, columns='Objects', inplace=True)
    df_Glasses.drop(axis=1, columns='Objects', inplace=True)
    # df_OnePlus_Phone.drop(axis=1, columns='Objects', inplace=True)
    df_iPhoneXR.drop(axis=1, columns='Objects', inplace=True)
    df_Key.drop(axis=1, columns='Objects', inplace=True)
    df_Popcan.drop(axis=1, columns='Objects', inplace=True)
    df_Plastic_full_water.drop(axis=1, columns='Objects', inplace=True)
    df_AirPods_Chargebox.drop(axis=1, columns='Objects', inplace=True)
    df_Stainless_Cup_No_Water.drop(axis=1, columns='Objects', inplace=True)
    df_Stainless_Cup_Full_Water.drop(axis=1, columns='Objects', inplace=True)
    df_Bowl.drop(axis=1, columns='Objects', inplace=True)
    df_Nothing.drop(axis=1, columns='Objects', inplace=True)

    # print(df_AirPods_Chargebox.shape)
    # print(df_Stainless_Cup_Full_Water.shape)

    df_Soundbox = df_Soundbox.mean(axis=0)
    df_Glasses = df_Glasses.mean(axis=0)
    df_OnePlus_Phone = df_OnePlus_Phone.mean(axis=0)
    df_iPhoneXR = df_iPhoneXR.mean(axis=0)
    df_Key = df_Key.mean(axis=0)
    df_Popcan = df_Popcan.mean(axis=0)
    df_Plastic_full_water = df_Plastic_full_water.mean(axis=0)
    df_AirPods_Chargebox = df_AirPods_Chargebox.mean(axis=0)
    df_Stainless_Cup_No_Water = df_Stainless_Cup_No_Water.mean(axis=0)
    df_Stainless_Cup_Full_Water = df_Stainless_Cup_Full_Water.mean(axis=0)
    df_Bowl = df_Bowl.mean(axis=0)
    df_Nothing = df_Nothing.mean(axis=0)
    # print(df0_Size0)

    # 画图
    plotMaxLength = 300
    draw(plotMaxLength,
         df_Soundbox,
         df_Glasses,
         df_OnePlus_Phone,
         df_iPhoneXR,
         df_Key,
         df_Popcan,
         df_Plastic_full_water,
         df_AirPods_Chargebox,
         df_Stainless_Cup_No_Water,
         df_Stainless_Cup_Full_Water,
         df_Bowl,
         df_Nothing)

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    plotDataPoints()
