# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from bs4 import BeautifulSoup;
from iemp.items import IempItem;
from iemp.url_loading import tools;
import scrapy
__author__ = 'cdchwei'


class IempSpider(scrapy.spider.Spider):
    name = "iemp"
    allowed_domains = ["zhaopin.com"]
    start_urls = tools().loadurls();
    def parse(self, response):
        page=IempItem();
        page["url"] = response.url;
        page["html_body"] = response.body.replace('\n','\u001\u002\u003').replace("\r","")
        #response.body.replace("\n","\u001\u002");
        soup=BeautifulSoup(response.body);
        # next_page=soup.find_all('li',class_='pagesDown-pos')
        links=soup.find_all('a');
        for link in links:
            sub_url=link.get('href')
            # print sub_url;
            try:
                if (None<>sub_url)&(sub_url.__str__().lower().startswith("http")):
                       scrapy.Request(sub_url,callback=self.parse);
            except Exception as e:
                print e;
        return page;
        # if next_page.__len__()==1:
            # url=next_page[0].a['href']
            # print url;
            # yield scrapy.Request(url, callback=self.parse)

