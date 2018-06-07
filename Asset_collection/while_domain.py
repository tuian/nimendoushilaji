# coding: utf-8
'''
Created on 2018年5月30日

@author: guimaizi
'''
import model,re
from lib import mongodb_con
class while_domain:
    def __init__(self,domain,Blacklist_domain):
        self.models=model.model()
        self.domain=domain
        self.Blacklist_domain=Blacklist_domain
        self.mongodb_cons=mongodb_con.mongodb_con()
    def read_tmp_domain(self):
        list_url=[]
        for i in self.models.callback_tmp_list():
            url=self.models.callback_domain(i)
            if url!=False:
                list_url.append(url)      
        list_url=list(set([i for i in list_url if re.search(r'.*\.qq\.com$', i)!=None]))
        list_url=[i for i in list_url if self.models.Blacklist(self.Blacklist_domain, i)!=False]
        list_url=[i for i in list_url if self.mongodb_cons.find(self.domain, i)==0]
        return list_url
if __name__=="__main__":
    p=while_domain('qq.com',['.qzone.qq.com','.gamebbs.qq.com','.ke.qq.com','.house.qq.com','.auto.qq.com','.openwebgame.qq.com','.house.qq.com'])
    print(p.read_tmp_domain())
                      
                
        
        