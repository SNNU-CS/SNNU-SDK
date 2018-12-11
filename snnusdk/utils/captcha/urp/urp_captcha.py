'''
Created on Dec 3, 2018

@author: QiZhao
'''
import json
import os
from io import BytesIO
import requests
from PIL import Image
from snnusdk.tool.Image import ImageBinarization
from snnusdk.utils.captcha.base import ImageToString

current_dir = os.path.dirname(os.path.abspath(__file__))


class UrpCaptcha:
    """
    ocr 识别urp验证码
    """

    def __init__(self, image):
        self.image = image
        self.image_pre_process()

    def image_pre_process(self):
        threshold = 140
        self.image = ImageBinarization(self.image, threshold)

    def crack(self):
        return ImageToString(self.image)

    def __str__(self):
        return self.crack()


if __name__ == "__main__":
    r = requests.get("http://219.244.71.113/validateCodeAction.do")
    im = Image.open(BytesIO(r.content))
    im.show()
    cap = UrpCaptcha(im)
    print(cap)
