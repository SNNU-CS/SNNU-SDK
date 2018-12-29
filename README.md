[![Build Status](https://travis-ci.com/ZhaoQi99/SNNU-SDK.svg?branch=dev)](https://travis-ci.com/ZhaoQi99/SNNU-SDK)
[![image](https://img.shields.io/pypi/v/snnusdk.svg)](https://pypi.org/project/snnusdk/)
[![Release](https://img.shields.io/github/release/ZhaoQi99/SNNU-SDK.svg)](https://github.com/ZhaoQi99/SNNU-SDK/releases)
[![image](https://img.shields.io/pypi/pyversions/snnusdk.svg)](https://pypi.org/project/snnusdk/)
[![Documentation Status](https://readthedocs.org/projects/snnu-sdk/badge/?version=dev)](https://snnu-sdk.readthedocs.io/zh_CN/dev/?badge=dev)
[![GitHub license](https://img.shields.io/github/license/ZhaoQi99/SNNU-SDK.svg)](https://github.com/ZhaoQi99/SNNU-SDK/blob/dev/LICENSE)


# 陕西师范大学(SNNU) 第三方Python SDK
---
SNNU-SDK 是陕西师范大学(SNNU)的一个第三方Python-SDK，实现了校内常用服务如教务处、图书馆、校园卡、教室查询等接口的Python封装。

## 功能
### Urp教务系统
- 本学期课表
- 历年课表
- 本学期成绩
- 历年考试成绩
- 必修课绩点

### 图书馆
- 基本信息
- 在借书籍
- 预约书籍
- 现金事务
- 挂失、解挂图书证
- 预约到馆信息

### 教室
- 某教学楼的所有教室号
- 某教学楼某周的所有教室的状态
- 某教学楼某周某一教室的状态

### 校园卡
- 校园卡消费明细
- 校园卡余额
- 校园卡照片

### 通知新闻
- 某部门的最新通知
- 某部门的最新新闻
- 所支持的部门

## 安装

```bash
pip install snnusdk
✨🍰✨

```
## 使用示例
这里是一些简单的使用案例
```Python
from snnusdk import Urp
urp = Urp(account='B11111111', password='xxx')

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

from snnusdk import Libiary
libiary = Library(username='B11111111', password='xxx')

>>> library.getInfo()
{
    '帐号ID': '2016xxxxx', 
    '姓名': '张三', 
    '昵称': 'xx', 
    '登录次数': '123', 
    '状态': '正常'
}
```

## 文档
你可以在[https://ZhaoQi99.github.io/SNNU-SDK](https://ZhaoQi99.github.io/SNNU-SDK)看到本项目的完整使用文档。

## 贡献你的代码
欢迎您贡献出自己的一份力量，你可以随时提交`issue`或`fork`本仓库,静候你的`pull request`。

## 贡献者
感谢所有对本项目做出过贡献的开发者([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):


| [<img src="https://avatars3.githubusercontent.com/u/40024866?v=4" width="100px;"/><br /><sub><b>jhy</b></sub>](https://Small-funny.github.io/)<br />[💻](https://github.com/ZhaoQi99/SNNU-SDK/commits?author=Small-funny "Code") [📖](https://github.com/ZhaoQi99/SNNU-SDK/commits?author=Small-funny "Documentation")|
| :---: |

## 谁在使用

## 开源协议 & 作者
* 作者:Qi Zhao([zhaoqi99@outlook.com](mailto:zhaoqi99@outlook.com))
* 开源协议:[GNU General Public License v3.0](https://github.com/ZhaoQi99/SNNU-SDK/blob/dev/LICENSE)