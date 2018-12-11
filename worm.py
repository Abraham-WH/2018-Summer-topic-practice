from bs4 import BeautifulSoup
import requests
import sys
import time 
import random
import re

def get_comment_info(s_name,c_url):
    res = requests.get(c_url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    comment = []

    comment.append(s_name)
    for news in soup.select('.comment_list p'):
        comment.append(news.text) 
    print(comment)
    c = ' '.join(comment)
    fp = open('E:\comment.txt','a',encoding='utf-8')
    fp.write(c)
    fp.write('\n')
    fp.close()
    
    
#抓取软件信息

def get_software_info(url):
    try:
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        #info放某个软件的信息
        info = []
        #软件名字
        for news in soup.select('.detail_line h3'):
            info.append(news.text.strip('933') + '\n')
        #分类，时间，系统，下载量
        for news in soup.select('#detail_line_ul'):
            info.append(news.text.strip('\n'))
        s = ''.join(info)
        info = re.split(r'\n|：',s)

        #下载链接
        for news in soup.select('.detail_down '):
            info.append(news.select('a')[0]['onclick'])
        #评分
        for news in soup.select('#stars_detail'):
            s = str(news)
            s=s.lstrip('<div class="stars center" id="stars_detail" style="background-position:0 -')
            s=s.rstrip('px;"></div>')
            info.append(s)

        #print(info)
        #删除多余信息,文件写入名字，分类，时间，系统，下载量，评分
        index = (0,2,4,6,8,10,18)
        j = 0
        for i in index:
            print(info[i].strip( ))
            fp = open('E:\software_data.txt','a',encoding='utf-8')
            fp.write(info[i]+" ")    
            fp.close()  
            j = j + 1
        print(url)
        info.append(url)
        fp = open('E:\software_data.txt','a',encoding='utf-8')        
        fp.write(info[19]+"\n")    
        fp.close()
        s_name = str(info[0])
        c_url = 'http://www.anzhi.com/post/' + url.strip ('http://www.anzhi.com/pkg')
        get_comment_info(s_name,c_url)
    except IndexError:
        print("a")
    #调用，爬取该软件评论



def get_page_info(sort_url):
    res = requests.get(sort_url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    url = []
    uconst = 'http://www.anzhi.com'
    for n in soup.select('.app_icon'):
        url.append(n.select('a')[0]['href'])

    j = 0
    u1 = uconst + url[0]
    
    #每种每页循环
    while j < len(url) - 1:
    #while j < 3:
    #    j = j + 1
        get_software_info(u1)
        #获取该软件的地址
        u1 = uconst + url[j]
        print(j)


def get_sort_info(cur_url):
    page_url = []
    i = 0
    uconst = 'http://www.anzhi.com'
    now_url = cur_url
    j = 0
    while j < 5:
        j = j + 1
 #   while now_url != uconst:
        res = requests.get(now_url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        #获取当前页所有软件地址
        get_page_info(now_url)
        #下一页地址，循环
        for n in soup.select('.pagebars'):
            page_url.append(n.select('.next')[0]['href'])
        l3 = len(page_url)
        u2 = uconst + page_url[i]
        i = i + 1
        now_url = u2
        time.sleep(random.random()*3)
        #很多网站的反爬虫机制都设置了访问间隔时间，一个IP如果短时间内超过了指定的次数就会进入“冷却CD”，所以可以抓取一个页面休眠一个随机时间

def main():
    res = requests.get('http://www.anzhi.com/widgetcat_1.html')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    sort_url = [ ]
    uconst = 'http://www.anzhi.com'
   
    for n in soup.select('.itemlist'):
        sort_url.append(n.select('a')[0]['href'])
    l2 = len(sort_url)
    all_info = []
    i = 0
    u3 = uconst + sort_url[0]
    #每个种类循环
    while i < len(sort_url) - 1:
        i = i + 1
        get_sort_info(u3)
        #获取每种的首页地址
        u3 = uconst + sort_url[i]


if __name__ == '__main__':
    main()
