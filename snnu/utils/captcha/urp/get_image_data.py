'''
Created on Dec 3, 2018

@author: QiZhao
'''
import hashlib
import json
import os
import shutil

from PIL import Image
from snnu.utils.captcha.urp.urp_captcha import UrpCaptcha
from snnu.tool.Image import build_vector
import time


def SpiltToChars():
    """
    分割已有的数据为字符并保存
    """
    try:
        shutil.rmtree('captcha_train')
    except:
        pass
    os.mkdir("captcha_train")
    values = "abcdefghijklmnopqrstuvwxyz1234567890"
    for value in values:
        os.mkdir('captcha_train/{}'.format(value))

    file_names = os.listdir('captchas.')
    for file_name in file_names:  #
        values = file_name[:4]
        im = Image.open('captchas/{}'.format(file_name))
        captcha = UrpCaptcha(im)
        for im_part, value in zip(captcha.handle_split_image(), values):
            m = hashlib.md5()
            m.update("{}{}".format(time.time(), value).encode('utf8'))
            im_part.save("captcha_train/{}/{}.png".format(value, m.hexdigest()))
            
def GenerateVector():
    '''
    从分割后的图像数据生成向量数据
    '''
    letters = list('0123456789abcdefghijklmnopqrstuvwxyz')
    # 将图像数据转为向量数据并保存
    imageset = []
    for letter in letters:
        for img in os.listdir('captcha_train/{}/'.format(letter)):
            vector = build_vector(Image.open("captcha_train/{}/{}".format(letter, img)))
            imageset.append({letter: vector})

    with open('image_data.json', 'w') as f:
        json.dump(imageset, f)
        
if __name__ == "__main__":
    SpiltToChars()
    GenerateVector()
