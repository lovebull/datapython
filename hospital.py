#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from urllib import  request
#from io import  StringIO
#import  gzip
import  time
from bs4 import  BeautifulSoup


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

yy_name=html.find_all("a","yy-name")
i=0
for key in yy_name:
    i=i+1

    print("%d= %s" %(i,key))


#def has_class_but_no_id_and_class(tag):
    #return not tag.has_attr('class')
    # and not tag.has_attr('id')
print("dddddddddd")
def has_noclass_intag_p():
    yy_dizhi=html.find_all("p")
    for keys in yy_dizhi:
         print(keys)
    return keys



#获取 三级甲等/ 心血管病医院 / 医保定点
yy=html.find_all("p","di")
for key in yy:
    tt=key.find_previous_siblings("p")
    for keys in tt:
        print(keys.get_text())















#print( f.read().decode('gbk').encode('utf-8').decode('utf-8'))

# if f.info().get('Content-Encoding') == 'gzip':
#     buf = StringIO(f.read().decode('utf-8'))
#     f = gzip.GzipFile(fileobj=buf)
#     data = f.read()



