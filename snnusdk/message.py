'''
Created on Dec 29, 2018

@author: QiZhao
'''
from snnusdk.configs import SPIDER_CONFIG
from snnusdk.exceptions import DepartmentNotSupportedError
import requests
import re

class Notice(object):
    """
    校园通知

    :param str dep: 部门名称
    :raise: :class:`snnusdk.exceptions.DepartmentNotSupportedError`

    >>> n = Notice(dep='计算机科学学院')
    """

    def __init__(self, dep):
        super().__init__()
        self.dep=dep
        self.data=None
    
    def get_count(self):
        """通知条数
        
        :rtype: int
        :return: 通知的条数

        >>> n.get_count()
        14
        """
        return len(self.data)
    
    def get_notice(self):
        """通知的关键信息(标题,时间,链接)
        
        :raise: :class:`snnusdk.exceptions.DepartmentNotSupportedError`
        :rtype: list of dict
        :return: 参照例子

        >>> n.get_notice()
        [
            {
                'date': '2018-12-26', 
                'link': 'http://tyxy.snnu.edu.cn/News_information.asp?id=33&bh=1593', 
                'title': '【学生工作】学院2017级开展宿舍冬季安全教育工作'
            },
            ...
        ]
        """
        if self.dep not in get_support_dep():
            raise DepartmentNotSupportedError("暂时不支持该部门!")
        dic={}
        for d in SPIDER_CONFIG:
            if (self.dep==d['department_EN'] or self.dep==d['department_CN'])\
             and d['type']=='通知':
                dic=d
                break
        try:
            r=requests.get(dic['url'])
            r.encoding=dic['coding']
            pattern = re.compile(dic['rule'], re.S)
            data_use = []
            it = pattern.finditer(r.text)
            for i in it:
                data_use.append(i.groupdict())
            for item_dict in data_use:
                item_dict['link'] = dic['url_main'] + item_dict['link']
            self.data=data_use
        except ConnectionError:
            raise ConnectionError("网络连接超时!")
            self.data=None
        except Exception:
            raise Exception("未知错误!")
            self.data=None
        return self.data

class News(object):
    """
    校园新闻

    :param str dep: 部门名称
    :raise: :class:`snnusdk.exceptions.DepartmentNotSupportedError`

    >>> n = News(dep='计算机科学学院')
    """

    def __init__(self, dep):
        super().__init__()
        self.dep=dep
        self.data=None
    
    def get_count(self):
        """新闻条数
        
        :rtype: int
        :return: 通知的条数

        >>> n.get_count()
        14
        """
        return len(self.data)
    
    def get_news(self):
        """新闻的关键信息(标题,时间,链接)
        
        :raise: :class:`snnusdk.exceptions.DepartmentNotSupportedError`
        :rtype: list of dict
        :return: 参照例子

        >>> n.get_news()
        [
            {
                'date': '2018-12-26', 
                'link': 'http://tyxy.snnu.edu.cn/News_information.asp?id=33&bh=1593', 
                'title': '【学生工作】学院2017级开展宿舍冬季安全教育工作'
            },
            ...
        ]
        """
        if self.dep not in get_support_dep():
            raise DepartmentNotSupportedError("暂时不支持该部门!")
        dic={}
        for d in SPIDER_CONFIG:
            if (self.dep==d['department_EN'] or self.dep==d['department_CN'])\
             and d['type']=='新闻':
                dic=d
                break
        try:
            r=requests.get(dic['url'])
            r.encoding=dic['coding']
            pattern = re.compile(dic['rule'], re.S)
            data_use = []
            it = pattern.finditer(r.text)
            for i in it:
                data_use.append(i.groupdict())
            for item_dict in data_use:
                item_dict['link'] = dic['url_main'] + item_dict['link']
            self.data=data_use
        except ConnectionError:
            raise ConnectionError("网络连接超时!")
            self.data=None
        except Exception:
            raise Exception("未知错误!")
            self.data=None
        return self.data
    
def get_support_dep():
    """所支持的部门

    :rtype: list
    :return: 所支持部门的名称的列表

    >>> get_support_dep()
    ['生命科学学院', '新闻与传播学院', ...]
    """
    ret=set()
    for dic in SPIDER_CONFIG:
        ret.add(dic['department_CN'])
    return list(ret)

if __name__ == '__main__':
    print(get_support_dep())
    for i in SPIDER_CONFIG:
        a=News(i["department_CN"])
        a.get_news()
        print(a.data[0]) 