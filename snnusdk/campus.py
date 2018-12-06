'''
Created on Dec 5, 2018

@author: QiZhao
'''
from snnusdk.tool.Table import table_to_list
from bs4 import BeautifulSoup
import requests

class Campus:
    """校园卡消费明细
    :param str id: 校园卡号

    >>> c = Campus(id='2016xxx')
    """
    url='http://edutech.snnu.edu.cn/ecard/ccc.asp'
    def __init__(self, id):
        self.id=id
        self.data={
            'usernum': id,
            'search': '查询',
            'wx':'' 
        }
    
    def getList(self):
        """
        查询消费明细
        
        :rtype: dict
        :return: 参见例子

        >>> c = getList()
        {
            'success': True, 
            'result': 
            [
                {
                    '卡号': '201608735', 
                    '时间': '2018-12-5 22:48:10', 
                    '次数': '2760', 
                    '原金额': '98.09', 
                    '交易额': '30.70', 
                    '卡余额': '67.39', 
                    '记录信息': '99CB399', 
                    '备注': ''
                }, 
                ...
            ]
        }
        """
        ret={}
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
        """
        :rtype: str
        :return: 校园卡号
        """
        return self.id
        
if __name__ == "__main__":
    a=Campus('201608735')
    print(a.getList())