import sys
import importlib
importlib.reload(sys)
import jieba
import jieba.analyse
 
if __name__=="__main__":

    data=open('E:\comment.txt',"r",encoding='utf-8')
    l = data.readline()

    while l:
        word_lst = []
        key_list=[]
        l=str(l)
    
        tags = jieba.cut(l,cut_all=False) #jieba分词
        for t in tags:
            if t != '！':#加去除的字符
                word_lst.append(t)
 
        word_dict= {}
        with open('E:\wordCount.txt','a+',encoding='utf-8') as wf2: #打开文件
 
            for item in word_lst:
                if item not in word_dict: #统计数量
                    word_dict[item] = 1
                else:
                    word_dict[item] += 1
       
                orderList=list(word_dict.values())
                orderList.sort(reverse=True)
            '''  
            for i in range(len(orderList)):
                for key in word_dict:
                    if word_dict[key]==orderList[i]:
                        wf2.write(key+' '+str(word_dict[key])+' ') #写入txt文档
                        key_list.append(key)
                        word_dict[key]=0
            wf2.write('\n')
            '''
            i = 1
            while i < 4 and i < len(orderList):
                i = i + 1
                for key in word_dict:
                    if word_dict[key]==orderList[i]:
                        wf2.write(key+' ') #写入txt文档
                        key_list.append(key)
                        word_dict[key]=0
            wf2.write('\n')
        l = data.readline()
    data.close()
