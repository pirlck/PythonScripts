#coding:utf-8
#对item进行格式化编码


import json
item = {}
item['hello'] = 'world'
line = json.dumps(dict(item))+ "\n"

print line,item









