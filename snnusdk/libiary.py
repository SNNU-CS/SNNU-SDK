'''
Created on Dec 5, 2018

@author: QiZhao
'''
from snnusdk.base import API
from snnusdk.exceptions import AuthenticationError
from bs4 import BeautifulSoup
from snnusdk.tool.Table import table_to_list
import requests
import re


class Library(API):
    """图书馆

    :param str username: 用户名
    :param str password: 密码
    :raise: :class:`snnusdk.exceptions.AuthenticationError`

    >>> libiary = Library(username='B11111111', password='xxx')
    """

    class URLs:
        HOST = "http://www.lib.snnu.edu.cn/"
        LOGIN = HOST + 'centerlogin.do'        # 登录
        INFO = HOST + 'action.do?webid=w-l-mylib'   # 信息
        BORROW = HOST + 'action.do?webid=w-l-zjts'  # 在借书籍
        RESERVATION = HOST + 'action.do?webid=w-l-yyts'  # 预约书籍
        CASH = HOST + 'action.do?webid=w-l-xjsw'  # 现金事务
        LOCK = HOST + 'action.do?webid=w-l-gsjsz'  # 挂失
        UNLOCK = HOST + 'action.do?webid=w-l-jgjsz'  # 解挂

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.login(self.username, self.password)

    def login(self, username, password):
        """登录
        
        :param str username: 学号
        :param str password: 密码
        :raise: :class:`snnusdk.exceptions.AuthenticationError`
        """
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
            raise AuthenticationError('您输入的帐号或密码有误')
        else:
            raise AuthenticationError('未知错误')

    def get_info(self):
        """基本信息
        
        :raise: :class:`snnusdk.exceptions.UnauthorizedError`
        :rtype: dict
        :return: 用户基本信息的字典

        >>> library.get_info()
        {
            '帐号ID': '2016xxxxx', 
            '姓名': '张三', 
            '昵称': 'xx', 
            '登录次数': '123', 
            '状态': '正常'
        }
        """
        if self.verify == False:
            raise UnauthorizedError('您还没有登录!')
        soup = self.get_soup(self.URLs.INFO)
        table = soup.find(name='table', attrs={'class': 'dzjbzl'})
        info = {}
        for tr in table.select('tr'):
            tds = tr.select('td')
            key = str(tds[0].text)
            value = str(tds[1].text)
            info[key.rstrip('：')] = value
        for f in soup.find_all(name='font'):
            if f.has_attr('color'):
                info['状态'] = f.text
                break
        return info

    def get_borrowing_books(self):
        """在借书籍列表
        
        :raise: :class:`snnusdk.exceptions.UnauthorizedError`
        :rtype: list of dict
        :return: 在借书籍列表

        >>> library.get_borrowing_books()
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
        if self.verify == False:
            raise UnauthorizedError('您还没有登录!') 
        soup = self.get_soup(self.URLs.BORROW)
        book_list = []
        tables = soup.find_all(name='table', attrs={'class': 'borrows'})
        for table in tables:
            book = {}
            divs = table.select_one('td').find_all(name='div')
            book['书名'] = divs[0].select_one('a').text
            for div in divs[1:]:
                ls = div.text.split('：', maxsplit=2)
                book[ls[0]] = ls[1]
            book_list.append(book)
        return book_list

    def get_reservation_books(self):
        """预约书籍列表
        
        :raise: :class:`snnusdk.exceptions.UnauthorizedError`
        :rtype: list of dict
        :return: 预约书籍列表

        >>> library.get_reservation_books()
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
        if self.verify == False:
            raise UnauthorizedError('您还没有登录!')
        book_list = []
        soup = self.get_soup(self.URLs.RESERVATION)
        borrow_divs = soup.find_all(name='div', attrs={'class': 'borrows'})
        for borrow_div in borrow_divs:
            temp = {}
            for div in borrow_div.find_all(name='div'):
                class_value = div.get('class')[0]
                if class_value == 'title':
                    temp['书名'] = div.text.split('、', 2)[1]
                elif class_value == 'author':
                    temp['作者'], temp['出版社'] = div.text.split(' -- ')
                elif class_value == 'qsdd':
                    temp['取书地点'] = div.text.split('：')[1]
                elif class_value == 'yyrq':
                    temp['预约开始日期'] = div.text.split('：')[1]
                elif class_value == 'yysxrq':
                    temp['预约失效日期'] = div.text.split('：')[1]
            book_list.append(temp)
        return book_list

    def get_cash(self):
        """现金事务
        
        :raise: :class:`snnusdk.exceptions.UnauthorizedError`
        :rtype: dict
        :return: 参照例子

        >>> library.get_cash()
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
        if self.verify == False:
            raise UnauthorizedError('您还没有登录!')
        dic = {}
        soup = self.get_soup(self.URLs.CASH)
        div = soup.find(name='div', attrs={'id': 'b2_block'})
        dic['总额'] = re.search('总额：([^\n]+)', div.text, re.S).group(1)

        dic['明细'] = []
        borrow_divs = soup.find_all(name='div', attrs={'class': 'borrows'})
        for borrow_div in borrow_divs:
            temp = {}
            flag = False
            for div in borrow_div.find_all(name='div'):
                class_value = div.get('class')[0]
                if class_value == 'title':
                    temp['书名'] = div.text.split('、', 2)[1]
                elif class_value == 'author':
                    temp['作者'], temp['出版社'] = div.text.split(' -- ')
                elif class_value == 'qsdd':
                    temp['数量'] = div.text.split('：')[1]
                elif class_value == 'yyrq':
                    if not flag:
                        temp['原因'] = div.text.split('：')[1]
                        flag = True
                    else:
                        temp['状态'] = div.text.split('：')[1]
            dic['明细'].append(temp)
        return dic

    def lock_lib_card(self):
        """挂失图书证
        
        :raise: :class:`snnusdk.exceptions.UnauthorizedError`
        :rtype: dict
        :return: 挂失借书证的结果

        >>> library.lock_lib_card()
        {
            'success':True,
            'msg':'挂失借书证成功'
        }
        """
        if self.verify == False:
            raise UnauthorizedError('您还没有登录!')
        r = self.get(url=self.URLs.LOCK)
        if '挂失借书证成功' in r.text:
            return {'success': True, 'msg': '挂失借书证成功'}
        else:
            return {'success': False, 'msg': '挂失借书证失败'}

    def unlock_lib_card(self):
        """解挂图书证
        
        :raise: :class:`snnusdk.exceptions.UnauthorizedError`
        :rtype: dict
        :return: 解挂借书证的结果

        >>> library.unlock_lib_card()
        {
            'success':True,
            'msg':'解挂借书证成功'
        }
        """
        if self.verify == False:
            raise UnauthorizedError('您还没有登录!')
        r = self.get(url=self.URLs.UNLOCK)
        if '解挂借书证成功' in r.text:
            return {'success': True, 'msg': '解挂借书证成功'}
        else:
            return {'success': False, 'msg': '解挂借书证失败'}


def get_borrow_info():
    """预约到馆信息

    :rtype: dict
    :return: 预约到馆信息的字典

    >>> get_borrow_info()
    {
        'success': True, 
        'msg': '查询成功',
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
    url = 'http://opac.snnu.edu.cn:8991/F?func=file&file_name=hold_shelf'
    ret = {}
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        table = soup.find(name='table', attrs={'summary': 'Script output'})
        ls = table_to_list(table)
        ret['success'] = True
        ret['result'] = ls
        ret['msg']='查询成功'
    except Exception as e:
        ret['success'] = False
        ret['result'] = []
        ret['msg']=e.message
    finally:
        return ret

if __name__ == "__main__":
    lib = Library('xx', 'xx')
    print(lib.get_reservation_books())
#     print(lib.get_info())
#     print(lib.get_borrowing_books())
