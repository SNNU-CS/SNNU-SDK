'''
Created on Dec 5, 2018

@author: QiZhao
'''
from snnusdk.tool.Table import table_to_list
from bs4 import BeautifulSoup
import requests
class Campus:

    url='http://edutech.snnu.edu.cn/ecard/ccc.asp'
    def __init__(self, id):
        self.id=id
        self.data={
            'usernum': id,
            'search': '查询',
            'wx':'' 
        }
    
    def getList(self):
        ret=[]
        try:
            r=requests.post(self.url,data=self.data)
            r.encoding='utf-8'
            soup=BeautifulSoup(r.text,'lxml')
            ls=table_to_list(soup.find(name='table',attrs={'class':'hovertable'}))
            ret['success']=True
            ret['result']=ls
        except Exception as e:
            ret['success']=False
            ret['result']=[]
            raise e
        finally:
            return ret
        
    def __str__(self):
        return self.id
        
if __name__ == "__main__":
    a=Campus('201608735')
    print(a)