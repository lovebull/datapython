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
import pymysql
from multiprocessing.dummy import Pool as ThreadPool


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
        picture_name=os.path.basename(url_yyimg)
        save_file("E:/Python/datapython/img", picture_name, get_file(url_yyimg))
        print(key_img.get('src'))
    return picture_name

def GetDownImage_ceshi(url):
    picture_name=os.path.basename(url)
    save_file("E:/Python/datapython/img", picture_name, get_file(url))




#获取分页URL 下一页地址
def GetNextPage(html):
    page_url=html.find('div','next').find("a")
    page_url_next="http://yyk.39.net"+page_url.get('href')
    print(page_url_next)
    return page_url_next


#获取一页 页面所有数据
def GetHtmlForPage(url):

     html=GetHtml(url)
     yy_list=html.find_all("li")
     #picture_name=GetDownImage(html)
     i=0
     for yy_info in yy_list:
         #print(yy_info)
         i=i+1
         yy_name=yy_info.find("a","yy-name").get_text()

         yy_address=yy_info.find("p","di").get_text()

         yy_rank=yy_info.find("p").get_text(strip=True)
         yy_imgurl=yy_info.find("img","yy-img").get("src")


         print(i,'=',yy_name,"=",yy_address,"=",yy_rank)
         print(yy_imgurl)
         picture_names=os.path.basename(yy_imgurl)

         db_connect=pymysql.connect(host="localhost",user="root",passwd="root",database="core",port=3306,charset="utf8")
         cur=db_connect.cursor()
         sql="INSERT INTO oc_cms_hospitaldata(yy_name,yy_address,yy_rank,yy_image,create_time)VALUES(%s,%s,%s,%s,%s) "
         param=(yy_name,yy_address,yy_rank,picture_names,int(time.time()))
         try:
            #cur.execute(sql)
            cur.execute(sql,param)
            print('2=',sql)
            db_connect.commit()
         except:
            db_connect.rollback()

         cur.close()
         db_connect.close()
         GetDownImage_ceshi(yy_imgurl)


if __name__=='__main__':

    db_connect=pymysql.connect(host="localhost",user="root",passwd="root",database="core",port=3306,charset="utf8")
    cur=db_connect.cursor()

    url="http://yyk.39.net/beijing/hospitals/"

    #计算脚本运行时间
    start_time=time.time()

    #获取全部医院数据 分页内容数据
    for key in range(1,3):
        url2=url+'c_p'+str(key)
        print('1=',url2)
        GetHtmlForPage(url2)

        # pool=ThreadPool(4)
        # pool.map()
        # pool.close()
        # pool.join()

        #取得数据添加进数据库
        #sql="""INSERT INTO oc_cms_hospitaldata(yy_name,
        #yy_address,yy_rank,yy_image,create_time)VALUES('北京大学第一医院妇产儿童医院','北京市西城区西安门大街1号','三级甲等/ 儿童医院','1460747908','1460747908')  """
        #sql="INSERT INTO oc_cms_hospitaldata(yy_name,yy_address,yy_rank,yy_image,create_time)VALUES(%s,%s,%s,%s,%s) "
        #param=('1','1','1','1460747908','1460747908')
        #try:
            #cur.execute(sql)
        #    cur.execute(sql,param)

         #   db_connect.commit()
        #except:
        #    db_connect.rollback()



    #cur.close()
    #db_connect.close()
    end_time=time.time()

    print('运行时间=',end_time-start_time)


