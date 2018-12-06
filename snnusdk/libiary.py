'''
Created on Dec 5, 2018

@author: QiZhao
'''
from snnusdk.base import API
from snnusdk.exceptions import AuthenticationException
from bs4 import BeautifulSoup
from snnusdk.tool.Table import table_to_list
import requests

class Library(API):
    """图书馆

    :param username: 用户名
    :param password: 密码
    :raise: :class:`snnusdk.exceptions.AuthenticationException`

    >>> libiary = Library(username='B11111111', password='xxx')
    """


    class URLs:
        HOST = "http://www.lib.snnu.edu.cn/"
        LOGIN = HOST + 'centerlogin.do'        # 登录
        INFO = HOST + 'action.do?webid=w-l-mylib'   # 信息
        BORROW=HOST+'action.do?webid=w-l-zjts' # 在借书籍
        RESERVATION=HOST+'' #  预约书籍
        CASH=HOST+'action.do?webid=w-l-xjsw'# 现金事务
        LOCK=HOST+'action.do?webid=w-l-gsjsz'# 挂失
        UNLOCK=HOST+'action.do?webid=w-l-jgjsz' # 解挂
        
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.login(self.username,self.password)

    def login(self, username, password):
        data = {
            'userid': username,
            'password': password,
            '提交': '登录',
        }

        res = self.post(url=self.URLs.LOGIN, data=data)
        res.encoding = 'utf-8'
        if '已登录' in res.text:
            self.verify = True
        elif '您输入的帐号或密码有误' in res.text:
            raise AuthenticationException('您输入的帐号或密码有误')
        else:
            raise AuthenticationException('未知错误')

    def getInfo(self):
        """基本信息

        :rtype: dict
        :return: 用户基本信息的字典

        >>> library.getInfo()
        {
            '帐号ID': '2016xxxxx', 
            '姓名': '张三', 
            '昵称': 'xx', 
            '登录次数': '123', 
            '状态': '正常'
        }
        """
        soup = self.get_soup(self.URLs.INFO)
        table = soup.find(name='table',attrs={'class':'dzjbzl'})
        info = {}
        for tr in table.select('tr'):
            tds=tr.select('td')
            key=str(tds[0].text)
            value=str(tds[1].text)
            info[key.rstrip('：')] = value
        for f in soup.find_all(name='font'):
            if f.has_attr('color'):
                info['状态']=f.text
                break
        return info
    
    def getBorrowingBooks(self):
        """在借书籍列表
        
        :return: 在借书籍列表
        :rtype: list of dict
        
        >>> library.getBorrowingBooks()
        [
            {
            '书名': '大学语文', 
            '作者': '张三', 
            '出版社': '中国xx出版社', 
            '分馆': '雁塔外借图书库', 
            '索书号': 'TP311', 
            '条码号': '123456789', 
            '应还日期': '2018-12-11 22:00'
            }, 
            ...  
        ]
        """
        soup=self.get_soup(self.URLs.BORROW)
        book_list=[]
        tables=soup.find_all(name='table',attrs={'class':'borrows'})
        for table in tables:
            book={}
            divs=table.select_one('td').find_all(name='div')
            book['书名']=divs[0].select_one('a').text
            for div in divs[1:]:
                ls=div.text.split('：',maxsplit=2)
                book[ls[0]]=ls[1]
            book_list.append(book)
        return book_list
    
    def getReservationBooks(self):
        """预约书籍列表
        
        :return: 预约书籍列表
        :rtype: list of dict
        
        >>> library.getReservationBooks()
        [
            {
            '书名': '大学语文', 
            '作者': '张三', 
            '出版社': '中国xx出版社', 
            '取书地点': '长安总服务台', 
            '预约开始日期': '2018-12-01', 
            '预约失效日期': '2018-12-11'
            }, 
            ...  
        ]
        """
        book_list=[]
        return book_list
    
    def getCash(self):
        """现金事务
        
        :rtype: dict
        :return: 参见例子
        
        >>> library.getCash()
        {
            '总额':'-2.00',
            '明细':
            [
                {
                    '书名': '大学语文', 
                    '作者': '张三', 
                    '出版社': '中国xx出版社', 
                    '数量': '-2.00', 
                    '原因': '超期', 
                    '状态': 'O'
                },
                ...
            ]
        }
        """
        dic={}
        
        return dic
    def lockLibCard(self):
        """挂失图书证
        
        :rtype: dict
        :return: 挂失借书证的结果
        
        >>> library.lockLibCard()
        {
            'success':True,
            'msg':'挂失借书证成功'
        }
        """
        r = self.get(url=self.URLs.LOCK)
        if '挂失借书证成功' in r.text:
            return {'success':True,'msg':'挂失借书证成功'}
        else:
            return  {'success':False,'msg':'挂失借书证失败'}

    def unLockLibCard(self):
        """解挂图书证
        
        :rtype: dict
        :return: 解挂借书证的结果
        
        >>> library.unLockLibCard()
        {
            'success':True,
            'msg':'解挂借书证成功'
        }
        """
        r = self.get(url=self.URLs.UNLOCK)
        if '解挂借书证成功' in r.text:
            return {'success':True,'msg':'解挂借书证成功'}
        else:
            return  {'success':False,'msg':'解挂借书证失败'}

def getBorrowInfo():
    """预约到馆信息

    :rtype: dict
    :return: 预约到馆信息的字典

    >>> getBorrowInfo()
    {
        'success': True, 
        'result': [
            {
                '预约者': '张三', 
                '书名': 'C语言程序设计', 
                '著者': '李四', 
                '保留结束日期': '2018-12-06', 
                '单册分馆': '长安西密集库', 
                '取书地点': '雁塔总服务台'
            },
            ...
            ]
    }
    """
    url='http://opac.snnu.edu.cn:8991/F?func=file&file_name=hold_shelf'
    ret={}
    try:
        r=requests.get(url)
        r.encoding='utf-8'
        soup=BeautifulSoup(r.text,'lxml')
        table=soup.find(name='table',attrs={'summary':'Script output'})
        ls=table_to_list(table)
        ret['success']=True
        ret['result']=ls
    except Exception as e:
        ret['success']=False
        ret['result']=[]
        raise e
    finally:
        return ret
    
if __name__ == "__main__":
    lib = Library('xx', 'xx')
    print(lib.getInfo())
    print(lib.getBorrowingBooks())