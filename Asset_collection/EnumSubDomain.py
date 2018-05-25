# coding: utf-8
'''
Created on 2018��5��23��

@author: guimaizi
'''
import dns.resolver
from itertools import product
from lib import model
class EnumSubDomain:
    def __init__(self,domain):
        self.domain=domain
        self.model=model.model()
        self.domain_list=[]
    def sort_domain(self):
        for i in range(1, 3):
            list_str = []
            l = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', \
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', \
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', \
                 'y', 'z']
            for j in list(product(l, repeat=i)):
                list_str.append("".join(j)+ '.'+self.domain)
            self.model.threadpool_fun(self.query,list_str,200)
    def query(self,domain):
        try:
            A = dns.resolver.query(domain, 'A') 
            print(domain)
            self.domain_list.append('http://'+domain)
        except:
            pass
    def callback_domain(self):
        return self.domain_list
if __name__=="__main__":
    p=EnumSubDomain('qq.com')
    p.sort_domain()
    print(p.callback_domain())