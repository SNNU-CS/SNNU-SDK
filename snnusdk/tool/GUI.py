'''
Created on Nov 29, 2018

@author: QiZhao
'''
import tkinter
from io import BytesIO

import requests
from PIL import Image, ImageTk


class CaptchaGUI:

    def __init__(self, im):
        self.im = im
        self.captcha_value = ""

        self.root = tkinter.Tk()
        self.tkimg = ImageTk.PhotoImage(self.im)
        self.imgLabel = tkinter.Label(self.root, image=self.tkimg)
        self.imgLabel.pack()
        self.message = tkinter.Entry(self.root)
        self.message.pack()
        self.root.bind('<Return>', self.input)
        self.root.mainloop()

    def input(self, event):
        self.captcha_value = self.message.get()
        # print(self.captcha_value)
        self.root.quit()

    def __str__(self):
        return self.captcha_value


if __name__ == "__main__":
    captcha_url = "http://219.244.71.113/validateCodeAction.do"
    r = requests.get(captcha_url)
    im = Image.open(BytesIO(r.content))
#     im.show()
    captcha_gui = CaptchaGUI(im)
    print(captcha_gui)
