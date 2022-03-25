#!/usr/bin/python
# -*- coding: GBK -*-
# 因为文件中有中文，所以选择GBK编码
import numpy as np
from sklearn.cluster import KMeans


def loadData(filePath):
    # r+读写打开一个文本文件
    fr = open(filePath, 'r+')
    # .read()每次读取整个文件，它通常用于将文件内容放到一个字符串变量中
    # .readlines()一次读取整个文件,存为list
    # .readline()每次只读取1行，通常比.readlines()慢得多
    lines = fr.readlines()
    # retData用来存储城市的各项消费信息
    # retCityName:用来存储城市名称
    retData = []
    retCityName = []
    print(lines)
    for line in lines:
        # strip()删除字符串头尾指定的字符(默认为空格或换行符)
        # split(",")以，为切片
        items = line.strip().split(",")
        # 城市名称
        retCityName.append(items[0])
        # 把每一个城市的各项数据放到一个list里
        retData.append([float(items[i]) for i in range(1, len(items))])

    return retData, retCityName


if __name__ == '__main__':
    data, cityName = loadData('city.txt')
    # 创建对象
    km = KMeans(n_clusters=3)
    # 打标签
    label = km.fit_predict(data)
    # 利用聚类中心，计算expense
    expenses = np.sum(km.cluster_centers_, axis=1)
    CityCluster = [[], [], []]
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])
    for i in range(len(CityCluster)):
        print("Expenses:%.2f" % expenses[i])
        print(CityCluster[i])



