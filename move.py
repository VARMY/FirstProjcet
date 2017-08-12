# encoding:utf-8

import requests
from bs4 import BeautifulSoup
import re

# def move_get():
#
#         # for i in range(1,3):
#             url = 'http://newoss.maiziedu.com/qiniu/Scrapy-11.mp4'
#             print(url.split('/')[-1])
#             req = requests.get(url)
#             file = open('F:\\spider\\'+ url.split('/')[-1], 'wb')
#             file.write(req.content)
#             file.close()
#
# if __name__ == '__main__':
#     move_get()

req = requests.get('http://www.smiler.ren:2333/random')
print(req)