# model_OR_sevenfruits.py
# FreqStarts at 100khz
# minFreq = 5000, steps = 300
import numpy as np
import pandas as pd
import sklearn
from sklearn import svm #  includes Support Vector Machine algorithms
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score # 运用交叉验证进行模型评估（可以写到论文中去）

def loadFile(path):
    # pandas默认把第一行作为列属性，第一行不能用
    # index_col=0将第一列作为索引
    df = pd.read_csv(path, index_col=0, converters={'BodyParts': typeConverter})
    # print(df.iloc[0]   # iloc通过行号索引来确定行
    # print(df)
    return df

def typeConverter(type):
    # 字符串前面加 'r'，表示这是个普通字符串
    fruits_type = {r'No_Contact': 0,
                   r'Ear': 1,
                   r'Righthand': 2,
                   r'Elbow': 3,
                   r'Chin': 4,
                   r'Chest': 5,
                   r'Knee': 6,
                   r'Waist': 7}
    # 这个函数返回数组，数组包含水果的7种类型
    return fruits_type[type]

def objectConverter(type):
    fruits_type = {0: r'No Contact',
                   1: r'Ear',
                   2: r'Righthand',
                   3: r'Elbow',
                   4: r'Chin',
                   5: r'Chest',
                   6: r'Knee',
                   7: r'Waist'}
    return fruits_type[type]

def splitData(data):
    # numpy.split(ary, indices_or_sections, axis=0), indices_or_sections为沿轴切分的位置，因为数据前4列是特征值，第5列是类型结果
    # axis: 沿着哪个维度进行切向，默认为0横向切分,为1时纵向切分
    X = data.iloc[:,:300]
    y = data.iloc[:,[300]]
    # 现在使用
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, random_state = 2)
    return X_train, X_test, y_train, y_test

def trainSVM():

    # 从路径中读取csv数据
    df0 = loadFile('../data/BPR/BodyParts_No_Contact.csv')
    df1 = loadFile('../data/BPR/BodyParts_Ear.csv')
    df2 = loadFile('../data/BPR/BodyParts_Righthand.csv')
    df3 = loadFile('../data/BPR/BodyParts_Elbow.csv')
    df4 = loadFile('../data/BPR/BodyParts_Chin.csv')
    df5 = loadFile('../data/BPR/BodyParts_Chest.csv')
    df6 = loadFile('../data/BPR/BodyParts_Knee.csv')
    df7 = loadFile('../data/BPR/BodyParts_Waist.csv')
    # df8 = loadFile('data/OR_Daily/Objects_Stainless_Cup_No_Water.csv')
    # df9 = loadFile('data/OR_Daily/Objects_Stainless_Cup_Full_Water.csv')
    # df10 = loadFile('data/OR_Daily/Objects_Bowl.csv')
    # df11 = loadFile('data/OR_Daily/Objects_Nothing.csv')

    # 将所有数据合在一起
    df_alldata = pd.concat([df0, df1, df2, df3, df4, df5, df6, df7], axis=0, ignore_index=True)
    print(df_alldata)

    # 运用交叉验证进行模型评估, K-fold Cross Validation，有助于判断模型是否过拟合，以及找到最好的参数
    # C为正则化系数，Regularization parameter, kernel='rbf' is default, gamma = scale
    clf = svm.SVC(C=10, kernel='poly', gamma='scale', coef0=1, decision_function_shape='ovr')
    X = df_alldata.iloc[:,:300]
    y = df_alldata.iloc[:,[300]]
    scores = cross_val_score(clf, X, y.values.ravel(), cv=10, scoring='accuracy')   # Stratified K-Folds cross-validator 分层交叉验证
    print(scores)   # Return the mean accuracy on the given test data and labels
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2))    # 输出平均值与95%的置信区间误差

    # 随机拆分数据为训练集与测试集，生成clf评估器
    X_train, X_test, y_train, y_test = splitData(df_alldata)
    # 生成估计器
    clf.fit(X_train, y_train.values.ravel())   # numpy中的ravel()，将多为数组转换为1维数组，由于dataframe不支持ravel，因此使用.values.ravel()

    print(clf.score(X_train, y_train))  # predict()训练集的准确度
    print(clf.predict(X_train))         # 输出x_train的预测结果
    print(clf.score(X_test, y_test))    # predict()测试集的准确度
    print(clf.predict(X_test))          # 输出x_test的预测结果

    return clf

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    trainSVM()
