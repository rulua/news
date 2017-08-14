#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-10 下午3:05
# @Author  : ai-i-luru@interns.chuangxin.com

from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db= client.news
news = db.newstable

def getnews(count):
    result=news.find({},{"_id":0,"title":1}).limit(count)
    #for item in result:
        #print(item)
    return result
#getnews(10)

def newByTitle(title):
    result=news.find_one({"title":title},{"title": 1, "id": 1,"content":1,"pubDate":1,"url":1})
    #print result
    return result

#newByTitle("test")
def api_getnews(count):
    result=news.find({},{"_id":0}).limit(count)
    return result
print api_getnews(10)