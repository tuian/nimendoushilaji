'''
Created on 2018年5月24日

@author: rasca1
'''
import urllib.parse  
class test:
    def __init__(self):
        print(1111)
    def get(self,i):
        print(i)
    def callback_domain(self,url):
        #返回domain
        url=urllib.parse.urlparse(url)
        if url.scheme=='http' or url.scheme=='https':
            return url.scheme+'://'+url.netloc
        else:
            return False
        #print(url.)
if __name__=="__main__":
    p=test()
    str=['http://www.dsada.net/dsadsa.php?dsadas=1&dsada=213','http://www.sada.com/dsada.php']
    print(p.callback_domain('http://www.sada.com/dsada.php'))