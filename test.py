'''
Created on 2018年5月24日

@author: rasca1
'''
import urllib.parse,configparser  
from lib import webbrowser
class test:
    def __init__(self):
        #self.list_browser=[webbrowser.webbrowser() for i in range(5)]
        pass
    def get(self,i):
        print(self.list_browser[0].callback_data(i))
        '''for i in range(5):
            print(i)'''
    def callback_domain(self,url):
        #返回domain
        url=urllib.parse.urlparse(url)
        if url.scheme=='http' or url.scheme=='https':
            return url.scheme+'://'+url.netloc
        else:
            return False
    def read_config(self,itme):
        cf = configparser.ConfigParser()
        cf.readfp(open('config.ini'))    
        return cf.get("config",itme)
if __name__=="__main__":
    p=test()
    str=['http://www.dsada.net/dsadsa.php?dsadas=1&dsada=213','http://www.sada.com/dsada.php']
    #print(p.callback_domain('http://www.sada.com/dsada.php'))
    print(p.read_config('path'))