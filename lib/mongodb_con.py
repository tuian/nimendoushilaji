# coding: utf-8
'''
Created on 2018��5��22��

@author: guimaizi
'''
from pymongo import MongoClient
class mongodb_con:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db_target_domian = self.client.target_domian
        self.db_spider_domian = self.client.spider_domian
    def into(self,domain,data):
        try:
            #print data
            domain=domain.replace('.','_')
            collection = self.db[domain]
            collection.insert(data,manipulate=True)
        except Exception as e:
            print(e)
    def find(self,url):
        collection = self.db[self.domain]
        return collection.find({"url": "%s"%url}).count()
if '__main__' == __name__:
    p=mongodb_con('www.qq.com')
    p.into({'a':'b'})