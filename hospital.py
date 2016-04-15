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



#生产出html
def GetHtml(url):
    req = request.Request(url)
    req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')

    f = request.urlopen(req)
    data = f.read().decode('gbk')

    soup = BeautifulSoup(data, 'lxml')

    html = soup.find("div", "serach-left-list")
    return html



#获取医院名称
def GetHospitalName(html):
    yy_name=html.find_all("a","yy-name")
    #i=0
    #print(yy_name)
    nameList=[]
    for key in yy_name:
        #i=i+1
        #print("医院名称=",key.get_text())
        nameList.append(key.get_text())
    return nameList
    #return key.get_text()


        #print("%d= %s" %(i,key.get_text()))



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
def GetHospitalAddress(html):
    address=html.find_all("p","di")

    addressList=[]
    for key_address in address:
        kk=key_address.find_all("a")
        for key_add in kk:
            #print("医院地址=",key_add.get_text())
            addressList.append(key_add.get_text())
            #print("%d=%s" %(aa, key_add.get_text()))
    return addressList
    #return key_add.get_text()



print("-----------------ttttttt-------------------")
#获取 三级甲等/ 心血管病医院 / 医保定点
#增加 去除获得文本内容的前后空白strip=True

def GetHospitalRank(html):
    yy=html.find_all("p","di")
    rankList=[]
    for key in yy:
        tt=key.find_previous_siblings("p")
        for keys in tt:
            #print("医院等级=",keys.get_text(strip=True))
            rankList.append(keys.get_text(strip=True))
            #cc=cc+1
            #print("%d=%s" %(cc,keys.get_text(strip=True)))
    return rankList
    #return keys.get_text(strip=True)




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
def GetDownImage(html):
    img_url=html.find_all("img","yy-img")
    for key_img in img_url:
        url_yyimg=key_img.get('src')
        save_file("E:/Python/datapython/img", unique_str()+".jpg", get_file(url_yyimg))
        print(key_img.get('src'))



#获取分页URL 下一页地址
def GetNextPage(html):
    page_url=html.find('div','next').find("a")
    page_url_next="http://yyk.39.net"+page_url.get('href')
    print(page_url_next)
    return page_url_next




url=""
# html=GetHtml(url)
# yy_name=GetHospitalName(html)
# yy_address=GetHospitalAddress(html)
# yy_rank=GetHospitalRank(html)
# print(yy_name)
# print(yy_address)
# print(yy_rank)



#print(yy_name,"=",yy_address,"=",yy_rank)

#计算脚本运行时间
start_time=time.time()

#获取全部医院数据 分页内容数据
for key in range(1,3):
    url2=url+'c_p'+str(key)

    print(url2)
    html=GetHtml(url2)

    yy_name=GetHospitalName(html)
    yy_address=GetHospitalAddress(html)
    yy_rank=GetHospitalRank(html)
    GetDownImage(html)
    print(yy_name)
    print(yy_address)
    print(yy_rank)


end_time=time.time()

print('运行时间=',end_time-start_time)


