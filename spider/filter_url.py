# coding: utf-8
'''
Created on 2018年7月1日

@author: guimaizi
'''
import urllib.parse
class filter_url:
    def __init__(self):
        self.list_url_static=[]
    def filter_url(self,url):
        url=urllib.parse.urlparse(url)
        if url.query!='':
            print(self.params_filter(url))
        elif url.query=='':
            print(self.static_filter(url))
        elif url.path=='':
            print(url)
    def static_filter(self,url):
        print()
    def params_filter(self,url):
        liststr = []
        try:
            liststr = []
            for i in url.query.split('&'):
                para = i.split('=')
                length_int = len(para[1])
                if self.judgetype(para[1]) == 'int':
                    para[1] = '{int:%s}' % length_int
                else:
                    para[1] = '{str:%s}' % length_int
                para = '='.join(para)
                liststr.append(para)
            url_paras='&'.join(liststr)
            return url.scheme + '://' + url.netloc + url.path + '?' + url_paras
        except:
            length_int = len(url.query)
            url_paras = '{'+self.judgetype(url.query) + ':%s}' % length_int 
            return url.scheme + '://' + url.netloc + url.path + '?' + url_paras
    def judgetype(self, strs):
        try:
            int(strs)
            return 'int'
        except:
            return 'str'
if __name__ == '__main__':
    urlss = ['http://www.mianxian.gov.cn/zxft/20483.htm?dsdsa','http://www.mianxian.gov.cn/zxft.php',\
             'http://www.mianxian.gov.cn/zxft/20483.htm','http://www.mianxian.gov.cn/zxft/20483.htm?dsdsa=dsadsa&dada=1',\
             'http://www.mianxian.gov.cn/zxft/31231.htm','http://www.mianxian.gov.cn/zxft/31231',\
             'http://www.mianxian.gov.cn/','http://www.mianxian.gov.cn/zxft/20483.htm?dsdsa=ds1adsa&dada=231231']
    p = filter_url()
    for i in urlss:
        p.filter_url(i)