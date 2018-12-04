'''
Created on Dec 3, 2018

@author: QiZhao
'''
import json
import os
from io import BytesIO
import requests
from PIL import Image
from snnu.tool.Image import distance_hanmming, build_vector,ImageBinarization

current_dir = os.path.dirname(os.path.abspath(__file__))


class UrpCaptcha:
    """
    knn 识别urp验证码
    """

    def __init__(self, image):
        self.image = image
        self.image_pre_process()

    def image_pre_process(self):
        threshold=140 
        self.image = ImageBinarization(self.image,threshold) 
        

    def handle_split_image(self):
        # 切割验证码，返回包含四个字符图像的列表
        y_min, y_max = 0, 20
        split_lines = [5, 18, 31, 44, 57]
        ims = [self.image.crop([u, y_min, v, y_max]) for u, v in zip(split_lines[:-1], split_lines[1:])]
        return ims

    def crack(self):
        result = []
        # 加载数据
        with open(os.path.join(current_dir, 'image_data.json'), 'rb+') as f:
            image_data = json.load(f)
        for letter in self.handle_split_image():
            letter_vector = build_vector(letter)
            guess = []
            for image in image_data:
                for x, y in image.items():
                    guess.append((distance_hanmming(y, letter_vector), x))
            guess.sort()
            neighbors = guess[:15]  # 距离最近的十五个向量
            class_votes = {}  # 投票
            for neighbor in neighbors:
                class_votes.setdefault(neighbor[-1], 0)
                class_votes[neighbor[-1]] += 1
            sorted_votes = sorted(class_votes.items(), key=lambda x: x[1], reverse=True)
            result.append(sorted_votes[0][0])
        return ''.join(result)

    def __str__(self):
        return self.crack()


if __name__ == "__main__":
    r = requests.get("http://219.244.71.113/validateCodeAction.do")
    im = Image.open(BytesIO(r.content))
    im.show()
    cap=UrpCaptcha(im)
    print(cap)