#coding:utf-8

'''
this is a pymongo test !
很混乱的测试代码
By CL-K 2015.10.26
'''


import pymongo
import datetime
import random

conn = pymongo.Connection('127.0.0.1',27017)

db = conn.study
print 'all collections:',db.collection_names()

posts = db.post
print posts

new_post ={"AccountID":22,"UserName":"libing",'date':datetime.datetime.now()}
new_posts = [{"AccountID":22,"UserName":"liuw",'date':datetime.datetime.now()},
             {"AccountID":23,"UserName":"urling",'date':datetime.datetime.now()}]

posts.insert(new_post)
print posts.find_one({"AccountID":22,"UserName":"libing"} )

#posts.remove({"AccountID":22,"UserName":"libing"})
#posts.update({"UserName":"urling"},{"$set":{'AccountID':random.randint(20,50)}})

print 'all isues:',posts.count(),posts.find().count()
print 'single issue:',posts.find_one()
print posts.find_one({"UserName":"liuw"})

print 'all issues'

for item in posts.find().sort([("UserName",pymongo.ASCENDING),('date',pymongo.DESCENDING)]):#查询结果根据多列排序
    print item


print posts.find().sort([("UserName",pymongo.ASCENDING),('date',pymongo.DESCENDING)]).explain()["cursor"]#未加索引用BasicCursor查询记录
print posts.find().sort([("UserName",pymongo.ASCENDING),('date',pymongo.DESCENDING)]).explain()["nscanned"]


























raw_input()



