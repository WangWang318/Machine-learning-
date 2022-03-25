#!/usr/bin/python
# -*- coding: GBK -*-
# ��Ϊ�ļ��������ģ�����ѡ��GBK����
import numpy as np
from sklearn.cluster import KMeans


def loadData(filePath):
    # r+��д��һ���ı��ļ�
    fr = open(filePath, 'r+')
    # .read()ÿ�ζ�ȡ�����ļ�����ͨ�����ڽ��ļ����ݷŵ�һ���ַ���������
    # .readlines()һ�ζ�ȡ�����ļ�,��Ϊlist
    # .readline()ÿ��ֻ��ȡ1�У�ͨ����.readlines()���ö�
    lines = fr.readlines()
    # retData�����洢���еĸ���������Ϣ
    # retCityName:�����洢��������
    retData = []
    retCityName = []
    print(lines)
    for line in lines:
        # strip()ɾ���ַ���ͷβָ�����ַ�(Ĭ��Ϊ�ո���з�)
        # split(",")�ԣ�Ϊ��Ƭ
        items = line.strip().split(",")
        # ��������
        retCityName.append(items[0])
        # ��ÿһ�����еĸ������ݷŵ�һ��list��
        retData.append([float(items[i]) for i in range(1, len(items))])

    return retData, retCityName


if __name__ == '__main__':
    data, cityName = loadData('city.txt')
    # ��������
    km = KMeans(n_clusters=3)
    # ���ǩ
    label = km.fit_predict(data)
    # ���þ������ģ�����expense
    expenses = np.sum(km.cluster_centers_, axis=1)
    CityCluster = [[], [], []]
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])
    for i in range(len(CityCluster)):
        print("Expenses:%.2f" % expenses[i])
        print(CityCluster[i])



