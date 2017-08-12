# -*- coding: utf-8 -*-
import scrapy
from ..items import YoutuItem
from scrapy.http import Request
from bs4 import BeautifulSoup

class HuaSpider(scrapy.Spider):
    name = 'hua'

    def start_requests(self):
        for i in range(1,5):
            url = 'http://www.youtu88.com/smhx.asp?sortpath=0,384,&pnew=0&com=&order=id&page=%s'%(i)
            yield Request(url,self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        img_url = soup.select('.transp-block a img')
        bts = YoutuItem()
        for i in img_url:
            bts['imgurl'] = i.get('src')
            yield bts

        #     print(img.split('/')[-1])
        #     filte = open('F:\\pic\\'+'编号：'+img.split('/')[-1], 'wb')
        #     filte.write(img)
        # filte.close()
