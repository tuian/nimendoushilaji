# coding: utf-8
'''
Created on 2018年5月21日

@author: guimaizi
'''
# coding: utf-8
'''
Created on 2018��4��15��

@author: 63571
'''

#import socket,re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class webbrowser:
    def __init__(self, cookie):
        #浏览器
        chrome_options = Options()
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        chrome_options.add_argument('--hide-scrollbars') 
        #chrome_options.add_argument('permissions.default.stylesheet', 2)
        chrome_options.binary_location = r'C:\Users\63571\AppData\Local\Google\Chrome\Application\chrome.exe'
        # chrome_options.binary_location = '/opt/google/chrome/chrome'
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
    def access(self,url):
        self.driver.get(url)
    def callback_network(self):
        #返回http请求url
        performances = self.driver.execute_script("return window.performance.getEntries()")
        list_net_url=list(set([i['name'] for i in performances]))
        return list_net_url
    def callback_href(self):
        #返回href
        list_url=list(set([i.get_attribute('href') for i in self.driver.find_elements_by_xpath("//a[@href]")]))
        return (list_url)
    def callback_source(self):
        return self.driver.page_source
    def close(self):
        #结束浏览器
        self.driver.quit()
if __name__ == '__main__':
    itme=webbrowser('A')
    for i in ['http://www.qq.com/']:
        print(itme.access(i))
        print(itme.callback_href())
        print(itme.callback_network())
        print(itme.callback_source())
    itme.close()