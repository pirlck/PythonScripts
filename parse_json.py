#-*-coding:utf-8-*-

import json
s = json.loads('{ "name":"test","types": { "name":"seq","para":["1","2"] } }')
print s
print s.keys()
print s["name"]
print s["types"]["name"]
print s["types"]["para"][1]

##½«ÄÚÈÝÐ´³Éjson
file = 'ss.json'
fp = open(file,'w+')
fp.write(json.dumps(s))
fp.close()

#¶Á
file = 'test.json'
fp = open(file, 'r')
dict = json.dump(fp.read())
fp.close()

#Ð´
testDict = {'a':1,'b':2}
file = 'my.json'
fp = open(file,'w+')
fp.write(json.loads(testDict))
fp.close()


