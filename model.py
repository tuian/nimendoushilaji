# coding: utf-8
'''
Created on 2018年5月23日

@author: guimaizi
'''
import threadpool,queue,urllib.parse,configparser 
class model:
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
    def read_config(self,itme):
        cf = configparser.ConfigParser()
        cf.readfp(open(r'C:\Users\63571\eclipse-workspace\nimendoushilaji\config.ini'))    
        return cf.get("config",itme)