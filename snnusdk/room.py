'''
Created on Dec 5, 2018

@author: QiZhao
'''

from bs4 import BeautifulSoup
import requests
import re
from snnusdk.exceptions import BuildingNotFoundException,RoomNotFoundException
dic = {
        '崇鋈楼':'0101',
        '积学堂':'0102',
        '学院教室':'0103',
        '雁塔教学八楼':'0104',
        '雁塔教学九楼':'0105',
        '雁塔教学六楼':'0106',
        '雁塔教学四楼':'0107',
        '雁塔教学五楼':'0108',
        '雁塔教学一楼':'0109',
        '雁塔体育场地':'0110',
        '雁塔田家炳楼':'0111',
        '雁塔语音':'0112',
        '逸夫楼':'0113',
        '教学七楼':'0114',
        '长安体育场地':'0201',
        '长安文津楼':'0202',
        '长安文渊楼':'0203',
        '长安语音':'0204',
        '六艺楼':'0205',
        '学院教室':'0206'
        }
host = 'http://kb.snnu.edu.cn/room/index/'
re_p = re.compile('<P>([^<]*?)</p>')
week_key=['','星期一','星期二','星期三','星期四','星期五','星期六','星期日']

class Room:

    def __init__(self, week, building):
        self.week = week
        self.building = building
        self.soup=self._getSoup()
        self.Rooms=self._getRooms()
        
    def _getSoup(self):
        try:
            url = '{}?jxz={}&lh={}'.format(host, self.week, dic[self.building])
            r = requests.get(url)
            soup=BeautifulSoup(r.text,'lxml')
        except KeyError :
            raise BuildingNotFoundException('不存在该教学楼！')
        except Exception as e:
            raise e
        return soup
       
    def _getRooms(self):
        ret=[]
        trs=self.soup.find(name='tbody').find_all(name='tr')
        for tr in trs:
            tds=tr.find_all(name='td')
            for td in tds:
                if not td.has_attr('align'):
                    ret.append(td.find(name='a')['title'])
                    break
        return ret
    
    def _getOneRoom(self,tr):
        tds=tr.find_all(name='td')
        dic={}
        flag=0
        oneday=[]
        for td in tds:
            if td.has_attr('align'):
                flag+=1
                one_class=self._getOneClass(td)
                oneday.append(one_class)
            else:# 教室整体信息
                dic['id']=td.find(name='a')['title']
                ls=re.findall('(\sbody=\[|>\s)([^：]*?)：([^\s]*?)\s',td['title'])
                for tup in ls:
                    dic[tup[1]]=tup[2]
            if int(flag)%5==0 and flag!=0:
                dic[week_key[int(flag/5)]]=oneday
                oneday=[]
                
        return dic
    
    def _getOneClass(self,td):
        one_class={}
        div=td.find(name='div')
        status=str(div['class'])[2:-2]
        one_class['状态']=status
        info_list=re_p.findall(div['onclick']) # list
        temp_keys=[item.split(':')[0] for item in info_list]
        temp_values=[item.split(':')[1] for item in info_list]
        info_dic=dict(zip(temp_keys,temp_values))
        one_class['info']=info_dic
        return one_class

    def QueryAll(self):
        trs=self.soup.find(name='tbody').find_all(name='tr')
        ret=[]
        for tr in trs:
            ret.append(self._getOneRoom(tr))
        return ret
    
    def GetAllRooms(self):
        return self.Rooms
    
    def QueryOneRoom(self,room):
        trs=self.soup.find(name='tbody').find_all(name='tr')
        if room not in self.Rooms:
            raise RoomNotFoundException('不存在该教室')
        tr=trs[self.Rooms.index(room)]
        return self._getOneRoom(tr)
    
if __name__ == '__main__':
    a=Room(12,'雁塔教学八楼')
    print(a.QueryOneRoom('8104'))

    
