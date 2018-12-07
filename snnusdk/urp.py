'''
Created on Nov 29, 2018

@author: QiZhao
'''

from snnusdk.base import API
# from snnusdk.tool.GUI import CaptchaGUI
from snnusdk.tool.Table import table_to_list
from snnusdk.exceptions import AuthenticationException
from snnusdk.utils.captcha import UrpCaptcha

class Urp(API):
    """陕师大Urp教务

    :param str account: 学号
    :param str password: 密码
    :raise: :class:`snnusdk.exceptions.AuthenticationException`

    >>> urp = Urp(account='B11111111', password='xxx')
    """

    class URLs:
        HOST = "http://219.244.71.113"

        SELECTED_COURSES = HOST + '/xkAction.do?actionType=6'
        OLD_COURSES = HOST + '/lnkbcxAction.do'  # 历年课表
        CAPTCHA = HOST + '/validateCodeAction.do'  # 教务系统验证码
        LOGIN = HOST + '/loginAction.do'  # 教务系统登录
        GRADE = HOST + '/bxqcjcxAction.do' # 本学期成绩
        ALL_GRADE = HOST + '/gradeLnAllAction.do?type=ln&oper=qbinfo' # 全部及格成绩
        
    def __init__(self, account=None, password=None):
        super(Urp, self).__init__()
        if account and password:
            self.account = account
            self.password = password
            self.login(account, password)

    def getCourses(self):
        """获取本学期的选课情况

        :rtype: list of dict
        :return:  参照例子

        >>> urp.getCourses()
        [
            {
                'id': '1241416', 
                'name': '算法设计与分析', 
                'number': '01', 
                'credits': 3.0, 
                'attributes': '必修', 
                'teacher': '王小明*', 
                'status': '置入', 
                'info': [
                            {
                                'week': '1-18周上', 
                                'day': '2', 
                                'timeOfClass': '1', 
                                'numOfClass': '2', 
                                'campus': '长安校区', 
                                'buildings': '长安文津楼', 
                                'room': '1511'
                            }
                        ]
            }
        ]
        """
        soup = self.get_soup(method='get', url=self.URLs.SELECTED_COURSES)
        tables = soup.findAll("table", attrs={'id' : "user"})
        table = tables[1]
        table_list = table_to_list(table, remove_index_list=[8, 9])  # 0,6虽不用,不可写
        courses = []
        temp_dic = {}
        keys = ['周次', '星期', '节次', '节数', '校区', '教学楼', '教室']
        for dic in table_list:
            dic_len = len(dic)
            if dic_len > 9:
                courses.append({
                                'id': dic['课程号'],
                                'name':dic['课程名'],
                                'number': dic['课序号'],
                                'credits': float(dic['学分']),
                                'attributes': dic['课程属性'],
                                'teacher': dic['教师'],
                                'status': dic['选课状态'],
                                'info': []
                    })
            else:
                dic = dict(zip(keys, [dic[key] for key in dic.keys()]))
            for key in dic.keys():
                if key in keys:
                    temp_dic = {
                            'week':dic['周次'],
                            'day':dic['星期'],
                            'timeOfClass':dic['节次'],
                            'numOfClass':dic['节数'],
                            'campus':dic['校区'],
                            'buildings':dic['教学楼'],
                            'room':dic['教室']
                        }
                    
            courses[-1]['info'].append(temp_dic)
            temp_dic = {}
        return courses
    
    def getOldCourses(self, year, semester):
        """
        获取指定学期的课表

        :param str year: 学年 格式为 "2017-2018"
        :param int semester: 学期 数字1或2
        :rtype: list of dict
        :return: 参照例子

        >>> u.getOldCourses(year='2017-2018', semester=1)
        [
            {
                'id': '1241416', 
                'name': '算法设计与分析', 
                'number': '01', 
                'credits': 3.0, 
                'attributes': '必修', 
                'teacher': '王小明*', 
                'status': '置入', 
                'info': [
                            {
                                'week': '1-18周上', 
                                'day': '2', 
                                'timeOfClass': '1', 
                                'numOfClass': '2', 
                                'campus': '长安校区', 
                                'buildings': '长安文津楼', 
                                'room': '1511'
                            }
                        ]
            }
        ]
        """
        return ""

    def getGrade(self):
        """
        获取本学期的成绩
        
        :rtype: list of dict
        :return: 参照例子

        >>> u.getGrade()
        [
            {
                '课程号': '1243432', 
                '课序号': '01', 
                '课程名': '高级数据结构', 
                '英文课程名': 'Advanced Data Structures', 
                '学分': '2', 
                '课程属性': '任选', 
                '课堂最高分': '', 
                '课堂最低分': '', 
                '课堂平均分': '', 
                '成绩': '', 
                '名次': '', 
                '未通过原因': ''
            },
            ...
        ]

        """
        return ""
    
    def getAllGrades(self,year,semester): 
        """获取指定学期的已及格成绩

        :param str year: 学年 格式为 "2017-2018"
        :param int semester: 学期 数字1或2
        :rtype: list
        :return: 参照例子

        >>> u.getAllGrades(year='2017-2018', semester=1)
        [
            {
                '课程号':'01111',
                '课序号': '62', 
                '课程名': '大学外语（一）', 
                '英文课程名': 'College English 1', 
                '学分': '3', 
                '课程属性': 
                '必修', 
                '成绩': '73.0'
            },
            ...
        ]
        """
        return ""
    
    def getGpa(self):
        """计算绩点
        
        :rtype: double
        :return: 只计算必修课的绩点

        >>> u.getGpa()
        73.00
        """
    def login(self, account, password):
        """
        :param str account: 学号
        :param str password: 密码
        :raise: :class:`snnusdk.exceptions.AuthenticationException`
        """
        # FIXME: 登录不可靠
        image = self.get_image(self.URLs.CAPTCHA)
#         captcha_code = CaptchaGUI(image)
        captcha_code=UrpCaptcha(image)
        data = {
            "zjh1":"" ,
            "tips":"",
            "lx": "",
            "evalue": "",
            "eflag":"",
            "fs":"",
            "dzslh":"",
            "zjh": account,
            "mm": password,
            "v_yzm": captcha_code
        }
        result = self._login_execute(url=self.URLs.LOGIN, data=data)
        if result['code'] == 2:
            # 如果验证码错误，尝试递归重复登录
            return self.login(account, password)
        result['success'] = not result['code']
#         print(result)
        if result['success']:
            self.verify = True
        else:
            raise AuthenticationException(result['msg'])
        return result

    def _login_execute(self, url=None, data=None):
        r = self.post(url=url, data=data)
        # print(r.text)
        if r.ok:
            if "学分制综合教务" in r.text:
                self.account = data['zjh']
                self.verify = True  # 登陆成功, 修改状态  (后期还可能继续修改)
                return {'code': 0, 'msg': '登录成功'}
            elif "你输入的验证码错误" in r.text:
                return {'code': 2, 'msg': '验证码不正确！！！'}
            elif "alert.gif" in r.text:
                return {'code': 1, 'msg': '密码错误！！'}
            else:
                return {'code': 3, 'msg': '未知错误'}
        else:
            return {'code': 1, "msg": "登录失败"}


if __name__ == '__main__':
    c = Urp("xx", "xx")
    print(c.getCourses())
    
    
