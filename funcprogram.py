#!/usr/bin/python
#-*-coding:utf-8-*-


#用泛函的方法去理解
#函数line与环境变量a,b构成闭包
def line_conf(a,b):
	def line(x):
		return a*x + b
		
	return line

line1 = line_conf(1,2)
line2 = line_conf(3,4)

print line1(2),line2(3)

#raw_input()


def pre_str(pre=''):
	def decorator(func):
		def NewF(a,b):
			print 'input:'+ pre,a,b
			return func(a,b)
		return NewF

	return decorator


@pre_str('=。=')
def square_sum(a,b):
	return a**2 + b**2
	

@pre_str('&=&')
def square_diff(a,b):
	return a**2 - b**2

print square_diff(5,3)




