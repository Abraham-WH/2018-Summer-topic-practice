from bs4 import BeautifulSoup
import requests
import sys
import time 
import random
import re

#抓取软件信息
'''
def get_comment_info(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    comment = []

    for news in soup.select('.comment_list p'):
        comment.append(news.text) 
    print(comment)
    c = ' '.join(comment)
    fp = open('E:\111.txt','a')
    fp.write(c)
    fp.close()
'''

def get_url(u):
    res = requests.get(u)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    comment = []

    for news in soup.select('.comment_div'):
        print(news)
        #comment.append(news.select('a')['href'])
    #print(comment)



def main():
    get_url("http://www.anzhi.com/pkg/4e03_com.mymoney.html")

if __name__ == '__main__':
    main()
