#-*- coding: UTF-8 -*-

import os
import re
import shutil

os.mkdir('F:\NewFloder')

listfile = open("test.txt","r")
str = listfile.readline()
while (str != ''):                  #''为空
    strinfo = re.compile(',')       #
    b = strinfo.sub(';',str)        #利用正则表达式查找','符号
    b = b[:-1]                      #去掉最后一个';'
    str_split = b.split(';')        #以每个';'符号作为分割
    
    print len(str)
    print b
    print len(str_split)
    str = listfile.readline()
    
listfile.close()


#if os.path.exists('test.txt'):     #判断文件是否存在
#    print 'True'


for ImgName  in  str_split:
    #print ImgName+'.jpg'
    #oldfile = 'test.txt'
    ImgName = ImgName+'.jpg'
    
    if os.path.exists(ImgName):     #如果文件存在就CP到新的文件夹中
        shutil.copy2(ImgName, 'F:\NewFloder')      #
    







