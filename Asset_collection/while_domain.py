# coding: utf-8
'''
Created on 2018年5月30日

@author: guimaizi
'''
import model,re
from lib import mongodb_con,browser_pool
class while_domain:
    def __init__(self):
        self.models=model.model()
        self.domain=self.models.read_config()['target_domain']
        self.Blacklist_domain=self.models.read_config()['Blacklist_domain']
        self.mongodb_cons=mongodb_con.mongodb_con()
    def start(self):
        list_url=[i['url'] for i in self.mongodb_cons.callback_list_url(self.domain,5)]
        print(list_url)
        print(self.mongodb_cons.callback_update(self.domain, 'http://z.qq.com')[0]['html_size'])

if __name__=="__main__":
    p=while_domain()
    p.start()
                      
                
        
        