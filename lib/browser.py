# coding: utf-8
'''
Created on 2018年5月21日

@author: guimaizi
'''
#import socket,re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
        chrome_options.add_argument(r'user-data-dir=C:\Users\63571\AppData\Local\Google\Chrome\User Data')
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
        self.driver.get(url)
        self.driver.implicitly_wait(10)
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
        return self.driver.current_url
    def close(self):
        #结束浏览器
        self.driver.quit()
if __name__ == '__main__':
    itme=webbrowser()
    for i in ['https://www.baidu.com/','http://www.qq.com']:
        itme.access(i)
        print(itme.callback_href())
        print(itme.callback_network())
        #print(itme.callback_source())
        print(itme.callback_url())
        time.sleep(10)
    itme.close()