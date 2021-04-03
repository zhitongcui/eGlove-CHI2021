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

def draw(plotMaxLength, df0, df1, df2, df3, df4, df5, df6, df7):
    fig = plt.figure(figsize=(8,6))
    xmin = 1
    xmax = plotMaxLength
    ymin = 1
    ymax = 900
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))
    ax.set_title('Deformability Test', fontsize=24)
    ax.set_xlabel('Frequency (KHz)', fontsize=18)
    ax.set_ylabel('Amplitude Raw Reading (V)', fontsize=18)
    ax.xaxis.set_major_formatter(FuncFormatter(xaxis_update_scale_value))
    ax.yaxis.set_major_formatter(FuncFormatter(yaxis_update_scale_value))
    ax.tick_params(axis='both', labelsize=12)

    lineLabel0 = 'Flat'
    lineLabel1 = 'Fold once'
    lineLabel2 = 'Fold twice'
    lineLabel3 = 'Fold three'
    lineLabel4 = 'No stretch'
    lineLabel5 = '10% stretch'
    lineLabel6 = '20% stretch'
    lineLabel7 = '30% stretch'

    # one of the Tableau Colors from the 'T10' categorical palette (the default color cycle): {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}
    lines0 = ax.plot([], [], label=lineLabel0, color='tab:purple')[0]
    lines0.set_data(range(plotMaxLength), df0)
    lines1 = ax.plot([], [], label=lineLabel1, color='tab:red')[0]
    lines1.set_data(range(plotMaxLength), df1)
    lines2 = ax.plot([], [], label=lineLabel2, color='tab:blue')[0]
    lines2.set_data(range(plotMaxLength), df2)
    lines3 = ax.plot([], [], label=lineLabel3, color='tab:green')[0]
    lines3.set_data(range(plotMaxLength), df3)
    # lines4 = ax.plot([], [], label=lineLabel4, color='tab:orange')[0]
    # lines4.set_data(range(plotMaxLength), df4)
    # lines5 = ax.plot([], [], label=lineLabel5, color='tab:brown')[0]
    # lines5.set_data(range(plotMaxLength), df5)
    # lines6 = ax.plot([], [], label=lineLabel6, color='tab:gray')[0]
    # lines6.set_data(range(plotMaxLength), df6)
    # lines7 = ax.plot([], [], label=lineLabel7, color='tab:cyan')[0]
    # lines7.set_data(range(plotMaxLength), df7)

    ax.legend(loc="upper right", fontsize='18')
    plt.show()

def yaxis_update_scale_value(temp, position):
    result = temp/1024*5
    return "{}".format(round(result))

def xaxis_update_scale_value(temp, position):
    result = temp*5
    return "{}".format(round(result))

def plotDataPoints():

    df_Deformation_flat = loadFile('Exploration/DeformationandStretchability/Deformation_flat.csv')
    df_Deformation_fold_once = loadFile('Exploration/DeformationandStretchability/Deformation_fold_once.csv')
    df_Deformation_fold_twice = loadFile('Exploration/DeformationandStretchability/Deformation_fold_twice.csv')
    df_Deformation_fold_third = loadFile('Exploration/DeformationandStretchability/Deformation_fold_third.csv')
    df_Stretchability_normal = loadFile('Exploration/DeformationandStretchability/Stretchability_normal.csv')
    df_Stretchability_10percent = loadFile('Exploration/DeformationandStretchability/Stretchability_10percent.csv')
    df_Stretchability_20percent = loadFile('Exploration/DeformationandStretchability/Stretchability_20percent.csv')
    df_Stretchability_30percent = loadFile('Exploration/DeformationandStretchability/Stretchability_30percent.csv')

    df_Deformation_flat.drop(axis=1, columns='Deformation', inplace=True)
    df_Deformation_fold_once.drop(axis=1, columns='Deformation', inplace=True)
    df_Deformation_fold_twice.drop(axis=1, columns='Deformation', inplace=True)
    df_Deformation_fold_third.drop(axis=1, columns='Deformation', inplace=True)
    df_Stretchability_normal.drop(axis=1, columns='Stretchability', inplace=True)
    df_Stretchability_10percent.drop(axis=1, columns='Stretchability', inplace=True)
    df_Stretchability_20percent.drop(axis=1, columns='Stretchability', inplace=True)
    df_Stretchability_30percent.drop(axis=1, columns='Stretchability', inplace=True)

    # print(df0_Triangle.shape)

    df_Deformation_flat = df_Deformation_flat.mean(axis=0)
    df_Deformation_fold_once = df_Deformation_fold_once.mean(axis=0)
    df_Deformation_fold_twice = df_Deformation_fold_twice.mean(axis=0)
    df_Deformation_fold_third = df_Deformation_fold_third.mean(axis=0)
    df_Stretchability_normal = df_Stretchability_normal.mean(axis=0)
    df_Stretchability_10percent = df_Stretchability_10percent.mean(axis=0)
    df_Stretchability_20percent = df_Stretchability_20percent.mean(axis=0)
    df_Stretchability_30percent = df_Stretchability_30percent.mean(axis=0)
    # print(df0_Size0)

    # 画图
    plotMaxLength = 300
    draw(plotMaxLength, df_Deformation_flat, df_Deformation_fold_once, df_Deformation_fold_twice, df_Deformation_fold_third, df_Stretchability_normal, df_Stretchability_10percent, df_Stretchability_20percent, df_Stretchability_30percent)

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    plotDataPoints()
