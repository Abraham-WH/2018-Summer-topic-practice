import numpy as np

#读取用户数据，找最优 x_user  返回推荐信息recommend
X_train = []

X_data = []

F0 = open(r"E:\info.txt", "r",encoding = 'utf-8')
List_row = F0.readlines()
for i in range(len(List_row)):
    column_list = List_row[i].strip().split(" ")    # 每一行split后是一个列表
    X_data.append(column_list)               # 加入list_source
F0.close()

F1 = open(r"E:\result.txt", "r",encoding = 'utf-8')
List_row = F1.readlines()

for i in range(len(List_row)):
    column_list = List_row[i].strip("\ufeff").split(" ")    # 每一行split后是一个列表
    X_train.append(column_list[0:len(column_list)-1])               # 加入list_source
F1.close()

X_train = np.array(X_train)

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
print(X_temp)
F3 = open("E:\\recommend.txt", "a",encoding = 'utf-8')
for i in range (0,len(X_user)):
    key = int (X_user[i][6])
    j = 0
    rank = 0
    index = 0
    while j < len(X_data):
        if int (X_temp[j][6]) == key and int (X_temp[j][5]) > rank and X_temp[j] != X_user[i] :
            rank = int (X_temp[j][5])
            index = j
        j = j + 1
    w_in = str(X_data[index])
    X_temp[index][5] = -1
    F3.write(w_in)
    recommend.append(X_data[index])

print("为您推荐：",recommend)
F3.close()
