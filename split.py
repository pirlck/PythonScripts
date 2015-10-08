#-*- coding: UTF-8 -*-




#按某个字符来分离字符串
str = 'www.google.com'
print str
str_split = str.split('.')
print str_split


#去掉最后一个字符
str2 = 'hh,query is not the one;'
str2 = str2[:-1]
print str2


#替换字符串中的特定字符

a = 'hh,python is useful!'
#2用正则表达式来完成替换:
import re
strinfo = re.compile(',')
b = strinfo.sub(';',a)
print b
#输出的结果也是hello python


#1注意使用 .replace()函数获得是右值；
#本身字符串并不会改变
a1 = "hello word";
a2 = a1.replace("word","python");
#print a1.replace("word","python")
print a2
str4 = "this is string example....wow!!! this is really string";
print str4.replace("is", "was");

