# coding: utf-8
'''
Created on 2018年5月31日

@author: guimaizi
'''
from Asset_collection import EnumSubDomain
from lib import browser_pool,mongodb_con
import model
class start:
    def __init__(self,domain,Blacklist_domain):
        self.domain=domain
        self.Blacklist_domain=Blacklist_domain
        self.models=model.model()
        #self.mongodb_con=mongodb_con.mongodb_con()
        self.browser=browser_pool.browser_pool()
    def start(self):
        self.models.del_tmp()
        EnumSub=EnumSubDomain.EnumSubDomain(self.domain)
        EnumSub.sort_domain(2)
        self.browser.control(EnumSub.callback_domain())
        mongodb_con=mongodb_con.mongodb_con()
        mongodb_con.into_target(self.domain,self.browser.callback_res())
    def while_domain(self):
        try:
            while True:
                list_url=self.models.read_tmp_domain(self.Blacklist_domain, self.domain)
                self.models.del_tmp()
                if list_url==[]:
                    break
                self.browser.control(list_url)
                mongodb_con=mongodb_con.mongodb_con()
                mongodb_con.into_target(self.domain,self.browser.callback_res())
                list_url=[]
        finally:
            self.browser.close_browser()
            
if __name__=="__main__":
    itme=start('qq.com',['.qzone.qq.com','.gamebbs.qq.com','.ke.qq.com','.house.qq.com','.auto.qq.com','.openwebgame.qq.com','.house.qq.com'])
    itme.start()
    itme.while_domain()