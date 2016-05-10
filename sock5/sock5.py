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
import  os,sys,shutil
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

def get_html(url):
    req = request.Request(url)
    req.add_header('User-Agent',
               #'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
    #req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.5 Safari/536.11')
    f = request.urlopen(req)
    data = f.read()#.decode('gbk')
    f.close()
    soup = BeautifulSoup(data, 'lxml')
    html=soup.find(id="free").find(class_="container")

    sockcontent=html.find(class_='row').find_next(class_='row')

    allip=sockcontent.find_all('div')
    return allip

#取得文本txt中的密码
def is_text_update():
    shutil.copy(cur_file_dir()+'\\'+"sock5代理服务器.txt",cur_file_dir()+'\\'+"sock5代理服务器copy.txt")
    content=[]
    try:

        file_text=open(cur_file_dir()+'\\'+"sock5代理服务器copy.txt",'r')
        content=file_text.readlines()
        file_text.close()
        one="".join(list(filter(str.isdigit, content[2])))
        two="".join(filter(str.isdigit, content[8]))
        three="".join(filter(str.isdigit, content[14]))
        content=[one,two,three]
        #return content
        #return one
        return content
    except Exception as e:
        print("出错了：",e)



#取得目标网站代理密码组合成list
def is_html_update(htmldata):
    passlist=[]
    for info in htmldata:
    #服务器地址
        allinfo=info.find_all('h4')
        allinfo.pop() #删除末尾不需要的元素
        #print(allinfo)


        passlist.append("".join(list(filter(str.isdigit,allinfo[2].get_text()))))
    return passlist


        #取得A密码 纯数字形式






def save_data_text(url):
    htmldata=get_html(url)
    f_text=""
    #sockpassword=[]
    html_update=is_html_update(htmldata)
    text_update=is_text_update()
    for info in htmldata:
    #服务器地址
        allinfo=info.find_all('h4')
        allinfo.pop() #删除末尾不需要的元素
        #print(allinfo)
        hostip=allinfo[0].get_text()
        hostport=allinfo[1].get_text()
        hostpassword=allinfo[2].get_text()
        hostpass=allinfo[3].get_text()
        hoststatus=allinfo[4].get_text()

        #取得A密码 纯数字形式
        #sockpassword.append("".join(list(filter(str.isdigit,hostpassword))))
        #print(sockpassword)


        #print(hostpassword)

        if not(text_update[0]==html_update[0]) and not(text_update[1]==html_update[1] and not(text_update[2]==html_update[2])):

                file_object = open(cur_file_dir()+'\\'+"sock5代理服务器.txt",'w+')
                f_text+="{0}\n{1}\n{2}\n{3}\n{4}\n\n".format(hostip,hostport,hostpassword,hostpass,hoststatus)
                file_object.writelines(f_text)
                file_object.write('\n')
                file_object.close()
        else :
                print("目标网站暂时没有更新")




        """
        for i in range(1):

            print(sockpassword)
            print(is_text_update()[1])

            if not(is_text_update()[0]==sockpassword[0]) and not(is_text_update()[1]==sockpassword[1] and not(is_text_update()[2]==sockpassword[2])):

                file_object = open(cur_file_dir()+'\\'+"sock5代理服务器t.txt",'w+')
                f_text+="{0}\n{1}\n{2}\n{3}\n{4}\n\n".format(hostip,hostport,hostpassword,hostpass,hoststatus)
                file_object.writelines(f_text)
                file_object.write('\n')
                file_object.close()
            else :
                print("目标网站暂时没有更新")
           """






if __name__=='__main__':
   url=''

   print("采集开始...........")

   save_data_text(url)
   
   #print(is_text_update()[2])
   #print(is_html_update(url))
   print("采集成功..............")
   time.sleep(5)
   os.remove(cur_file_dir()+'\\'+"sock5代理服务器copy.txt")

 
 



