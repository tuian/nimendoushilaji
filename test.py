'''
Created on 2018年5月24日

@author: rasca1
'''
import json
with open("config.json",'r') as load_f:
    load_dict = json.load(load_f)
print(load_dict['path'])
'''
import time,model
from lib import mongodb_con
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#mongodb_cons=mongodb_con.mongodb_con()
models=model.model()
list_url=models.read_tmp_domain(['.qzone.qq.com','.gamebbs.qq.com','.ke.qq.com','.house.qq.com','.auto.qq.com','.openwebgame.qq.com','.house.qq.com'], 'qq.com')
print(list_url)
#print(mongodb_cons.find('qq.com', 'http://e.qq.com'))
'''