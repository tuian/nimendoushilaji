# coding: utf-8
'''
Created on 2018��5��22��

@author: guimaizi
'''
from pymongo import MongoClient
import time
class mongodb_con:
    def __init__(self):
        '''
            常用mongodb指令：
            db.qq_com.find({"url":/.*Cookie*./}) 
            db.qq_com.find({"state":"0"}) .limit(10)
            db.qq_com.update({ "state" : {$ne:0}} ,{$set:{"state":0}},false,true)
        '''
        self.client = MongoClient("localhost", 27017)
        self.db_target_domian = self.client.target_domian
        self.db_spider_domian = self.client.spider_domian
    def into_target(self,domain,data):
        try:
            #print data
            domain=domain.replace('.','_')
            collection = self.db_target_domian[domain]
            collection.insert(data,manipulate=True)
        except Exception as e:
            print(e)
    def find(self,domain,url):
        domain=domain.replace('.','_')
        collection = self.db_target_domian[domain]
        return collection.find({"url": "%s"%url}).count()
    def callback_list_url(self,domain,limt):
        domain=domain.replace('.','_')
        collection = self.db_target_domian[domain]
        return collection.find({"state":0}, { "id": 1, "url": 1 }).limit(limt)
    def callback_update(self,domain,list_url):
        domain=domain.replace('.','_')
        collection = self.db_target_domian[domain]
        for data in list_url:
            len_data=collection.find({"url":data['url']}, {"html_size": 1 })[0]['html_size']
            #len_data=collection.find({"url":"http://z.qq.com"}, {"html_size": 1 })[0]['html_size']
            if len_data/data['html_size']>=1.2 or len_data/data['html_size']<=0.8:
                collection.update_one({"url": data['url']},{"$set": {"state": 1,"html_size":data['html_size'],"title":data['title'],"time":time.strftime('%Y-%m-%d',time.localtime())}})
            else:
                collection.update_one({"url": data['url']},{"$set": {"state": 1}})
    def close(self):
        self.client.close()
if '__main__' == __name__:
    p=mongodb_con()
    print(p.find('qq.com','http://v.qq.com')) 