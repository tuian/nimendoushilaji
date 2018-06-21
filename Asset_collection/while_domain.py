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
        self.browser=browser_pool.browser_pool()
    def start(self):
        while True:
            mongodb_cons=mongodb_con.mongodb_con()
            list_url=[i['url'] for i in mongodb_cons.callback_list_url(self.domain,200)]
            self.browser.regulator(list_url)
            data=self.browser.callback_res()
            if data==[]:break
            #data={'url': 'http://o.qq.com', 'current_url': 'http://o.qq.com/mobile/mobile-page.html', 'title': 'QQ International - Fun to Chat', 'html_size': 4945, 'state': 0, 'time': '2018-06-19'}
            #print(data['url'])
            mongodb_cons.callback_update(self.domain, data)
            self.models.while_domain(self.browser)
            self.models.del_tmp()
if __name__=="__main__":
    p=while_domain()
    p.start()
                      
                
        
        