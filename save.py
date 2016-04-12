#
# http://www.cnblogs.com/linjiqin/p/3672285.html

import  os
import uuid
from urllib import request
'''創建文件目录，并返回该目录'''

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

'''获取文件后缀名'''
def get_file_extension(file):
    return os.path.splitext(file)[1]


'''自动生成一个唯一的字符串，固定长度为36'''
def unique_str():
    return str(uuid.uuid1())




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
        print(e)
        return None

#創建文件目录，并返回该目录
#print(mkdir("E:/Python/datapython/111"))
#获取文件后缀名
#print(get_file_extension("123.jpg"))

#自动生成一个唯一的字符串，固定长度为36
print(unique_str())

url="http://qlogo1.store.qq.com/qzone/416501600/416501600/100?0"
#save_file("E:/Python/datapython/111", "123.jpg", get_file(url))
save_file("E:/Python/datapython/111", unique_str()+".jpg", get_file(url))
