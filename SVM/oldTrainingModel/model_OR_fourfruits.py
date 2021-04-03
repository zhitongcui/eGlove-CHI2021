# model_OR_fourfruits.py
# minFreq = 4000, steps = 225
import numpy as np
import pandas as pd
import sklearn
from sklearn import svm #  includes Support Vector Machine algorithms
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score # 运用交叉验证进行模型评估（可以写到论文中去）

def loadFile(path):
    # pandas默认把第一行作为列属性，第一行不能用
    # index_col=0将第一列作为索引
    df = pd.read_csv(path, index_col=0, converters={'Object': typeConverter})
    # print(df.iloc[0]   # iloc通过行号索引来确定行
    # print(df)
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

def objectConverter(type):
    fruits_type = {0: r'noObject',
                   1: r'Apple',
                   2: r'Banana',
                   3: r'Cucumber'}
    return fruits_type[type]

def splitData(data):
    # numpy.split(ary, indices_or_sections, axis=0), indices_or_sections为沿轴切分的位置，因为数据前4列是特征值，第5列是类型结果
    # axis: 沿着哪个维度进行切向，默认为0横向切分,为1时纵向切分
    X = data.iloc[:,:450]
    y = data.iloc[:,[450]]
    # 现在使用
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.75, random_state = 2)
    return X_train, X_test, y_train, y_test

def trainSVM():
    # 从路径中读取csv数据
    df0_top = loadFile('data/OR_fourfruits/NoObject_Top.csv')
    df0_bot = loadFile('data/OR_fourfruits/NoObject_Bottom.csv')
    df1_top = loadFile('data/OR_fourfruits/Apple_Top.csv')
    df1_bot = loadFile('data/OR_fourfruits/Apple_Bottom.csv')
    df2_top = loadFile('data/OR_fourfruits/Banana_Top.csv')
    df2_bot = loadFile('data/OR_fourfruits/Banana_Bottom.csv')
    df3_top = loadFile('data/OR_fourfruits/Cucumber_Top.csv')
    df3_bot = loadFile('data/OR_fourfruits/Cucumber_Bottom.csv')

    # 拼接两个表的数据
    df_noObject = pd.concat([df0_top, df0_bot], axis=1, ignore_index=True)
    df_apple = pd.concat([df1_top, df1_bot], axis=1, ignore_index=True)
    df_banana = pd.concat([df2_top, df2_bot], axis=1, ignore_index=True)
    df_cucumber = pd.concat([df3_top, df3_bot], axis=1, ignore_index=True)

    # 从数据中删除多余的一列
    df_noObject.drop(axis=1, columns=225, inplace=True)
    df_apple.drop(axis=1, columns=225, inplace=True)
    df_banana.drop(axis=1, columns=225, inplace=True)
    df_cucumber.drop(axis=1, columns=225, inplace=True)

    # 检查是否正确删除中间的一行数据，':'表示行全选，'[255]'表示第255列，inplace=True表示在原数据上继续删除
    # print(df_apple.iloc[:,[225]])

    # 将所有数据合在一起
    df_alldata = pd.concat([df_noObject, df_apple, df_banana, df_cucumber], axis=0, ignore_index=True)

    # 运用交叉验证进行模型评估, K-fold Cross Validation，有助于判断模型是否过拟合，以及找到最好的参数
    # C为正则化系数，Regularization parameter, kernel='rbf' is default, gamma = scale
    clf = svm.SVC(C=10, kernel='poly', gamma='scale', coef0=1, decision_function_shape='ovr')
    X = df_alldata.iloc[:,:450]
    y = df_alldata.iloc[:,[450]]
    scores = cross_val_score(clf, X, y.values.ravel(), cv=10, scoring='accuracy')   # Stratified K-Folds cross-validator 分层交叉验证
    print(scores)   # Return the mean accuracy on the given test data and labels
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))    # 输出平均值与95%的置信区间误差

    # 随机拆分数据为训练集与测试集
    X_train, X_test, y_train, y_test = splitData(df_alldata)
    # 生成评估器
    clf.fit(X_train, y_train.values.ravel())  # numpy中的ravel()，将多为数组转换为1维数组，由于dataframe不支持ravel，因此使用.values.ravel()
    print(clf.score(X_test, y_test))          # predict()测试集的准确度
    print(clf.predict(X_test))                # 输出x_test的预测结果

    # 通过验证集，验证模型的准确率
    # df_test_top = loadFile('/Users/cuizhitong/Desktop/Cucumber_Top.csv')
    # df_test_bot = loadFile('/Users/cuizhitong/Desktop/Cucumber_Bottom.csv')
    # df_test = pd.concat([df_test_top, df_test_bot], axis=1, ignore_index=True)
    # df_test.drop(axis=1, columns=225, inplace=True)
    # X_test = df_test.iloc[:,:450]
    # print(clf.predict(X_test))

    # 将估计器返回给调用模型的文件
    return clf

# 运行当前脚本的主函数, 如果当前脚本作为包导入，则不运行此主函数
if __name__ == "__main__":
    trainSVM()
