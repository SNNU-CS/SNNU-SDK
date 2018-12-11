'''
Created on Dec 5, 2018

@author: QiZhao
'''

from bs4 import BeautifulSoup
import requests
from requests.exceptions import ReadTimeout, ConnectionError
import re
from snnusdk.exceptions import BuildingNotFoundError, RoomNotFoundError

dic = {
    '崇鋈楼': '0101',
    '积学堂': '0102',
    '学院教室': '0103',
    '雁塔教学八楼': '0104',
    '雁塔教学九楼': '0105',
    '雁塔教学六楼': '0106',
    '雁塔教学四楼': '0107',
    '雁塔教学五楼': '0108',
    '雁塔教学一楼': '0109',
    '雁塔体育场地': '0110',
    '雁塔田家炳楼': '0111',
    '雁塔语音': '0112',
    '逸夫楼': '0113',
    '教学七楼': '0114',
    '长安体育场地': '0201',
    '长安文津楼': '0202',
    '长安文渊楼': '0203',
    '长安语音': '0204',
    '六艺楼': '0205',
    '学院教室': '0206'
}
host = 'http://kb.snnu.edu.cn/room/index/'
re_p = re.compile('<P>([^<]*?)</p>')
week_key = ['', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
jieshu = ['9-10节', '1-2节', '3-4节', '5-6节', '7-8节', ]


class Room:
    """陕师大教室状态查询

    :param int week: 周次
    :param str building: 教学楼
    :raise: :class:`snnusdk.exceptions.BuildingNotFoundError`
    :raise: :class:`snnusdk.exceptions.RoomNotFoundError`

    >>> room = Room(week=14, building='雁塔教学八楼')
    """

    def __init__(self, week, building):
        self.week = week
        self.building = building
        self.soup = self._get_Soup()
        self.Rooms = self._get_Rooms()

    def _get_Soup(self):
        """依据构造参数,获取BeautifulSoup对象对象
        
        :raise: :class:`snnusdk.exceptions.BuildingNotFoundError`
        :raise: :class:`requests.exceptions.ConnectionError`
        :rtype: bs4.BeautifulSoup对象
        :return: 依据构造参数获得的BeautifulSoup对象
        """
        try:
            url = '{}?jxz={}&lh={}'.format(host, self.week, dic[self.building])
            r = requests.get(url, timeout=10)
            soup = BeautifulSoup(r.text, 'lxml')
#             print(type(soup))
        except KeyError:
            raise BuildingNotFoundError('不存在该教学楼！')
        except ReadTimeout:
            raise ConnectionError('网络连接失败')
        return soup

    def _get_Rooms(self):
        """
        :rtype: list of str
        :retuen: 本教学楼内的所有教室名称

        >>> room._getRooms()
        ['8101', '8102', ...]
        """
        ret = []
        trs = self.soup.find(name='tbody').find_all(name='tr')
        for tr in trs:
            tds = tr.find_all(name='td')
            for td in tds:
                if not td.has_attr('align'):
                    ret.append(td.find(name='a')['title'])
                    break
        return ret

    def _get_one_room(self, tr):
        """依据选中的tr标签,获得tr标签所对应的教室一周内的状态

        :param bs4.element.Tag tr:
        :rtype: dict
        :return: 参照例子

        >>> room._get_one_room(tr)
        {
            'id': '8104', 
            '教室类型': '多媒体教室', 
            '上课座位': '60', 
            '星期一': 
            [
                {
                    '状态': '排课', 
                    'info': 
                    {
                        '科目': '高等数学（一）-3', 
                        '教师': '吴洪博', 
                        '班级':'数学与信息科学学院 恒元物理实验班1701', 
                        '时间': '1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18 周1 1-2节', 
                        '地点': '雁塔教学八楼 8104'
                    }
                    '节数':'1-2节'
                },
                ... 
            ]
            ...
        }
        """
        tds = tr.find_all(name='td')
        dic = {}
        flag = 0
        oneday = []
        for td in tds:
            if td.has_attr('align'):
                flag += 1
                one_class = self._get_one_class(td)
                one_class['节数'] = jieshu[int(flag) % 5]
                oneday.append(one_class)
            else:  # 教室整体信息
                dic['id'] = td.find(name='a')['title']
                ls = re.findall(
                    '(\sbody=\[|>\s)([^：]*?)：([^\s]*?)\s', td['title'])
                for tup in ls:
                    dic[tup[1]] = tup[2]
            if int(flag) % 5 == 0 and flag != 0:
                dic[week_key[int(flag / 5)]] = oneday
                oneday = []

        return dic

    def _get_one_class(self, td):
        """依据选中的td标签,获得td标签所对应的某教室某节课的状态

        :param bs4.element.Tag td:
        :rtype: dict
        :return: 参照例子

        >>> room._get_one_class(td)
        {
            '状态': '排课', 
            'info': 
            {
                '科目': '高等数学（一）-3', 
                '教师': '吴洪博', 
                '班级':'数学与信息科学学院 恒元物理实验班1701', 
                '时间': '1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18 周1 1-2节', 
                '地点': '雁塔教学八楼 8104'
            }
            '节数':'1-2节'
        }
        """
        one_class = {}
        div = td.find(name='div')
        status = str(div['class'])[2:-2]
        one_class['状态'] = status
        info_list = re_p.findall(div['onclick'])  # list
        temp_keys = [item.split(':')[0] for item in info_list]
        temp_values = [item.split(':')[1] for item in info_list]
        info_dic = dict(zip(temp_keys, temp_values))
        one_class['info'] = info_dic
        return one_class

    def query_all(self):
        """该教学楼该周所有教室的状态

        :rtype: list of dict
        :return: 参见例子

        >>> room.query_all()
        [
            {
            'id': '8101', 
            '教室类型': '多媒体教室', 
            '上课座位': '60', 
            '星期一': [
                        {
                            '状态': '排课', 
                            '节数':'1-2节'
                            'info':
                            {
                                '科目': '数学分析(一)', 
                                '教师': '曹小红',
                                ...
                            }
                        },
                        ...
                    ]
            },
            ..，
        ]
        """

        trs = self.soup.find(name='tbody').find_all(name='tr')
        ret = []
        for tr in trs:
            ret.append(self._get_one_room(tr))
        return ret

    def get_all_rooms(self):
        """教学楼内的所有教室名称

        :rtype: list of str
        :return: 本教学楼内的所有教室名称

        >>> room.get_all_rooms()
        ['8101', '8102', ...]
        """
        return self.Rooms

    def query_one_room(self, room):
        """
        查询该教学楼某一教室该周的所有状态

        :param str room: 教室号 8014
        :raise: :class:`snnusdk.exceptions.RoomNotFoundError`
        :rtype: dic
        :return: 参照例子

        >>> room.query_one_room(room='8014')
        {
            'id': '8104', 
            '教室类型': '多媒体教室', 
            '上课座位': '60', 
            '星期一': 
            [
                {
                    '状态': '排课', 
                    'info': 
                    {
                        '科目': '高等数学（一）-3', 
                        '教师': '吴洪博', 
                        '班级':'数学与信息科学学院 恒元物理实验班1701', 
                        '时间': '1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18 周1 1-2节', 
                        '地点': '雁塔教学八楼 8104'
                    }
                    '节数':'1-2节'
                },
                ... 
            ]
            ...
        }
        """
        trs = self.soup.find(name='tbody').find_all(name='tr')
        if room not in self.Rooms:
            raise RoomNotFoundError('不存在该教室')
        tr = trs[self.Rooms.index(room)]
#         print(type(tr))
        return self._get_one_room(tr)

if __name__ == '__main__':
    a = Room(12, '雁塔教学八楼')
    print(a.query_one_room('8104'))
#     print(a.QueryAll())
