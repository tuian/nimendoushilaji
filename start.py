# coding: utf-8
'''
Created on 2018年5月31日

@author: guimaizi
'''
from Asset_collection import EnumSubDomain
from lib import browser_pool
import model
class start:
    def __init__(self,domain):
        self.domain=domain
        self.models=model.model()
    def start(self):
        self.models.del_tmp()
        EnumSub=EnumSubDomain.EnumSubDomain(self.domain)
        EnumSub.sort_domain(2)
        browser=browser_pool.browser_pool()
        browser.control(EnumSub.callback_domain())
        print(browser.callback_res())
if __name__=="__main__":
    itme=start('qq.com')
    itme.start()