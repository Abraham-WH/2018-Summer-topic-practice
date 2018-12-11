import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors
from sklearn.cluster import KMeans,MiniBatchKMeans
from sklearn.datasets.samples_generator import make_blobs
from sklearn.metrics.pairwise import pairwise_distances_argmin

#解决中文显示问题

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

#读完整信息

X_data = []

F0 = open(r"E:\info.txt", "r",encoding = 'utf-8')
List_row = F0.readlines()
for i in range(len(List_row)):
    column_list = List_row[i].strip().split(" ")    # 每一行split后是一个列表
    X_data.append(column_list)               # 加入list_source
F0.close()

#读样本数据 size: n*7

X = []

F1 = open(r"E:\data.txt", "r",encoding = 'utf-8')
List_row = F1.readlines()

for i in range(len(List_row)):
    column_list = List_row[i].strip("\ufeff").split(" ")    # 每一行split后是一个列表
    X.append(column_list[0:len(column_list)-1])               # 加入list_source
F1.close()
#print(X)
X = np.array(X)

#初始化15个中心

centers = [[10000,2,43,12,4,7500],[20000,9000,43,13,4,7500],[50000,600,43,42,4,7500],[60000,9000,43,8,3,7500],[80000,600,43,21,4,7500],[100000,600,43,7,4,7500],[30000,1,43,9,2,4500],[40000,10000,43,18,2,6000],[70000,1,43,40,4,4500],[90000,20,43,19,4,6750],[110000,60,43,13,4,6000],[10000,1,43,28,4,7500],[20000,10,43,12,4,7500],[50000,80,43,8,4,7500],[60000,10,43,43,4,7500]]
clusters = len(centers)
#聚类数目为15
k_means =  KMeans(init="k-means++",n_clusters=clusters,random_state=28)
t0 = time.time()
k_means.fit(X)      #模型训练
km_batch = time.time()-t0       #使用kmeans训练数据消耗的时间
#print("K-Means算法模型训练消耗时间:%.4fs"%km_batch)


#构建mini batch kmeans算法

batch_size = 100        #采样集的大小
mbk = MiniBatchKMeans(init="k-means++",n_clusters=clusters,batch_size=batch_size,random_state=28)
t0 = time.time()
mbk.fit(X)
mbk_batch = time.time()-t0
#print("Mini Batch K-Means算法模型训练消耗时间:%.4fs"%mbk_batch)

#预测结果,X_train为X加上预测值, size:n*(6+1)

km_y_hat = k_means.predict(X)
mbk_y_hat = mbk.predict(X)
np.array(X)
np.array(km_y_hat)
c = np.column_stack((X,km_y_hat))
X_train = c.tolist()
#print(X_train)

F4 = open("E:\\result.txt", "a",encoding = 'utf-8')
X_in = str(X_train)
F4.write(X_in)
F4.close()

#获取聚类中心点并对其排序

k_means_cluster_center = k_means.cluster_centers_
mbk_cluster_center = mbk.cluster_centers_
#print("K-Means算法聚类中心点:\n center=",k_means_cluster_center)
#print("Mini Batch K-Means算法聚类中心点:\n center=",mbk_cluster_center)
order = pairwise_distances_argmin(k_means_cluster_center,mbk_cluster_center)

#读取用户数据，找最优 x_user  返回推荐信息recommend

X_user = []

F2 = open(r"E:\user.txt", "r",encoding = 'utf-8')
List_row = F2.readlines()
for i in range(len(List_row)):
    column_list = List_row[i].strip().split(" ")    # 每一行split后是一个列表
    X_user.append(column_list)               # 加入list_source
F2.close()

print("用户历史数据为：",X_user)
recommend = []

X_temp = X_train

F3 = open("E:\\recommend.txt", "a",encoding = 'utf-8')
for i in range (0,len(X_user)):
    key = int (X_user[i][6])
    j = 0
    rank = 0
    index = 0
    while j < len(X):
        if int (X_temp[j][6]) == key and int (X_temp[j][5]) > rank and X_temp[j] != X_user[i] :
            rank = int (X_temp[j][5])
            index = j
        j = j + 1
    w_in = str(X_data[index][0])
    X_temp[index][5] = -1
    F3.write(w_in + '\n')
    w_in = str(X_data[index][7])
    F3.write(w_in + '\n')
    recommend.append(X_data[index])

print("为您推荐：",recommend)
F3.close()

