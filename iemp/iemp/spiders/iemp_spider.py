# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from bs4 import BeautifulSoup;
from iemp.items import IempItem;
import scrapy
__author__ = 'cdchwei'


class IempSpider(scrapy.spider.Spider):
    name = "iemp"
    allowed_domains = ["zhaopin.com"]
    start_urls = [
        "http://www.zhaopin.com"
    ]
    def parse(self, response):
        page=IempItem();
        page["url"] = response.url;
        page["html_body"] = response.body;
        soup=BeautifulSoup(response.body);
        # next_page=soup.find_all('li',class_='pagesDown-pos')
        links=soup.find_all('a');
        for link in links:
            sub_url=link.get('href')
            # print sub_url;
            try:
                if (None<>sub_url)&(sub_url.__str__().lower().startswith("http")):
                    yield scrapy.Request(sub_url, callback=self.parse)
            except Exception as e:
                print e;
        # if next_page.__len__()==1:
            # url=next_page[0].a['href']
            # print url;
            # yield scrapy.Request(url, callback=self.parse)

