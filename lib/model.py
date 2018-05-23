# coding: utf-8
'''
Created on 2018��5��23��

@author: guimaizi
'''
import threadpool,queue
class model:
    def threadpool_fun(self,fun,lists,num):
        #print(1,lists)
        q = queue.Queue()
        #map(q.put,lists)
        for i in lists:
            q.put(i)
        lst = [q.get() for i in range(q.qsize())]
        pool = threadpool.ThreadPool(num)
        requests = threadpool.makeRequests(fun, lst)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        pool.dismissWorkers(num, do_join=True)   