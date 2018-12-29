'''
Created on Dec 5, 2018

@author: QiZhao
'''
from snnusdk.tool.Table import table_to_list
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError

class Campus:
    """校园卡相关信息

    :param str id: 校园卡号

    >>> c = Campus(id='2016xxx')
    """
    
    class URLs:
        CONSUMPTION= 'http://edutech.snnu.edu.cn/ecard/ccc.asp'
        PHOTO='http://219.244.185.5:8228/getuserphoto.jsp?userid='

    def __init__(self, id):
        self.id = id
        self.data = {
            'usernum': id,
            'search': '查询',
            'wx': ''
        }

    def get_list(self):
        """查询消费明细

        :rtype: dict
        :return: 参见例子

        >>> c = get_list()
        {
            'success': True, 
            'msg': '查询成功',
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
        ret = {}
        try:
            r = requests.post(self.URLs.CONSUMPTION, data=self.data)
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, 'lxml')
            ls = table_to_list(
                soup.find(name='table', attrs={'class': 'hovertable'}))
            ret['success'] = True
            ret['msg']='查询成功'
            ret['result'] = ls
        except AttributeError:
            ret['success'] = False
            ret['msg']='请核对校园卡号'
            ret['result'] = []
        except ConnectionError:
            ret['success'] = False
            ret['msg']='网络连接失败'
            ret['result'] = []
        except Exception:
            ret['success'] = False
            ret['msg']='未知错误'
            ret['result'] = []
        finally:
            return ret

    def __str__(self):
        """
        :rtype: str
        :return: 校园卡号
        """
        return self.id
    
    def get_photo(self):
        """获取个人照片

        :rtype: dict
        :return: 以二进制流的方式返回照片

        >>> c = get_photo()
        {
            'msg': '获取成功', 
            'success': True,
            'data': b'byte'
        }
        """
        ret = {}
        try:
            r=requests.get(self.URLs.PHOTO+self.id)
            ret['msg']='获取成功'
            ret['success'] = True
            ret['data']=r.content
        except ConnectionError:
            ret['success'] = False
            ret['msg']='网络连接失败'
            ret['result'] = []
        except Exception:
            ret['success'] = False
            ret['msg']='未知错误'
            ret['result'] = None
        finally:
            return ret
        
if __name__ == "__main__":
    a = Campus('201608735')
    print(a.get_photo())
