# coding: utf-8
'''
Created on 2018年5月24日

@author: guimaizi

'''
import test
from lib import webbrowser
from lib import model
class browser_pool:
    def __init__(self):
        #浏览器池
        self.model=model.model()
        self.list_browser=[webbrowser.webbrowser() for i in range(5)]
    def run(self,text):
        if text['signal']==1:
            self.fun_control(self.list_browser[0], text['url'])
        elif text['signal']==2:
            self.fun_control(self.list_browser[1], text['url'])
        elif text['signal']==3:
            self.fun_control(self.list_browser[2], text['url'])
        elif text['signal']==4:
            self.fun_control(self.list_browser[3], text['url'])
        elif text['signal']==5:
            self.fun_control(self.list_browser[4], text['url'])
    def fun_control(self,fun,text):
        #print(text)
        data=fun.callback_data(text)
        if data!=False:
            print(data)
    def dispatch(self,list):
        try:
            list_text=[]
            j=0
            for i in list:
                j=j+1
                list_text.append({"url":i,"signal":j})
                if j>=5:j=0
            #print(list_text)
            self.model.threadpool_fun(self.run, list_text, 5)
        finally:
            self.close_browser()
    def close_browser(self):
        for browser in self.list_browser:
            browser.close()
if __name__=="__main__":
    p=browser_pool()
    p.dispatch(['http://l.qq.com', 'http://t.qq.com', 'http://p.qq.com', 'http://b.qq.com', 'http://d.qq.com', 'http://i.qq.com', 'http://o.qq.com', 'http://x.qq.com', 'http://0.qq.com', 'http://4.qq.com', 'http://u.qq.com', 'http://5.qq.com', 'http://q.qq.com', 'http://v.qq.com', 'http://9.qq.com', 'http://c.qq.com', 'http://e.qq.com', 'http://g.qq.com', 'http://s.qq.com', 'http://6.qq.com', 'http://8.qq.com', 'http://a.qq.com', 'http://1.qq.com', 'http://7.qq.com', 'http://h.qq.com', 'http://z.qq.com', 'http://m.qq.com'])