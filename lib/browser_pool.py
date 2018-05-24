# coding: utf-8
'''
Created on 2018��5��24��

@author: guimaizi

'''
import test
from lib import model
class browser_pool:
    def __init__(self):
        #浏览器池
        self.model=model.model()
        self.obj1=test.test()
        self.obj2=test.test()
        self.obj2=test.test()
        self.obj3=test.test()
        self.obj4=test.test()
        self.obj5=test.test()
    def run(self,text):
        #print(text)
        if text['signal']==1:
            self.obj1.get(text['url'])
        elif text['signal']==2:
            self.obj2.get(text['url'])
        elif text['signal']==3:
            self.obj3.get(text['url'])
        elif text['signal']==4:
            self.obj4.get(text['url'])
        elif text['signal']==5:
            self.obj5.get(text['url'])
    def dispatch(self,list):
        list_text=[]
        j=0
        for i in list:
            j=j+1
            list_text.append({"url":i,"signal":j})
            if j>=5:
                j=0
        #print(list_text)
        self.model.threadpool_fun(self.run, list_text, 5)
        
if __name__=="__main__":
    p=browser_pool()
    p.dispatch(['e.qq.com', '5.qq.com', 'i.qq.com', 'd.qq.com', '0.qq.com', 'l.qq.com', 'p.qq.com', 'r.qq.com', 'n.qq.com', '1.qq.com', '4.qq.com', 'z.qq.com', 'x.qq.com', 'q.qq.com', 'u.qq.com', 'k.qq.com', 'h.qq.com', 'f.qq.com', '7.qq.com', '3.qq.com', 'j.qq.com', 'y.qq.com', 'g.qq.com', 'v.qq.com', 'c.qq.com', '6.qq.com', 'a.qq.com', '9.qq.com', 'o.qq.com', 'w.qq.com', '8.qq.com', 't.qq.com', 'm.qq.com', 's.qq.com', 'b.qq.com', '17.qq.com', '12.qq.com', '15.qq.com', '18.qq.com', '22.qq.com', '21.qq.com', '24.qq.com', '3d.qq.com', '3g.qq.com', '3q.qq.com'])