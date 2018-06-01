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
    def into_target(self,domain,data):
        try:
            #print data
            domain=domain.replace('.','_')
            collection = self.db_target_domian[self.domain]
            collection.insert(data,manipulate=True)
        except Exception as e:
            print(e)
    def find(self,domain,url):
        collection = self.db_target_domian[domain]
        return collection.find({"url": "%s"%url}).count()
if '__main__' == __name__:
    p=mongodb_con()
    #p.into_target('qq.com',{'url': 'http://v.qq.com', 'current_url': 'https://v.qq.com/', 'title': '腾讯视频-中国领先的在线视频媒体平台,海量高清视频在线观看', 'html_size': 1394887, 'state': 0, 'time': '2018-06-01'})
    print(p.find('qq.com','http://v.qq.com')) 