# coding: utf-8
'''
Created on 2018年5月30日

@author: guimaizi
'''
import model,re
class while_domain:
    def __init__(self,domain):
        self.models=model.model()
        self.domain=domain
    def read_tmp(self):
        list_url=[]
        for i in self.models.callback_tmp_list():
            url=self.models.callback_domain(i)
            if url!=False:
                list_url.append(url)
        list_url=(list(set(list_url)))
        return([i for i in list_url if re.search(r'.*\.qq\.com$', i)!=None])
if __name__=="__main__":
    p=while_domain('qq.com')
    p.read_tmp()
                      
                
        
        