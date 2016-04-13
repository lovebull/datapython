#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Script Name   : hospital.py
# Author        : lovebull
# Created       : 2016/04/12
# Last Modified : 2016/04/12
# Version       : 1.0.0
# Modifications : Added exceptions
#
# Description   :

from urllib import  request
import  time
from bs4 import  BeautifulSoup
import  os
import uuid



# website url
req=request.Request('')

req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
# print(11)
# time.sleep(1)
# print(22)
f=request.urlopen(req)
data=f.read().decode('gbk')

soup = BeautifulSoup(data,'lxml')

html=soup.find("div","serach-left-list")#.find("li")
#htmltwo=html.find_all("li")

#获取医院名称
yy_name=html.find_all("a","yy-name")
i=0
for key in yy_name:
    i=i+1

    print("%d= %s" %(i,key.get_text()))


#def has_class_but_no_id_and_class(tag):
    #return not tag.has_attr('class')
    # and not tag.has_attr('id')
print("-----------------ttttttt-------------------")
def has_noclass_intag_p():
    yy_dizhi=html.find_all("p")
    for keys in yy_dizhi:
         print(keys)
    return keys



#获取地址

address=html.find_all("p","di")
aa=0
for key_address in address:
    kk=key_address.find_all("a")

    for key_add in kk:
        aa=aa+1

        print("%d=%s" %(aa, key_add.get_text()))


print("-----------------ttttttt-------------------")
#获取 三级甲等/ 心血管病医院 / 医保定点
#增加 去除获得文本内容的前后空白strip=True
yy=html.find_all("p","di")
cc=0
for key in yy:
    tt=key.find_previous_siblings("p")
    for keys in tt:
        cc=cc+1
        print("%d=%s" %(cc,keys.get_text(strip=True)))






'''
抓取网页文件内容，保存到内存

@url 欲抓取文件 ，path+filename
'''
def get_file(url):
    try:
        req=request.Request(url)
        operate=request.urlopen(req)
        data=operate.read()
        return data
    except BaseException as e:
        print("BaseException",e)
        return None

'''创建文档'''
def mkdir(path):
    # 去除左右两边的空格
    path=path.strip()
    # 去除尾部 \符号
    path=path.rstrip("\\")

    if not os.path.exists(path):
        os.makedirs(path)

    return path
def save_file(path, file_name, data):
    if data == None:
        return

    mkdir(path)
    if(not path.endswith("/")):
        path=path+"/"
    file=open(path+file_name, "wb")
    file.write(data)
    file.flush()
    file.close()


def unique_str():
    return str(uuid.uuid1())

#获取医院图片地址并且下载到本地
img_url=html.find_all("img","yy-img")
for key_img in img_url:
    url_yyimg=key_img.get('src')
    save_file("E:/Python/datapython/img", unique_str()+".jpg", get_file(url_yyimg))
    print(key_img.get('src'))


#获取分页URL 下一页地址
page_url=html.find('div','next').find("a")
page_url_next="http://yyk.39.net"+page_url.get('href')
print(page_url_next)
