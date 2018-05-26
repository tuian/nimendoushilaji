# coding: utf-8
'''
Created on 2018年5月21日

@author: guimaizi
'''
#import socket,re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class webbrowser:
    def __init__(self):
        #浏览器
        chrome_options = Options()
        #headless模式运行
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        #不加载图片
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        #调用当前chrome用户数据 cookie登陆方式
        #chrome_options.add_argument(r'user-data-dir=C:\Users\63571\AppData\Local\Google\Chrome\User Data')
        chrome_options.add_argument('--hide-scrollbars') 
        chrome_options.binary_location = r'C:\Users\63571\AppData\Local\Google\Chrome\Application\chrome.exe'
        # chrome_options.binary_location = '/opt/google/chrome/chrome'
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
    def set_cookie(self,url,cookie):
        #js设置cookie
        self.driver.get(url)
        for i in cookie.split(';'):
            self.driver.execute_script("document.cookie = \"%s\"" % i)
    def access(self,url):
        #访问url
        try:
            #print(url)
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            return True
        except Exception as e:
                print(e)
                return False
    def callback_network(self):
        #return 页面的网络请求信息
        performances = self.driver.execute_script("return window.performance.getEntries()")
        list_net_url=list(set([i['name'] for i in performances]))
        return list_net_url
    def callback_href(self):
        #return href
        list_url=list(set([i.get_attribute('href') for i in self.driver.find_elements_by_xpath("//a[@href]")]))
        return (list_url)
    def callback_source(self):
        #return 页面源码
        return self.driver.page_source
    def callback_url(self):
        #return 当前url
        try:
            return self.driver.current_url
        except:
            return None
    def callback_title(self):
        #return html title
        return self.driver.title
    def callback_data(self,url):
        try:
            #print(url)
            self.driver.get(url)
            result = EC.alert_is_present()(self.driver)
            if result:result.dismiss()
            self.driver.implicitly_wait(6)
            self.driver.set_script_timeout(6)
            self.driver.set_page_load_timeout(6)  
            return {'url':self.driver.current_url,'title':self.driver.title,'html_size':len(self.driver.page_source),'state':0,'time':time.strftime('%Y-%m-%d',time.localtime())}
        except Exception as e:
                print(e)
                return False
    def close(self):
        #结束浏览器
        self.driver.quit()
if __name__ == '__main__':
    itme=webbrowser()
    #for i in ['http://l.qq.com', 'http://t.qq.com', 'http://p.qq.com', 'http://b.qq.com', 'http://d.qq.com', 'http://i.qq.com', 'http://o.qq.com', 'http://x.qq.com', 'http://0.qq.com', 'http://4.qq.com', 'http://u.qq.com', 'http://5.qq.com', 'http://q.qq.com', 'http://v.qq.com', 'http://9.qq.com', 'http://c.qq.com', 'http://e.qq.com', 'http://g.qq.com', 'http://s.qq.com', 'http://6.qq.com', 'http://8.qq.com', 'http://a.qq.com', 'http://1.qq.com', 'http://7.qq.com', 'http://h.qq.com', 'http://z.qq.com', 'http://m.qq.com']:
    print(itme.callback_data('http://b.qq.com/'))
        #print(itme.callback_url())
        #print(itme.callback_title())
        #time.sleep(10)
    itme.close()