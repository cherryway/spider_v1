# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from bs4 import BeautifulSoup;
from iemp.items import IempItem;
from iemp.tools import tools;
from urlparse import urlparse;
import re;
import scrapy
__author__ = 'cdchwei'


class IempSpider(scrapy.spider.Spider):
    name = "iemp"
    allowed_domains = ["zhaopin.com"]
    start_urls = tools.loadurls();

    def parse(self, response):
        soup=BeautifulSoup(response.body);
        link_set=set();
        links=soup.find_all('a');
        for link in links:
            sub_url=link.get('href')
            try:
                if (None<>sub_url)&(sub_url.__str__().lower().startswith("http")):
                       link_set.add(sub_url)
            except Exception as e:
                print e;
        for p in link_set:
            if(urlparse(p).hostname=='company.zhaopin.com' or urlparse(p).hostname=='special.zhaopin.com' or IempSpider.is_jd_page(p)):
                yield scrapy.Request(p, callback=self.parse_singe_page)
            else:
                yield scrapy.Request(p, callback=self.parse)

    @staticmethod
    def is_jd_page(url):
        job_page = 'http://jobs.zhaopin.com/([0-9]*).html*'
        return re.search(job_page,url);

    def parse_singe_page(self,response):
        page=IempItem();
        page["url"] = response.url;
        page["html_body"] = response.body.replace('\n',"\001").replace("\r","")
        return page;


