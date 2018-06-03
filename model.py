# coding: utf-8
'''
Created on 2018年5月23日

@author: guimaizi
'''
import threadpool,queue,urllib.parse,configparser,os,re
from lib import mongodb_con
class model:
    def __init__(self):
        self.mongodb_con=mongodb_con.mongodb_con()
    def threadpool_fun(self,fun,lists,num):
        #print(1,lists)
        q = queue.Queue()
        for i in lists:
            q.put(i)
        lst = [q.get() for i in range(q.qsize())]
        pool = threadpool.ThreadPool(num)
        requests = threadpool.makeRequests(fun, lst)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        pool.dismissWorkers(num, do_join=True) 
    def callback_domain(self,url):
        #返回domain
        url=urllib.parse.urlparse(url)
        if url.scheme=='http' or url.scheme=='https':
            return url.scheme+'://'+url.netloc
        else:
            return False  
    def callback_tmp_list(self):
        list_url=[]
        for i in open("{path}\\tmp\\href_tmp.txt".format(path=self.read_config('path'))):
            list_url.append(i.strip())
        for i in open("{path}\\tmp\\network_tmp.txt".format(path=self.read_config('path'))):
            list_url.append(i.strip())
        return list(set(list_url))
    def read_config(self,itme):
        #返回配置文件信息
        cf = configparser.ConfigParser()
        cf.readfp(open(r'C:\Users\63571\eclipse-workspace\nimendoushilaji\config.ini'))    
        return cf.get("config",itme)
    def del_tmp(self):
        #删除文件，可使用以下两种方法
        for filename in ['href_tmp','network_tmp']:
            path_href="{path}\\tmp\\{filename}.txt".format(path=self.read_config('path'),filename=filename)
            if os.path.exists(path_href):
                os.remove(path_href)
    def Blacklist(self,Blacklist_domain,domain):
        for j in Blacklist_domain:
            if j in domain:
                return False
    def read_tmp_domain(self,Blacklist_domain,domain):
        list_url=[]
        for i in self.callback_tmp_list():
            url=self.callback_domain(i)
            if url!=False:
                list_url.append(url)      
        list_url=list(set([i for i in list_url if re.search(r'.*\.qq\.com$', i)!=None]))
        list_url=[i for i in list_url if self.Blacklist(self.Blacklist_domain, i)!=False]
        list_url=[i for i in list_url if self.mongodb_con.find(domain, i)==0]
        return list_url
            
        