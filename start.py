# coding: utf-8
'''
Created on 2018年5月31日

@author: guimaizi
'''
from Asset_collection import EnumSubDomain
from lib import browser_pool,mongodb_con
import model
class start:
    def __init__(self):
        self.models=model.model()
        self.domain=self.models.read_config()['target_domain']
        self.browser=browser_pool.browser_pool()
    def start(self):
        self.models.del_tmp()
        EnumSub=EnumSubDomain.EnumSubDomain(self.domain)
        EnumSub.sort_domain(2)
        self.browser.regulator(EnumSub.callback_domain())
        mongodb_cons=mongodb_con.mongodb_con()
        data=self.browser.callback_res()
        mongodb_cons.into_target(self.domain,data)
        mongodb_cons.close()
        self.models.while_domain(self.browser)            
if __name__=="__main__":
    itme=start()
    itme.start()
    #itme.while_domain()