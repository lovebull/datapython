#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Script Name   : sock5.py
# Author        : lovebull
# Created       : 2016/05/10
# Last Modified : 2016/05/10
# Version       : 1.0.0
# Modifications : Added exceptions
#
# Description   :

from urllib import  request
import  time
from bs4 import  BeautifulSoup
import  os,sys
import uuid
import pymysql
from multiprocessing.dummy import Pool as ThreadPool



#获取脚本文件的当前路径
def cur_file_dir():
    #获取脚本路径
    path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


url=''
req = request.Request(url)
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
f = request.urlopen(req)
data = f.read()#.decode('gbk')
f.close()
soup = BeautifulSoup(data, 'lxml')
html=soup.find(id="free").find(class_="container")

sockcontent=html.find(class_='row').find_next(class_='row')

allip=sockcontent.find_all('div')

f_text=""
sockinfo=[]
for info in allip:
    #服务器地址
    allinfo=info.find_all('h4')
    allinfo.pop() #要删除末尾的元素

    print(allinfo)
    hostip=allinfo[0].get_text()
    hostport=allinfo[1].get_text()
    hostpassword=allinfo[2].get_text()
    hostpass=allinfo[3].get_text()
    hoststatus=allinfo[4].get_text()

    for i in range(1):
         file_object = open(cur_file_dir()+'\\'+"sock5代理服务器.txt",'w+')
         f_text+="{0}\n{1}\n{2}\n{3}\n{4}\n\n".format(hostip,hostport,hostpassword,hostpass,hoststatus)
         file_object.writelines(f_text)
         file_object.write('\n')
         file_object.close()
         #print(i.get_text())

    #for  i in allinfo:

          #file_object = open(cur_file_dir()+'\\'+"haha.txt",'w+')
          #f_text=i.get_text()
         # file_object.writelines(f_text)
          #file_object.write('\n')
          #file_object.close()
          #print(i.get_text())


    print('<br/>')





