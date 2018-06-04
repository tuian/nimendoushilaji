'''
Created on 2018年5月24日

@author: rasca1
'''
import urllib.parse,model
from lib import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
models=model.model()
chrome_options = Options()
#headless模式运行
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#不加载图片
chrome_options.add_argument('blink-settings=imagesEnabled=false')
#调用当前chrome用户数据 cookie登陆方式
#chrome_options.add_argument(r'user-data-dir=%s'%models.read_config('chrome_user_data'))
chrome_options.add_argument('--hide-scrollbars') 
chrome_options.binary_location = r'%s'%models.read_config('chrome_path')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.qq.com')
driver.set_page_load_timeout(8) 
print(driver.page_source)
driver.close()