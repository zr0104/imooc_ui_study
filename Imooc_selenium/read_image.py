# coding:utf-8
import pytesseract
from PIL import Image
# from ShowapiRequest import ShowRequest
image = Image.open("C:/Users/KXYL/PycharmProjects/imooc_study/Image/test001.png")
text = pytesseract.image_to_string(image)
print(text)
