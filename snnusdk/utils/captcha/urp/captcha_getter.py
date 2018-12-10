'''
Created on Dec 3, 2018

@author: QiZhao
'''
import os
import requests
import hashlib
from PIL import Image, ImageTk
import random
from io import BytesIO
import threading
import tkinter
from bs4 import BeautifulSoup
from snnusdk.tool.Table import table_to_list
from snnusdk.tool.Image import ImageBinarization
from snnusdk.utils.captcha.base import ImageToString

host = 'http://219.244.71.113/'
url_captcha = host + 'validateCodeAction.do'
url_login = host + 'loginAction.do'
headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    'Connection': 'close',
    'Referer': 'http://219.244.71.113/login.jsp'
}

save_image = 'save_image.txt'  # 本地已保存图片的hash值
data = 'data.txr'  # 图片的hash值与


class CaptchaGUI:

    def __init__(self, im, all_md5_name_file):
        self.im = im
        self.captcha_value = ""
        self.index = 0
        self.all_md5_name_file = all_md5_name_file

        self.root = tkinter.Tk()
        self.tkimg = ImageTk.PhotoImage(self.im)
        self.imgLabel = tkinter.Label(self.root, image=self.tkimg)
        self.imgLabel.pack()
        self.message = tkinter.Entry(self.root)
        self.message.pack()
        self.root.bind('<Return>', self.mark)
        self.root.mainloop()

    def mark(self, event):
        self.captcha_value = self.message.get()
        new_name = str(self.captcha_value) + ".gif"
        old_file = self.all_md5_name_file[self.index]
        os.rename('captchas/' + old_file, 'captchas/' + new_name)
        print("{}---->{}".format(old_file, new_name))
        self.index += 1
        if self.index < len(self.all_md5_name_file):
            file = self.all_md5_name_file[self.index]
            self.im = Image.open('captchas/' + file)
            self.tkimg = ImageTk.PhotoImage(self.im)
            self.imgLabel.config(image=self.tkimg)
            self.message.delete(0, 'end')
        else:
            self.root.quit()
            self.root.destroy()

    def __str__(self):
        return self.captcha_value


def Hash(img):
    '''
    获取对图片hash后的值
    '''
    md5 = hashlib.md5(img)
    return md5.hexdigest()


def Save(img, filename):
    '''
    保存图片
    '''
    with open("captchas/{}.gif".format(filename), 'wb') as f:
        f.write(img)


def GetAllImage():
    '''
    获取教务系统所有验证码
    '''
    if not os.path.exists('captchas/' + save_image):
        open(save_image, 'w')
    with open('captchas/' + save_image, 'r') as f:
        save_image = f.readlines()
    for i in range(0, len(save_image)):
        save_image[i] = save_image[i].strip('\n')
    num = len(os.listdir('captchas.'))
    ip_list = GetIpList()
    err = 0
    rep = 0
    pro = 0
    while True:
        pro += 1
        ip = ip_list[random.randint(0, len(ip_list) - 1)]
        proxies = {}
        proxies.update({
            'http': ip,
            "https": ip
        })
#         print(proxies)
        try:
            r = requests.get(url_captcha, proxies=proxies,
                             headers=headers, timeout=3).content
        except:
            err += 1
            print("ERROR:{}/{} {}% ip:{}".format(err, pro,
                                                 round(err * 1.0 / pro * 100, 2), ip))
            continue
        md5 = Hash(r)
        if md5 not in save_image:
            num += 1
            print("正在存储第{}张图片:{}".format(num, md5))
            Save(r, md5)
            save_image.append(md5)
            with open('captchas/' + save_image, 'a+') as f:
                f.write(md5 + '\n')
        else:
            rep += 1
            print("Existed:{}/{}\t{}% {}%".format(rep, pro, round(rep *
                                                                  1.0 / pro * 100, 2), round(rep * 1.0 / (pro - err) * 100, 2)))


def GenerateFromFile():
    '''
    从已经标记过的图片获取hash值与验证码的映射字典
    '''
    all_file = os.listdir('captchas.')
    for file in all_file:
        if file[-3:] == 'gif' and len(file) == 8:
            fd = open('captchas/' + file, "rb")
            img = fd.read()
            md5 = Hash(img)
            print(md5)
            with open('captchas/' + data, 'a+') as f:
                f.write("{},{}\n".format(md5, file[:4]))


def HumanMark():
    '''
    肉眼标记验证码
    '''
    all_file = os.listdir('captchas.')
    all_md5_name_file = []
    for file in all_file:
        if file[-3:] == 'gif' and len(file) > 8:
            all_md5_name_file.append(file)
    if len(all_md5_name_file) > 0:
        im = Image.open('captchas/' + all_md5_name_file[0])
        CaptchaGUI(im, all_md5_name_file)


def GetIpList():
    '''
    从代理网站库上获取代理ip
    '''
    ip_list = []
    r = requests.get('http://ip.jiangxianli.com/')
    soup = BeautifulSoup(r.text, 'lxml')
    table = soup.find(name='table', attrs={
                      "class": "table table-hover table-bordered table-striped"})
    ls = table_to_list(table)
    for dic in ls:
        ip_list.append(dic['IP'] + ':' + dic['端口'])
    return ip_list[:6]


def Ocr(content):
    '''
    使用ocr将图片识别为字符串
    '''
    im = Image.open(BytesIO(content))
    im = ImageBinarization(im, 140)
    value = ImageToString(im)
    return value


def OcrMark():
    '''
    使用Ocr标记验证码图片
    '''
    if not os.path.exists('captchas'):
        os.mkdir('captchas')
    data = {
        "zjh1": "",
        "tips": "",
        "lx": "",
        "evalue": "",
        "eflag": "",
        "fs": "",
        "dzslh": "",
        "zjh": "",
        "mm": "",
        "v_yzm": ""
    }
    num = 0
    success = 0
    while True:
        num += 1
        s = requests.session()
        v = s.get(url_captcha)
        value = Ocr(v.content)
        data['v_yzm'] = value
        r = s.post(url_login, data=data)
        if "你输入的验证码错误" in r.text:
            print("验证码输错了:" + value)
        else:
            success += 1
            print("成功！")
            with open("captchas/{}.gif".format(value), 'wb+') as f:
                f.write(v.content)
        print('正确率为:{}% {}/{}'.format(round(success / num * 100, 2), success, num))


if __name__ == '__main__':
    OcrMark()
#     threads = []
#     t1 = threading.Thread(target=GetAllImage)
#     threads.append(t1)
#     t2 = threading.Thread(target=HumanMark)
#     threads.append(t2)
#     for t in threads:
#         t.setDaemon(False)
#         t.start()
