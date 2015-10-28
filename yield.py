#!/usr/bin/python
#-*-coding:utf-8-*-



def addlist(alist):
	for i in alist:
		 yield i + 1;
		
alist = [1,2,3,4]

for x in addlist(alist):
	print x
	
[2,3,4,5]


def h():
    print 'To be brave'
    yield 5
h()