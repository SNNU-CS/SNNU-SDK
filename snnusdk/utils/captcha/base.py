'''
Created on Dec 4, 2018

@author: QiZhao
'''
import pytesseract


def ImageToString(im):
    '''
    使用ocr将图片识别为字符串
    '''
    value = ''
    try:
        value = str(pytesseract.image_to_string(im, lang='eng'))
    except Exception as e:
        raise e
    value = value.replace(' ', '')
    return value
