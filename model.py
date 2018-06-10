# coding: utf-8
'''
Created on 2018年5月23日

@author: guimaizi
'''
import threadpool,queue,urllib.parse,json,os,re
from lib import mongodb_con
class model:
    def read_config(self):
        #返回配置文件信息
        with open(r"C:\Users\63571\eclipse-workspace\nimendoushilaji\config.json",'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict
    def while_domain(self,fun):
        try:
            while True:
                list_url=self.read_tmp_domain()
                self.del_tmp()
                if list_url==[]:
                    break
                fun.regulator(list_url)
                data=fun.callback_res()
                mongodb_cons=mongodb_con.mongodb_con()
                mongodb_cons.into_target(self.read_config()['target_domain'],data)
                mongodb_cons.close()
                list_url=[] 
        except Exception as e:
            print(e)
    def threadpool_fun(self,fun,lists,num):
        #多线程
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
        for i in open(r"{path}\tmp\href_tmp.txt".format(path=self.read_config()['path'])):
            list_url.append(i.strip())
        for i in open(r"{path}\tmp\network_tmp.txt".format(path=self.read_config()['path'])):
            list_url.append(i.strip())
        return list(set(list_url))
    def del_tmp(self):
        #删除文件，可使用以下两种方法
        for filename in ['href_tmp','network_tmp']:
            path_href=r"{path}\tmp\{filename}.txt".format(path=self.read_config()['path'],filename=filename)
            if os.path.exists(path_href):
                os.remove(path_href)
    def Blacklist(self,domain):
        for j in self.read_config()['Blacklist_domain']:
            if j in domain:
                return False
                break
    def read_tmp_domain(self):
        #读取tmp目录文件 去重返回
        list_url=[]
        for i in self.callback_tmp_list():
            url=self.callback_domain(i)
            if url!=False:
                list_url.append(url)      
        list_url=list(set([i for i in list_url if re.search(r'.*%s$'%self.read_config()['target_domain'], i)!=None]))
        list_url=[i for i in list_url if self.Blacklist(i)!=False]
        mongodb_cons=mongodb_con.mongodb_con()
        list_url=[i for i in list_url if mongodb_cons.find(self.read_config()['target_domain'], i)==0]
        return list_url
            
        