#coding:utf-8

import pymongo
from pymongo import Connection

connection = Connection('localhost',27017)
db = connection.mydb
collection = db.mycollection

db.add_user('test', 'test') # add a user
db.authenticate('test', 'test') # check auth

muser = db.user
muser.save( {'id':1, 'name':'test'} )
muser.find_one()

muser.insert({'id':2,'name':'cl_k'})
muser.find_one()

muser.find_one({'id':2}) # find a record by query
 
muser.create_index('id')

muser.find().sort('id', pymongo.ASCENDING) # DESCENDING

# muser.drop() delete table
muser.find({'id':1}).count() # get records number

muser.find({'id':1}).limit(3).skip(2) # start index is 2 limit 3 records

muser.remove({'id':1}) # delet records where id = 1
muser.update({'id':2}, {'$set':{'name':'haha'}}) # update one recor






