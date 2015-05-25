# encoding=utf8
# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from bs4 import BeautifulSoup;
from iemp.items import IempItem;
from iemp.tools import tools;
from urlparse import urlparse;
from urllib import quote
import re;
import scrapy
__author__ = 'cdchwei'


class IempSpider(scrapy.spider.Spider):
    name = "iemp"
    allowed_domains = ["zhaopin.com"]
    start_urls = tools.loadurls();
    def __init__(self, pd=None,jl=None,et=None, *args, **kwargs):
        super(scrapy.spider.Spider, self).__init__(*args, **kwargs);
        base_url='http://sou.zhaopin.com/jobs/searchresult.ashx?isfilter=1&p=1'
        if(pd != None):
            base_url=base_url+'&pd='+pd;
        if jl != None :
            jlq=quote(jl);
            base_url=base_url+"&jl="+jlq;
        if et !=None:
            base_url=base_url+"&et="+et;
        self.start_urls = [base_url]
        if(pd==None and jl==None and et==None) :
            start_urls = tools.loadurls();
    def parse(self, response):
        print response.url;
        currnent_host=urlparse(response.url).hostname
        current_url=response.url;
        current_page_number=re.search('http*p=([0-9]+)\w*',current_url);
        cpn=1;
        if( current_page_number!= None ):
            cpn=int(current_page_number.group(1))
        soup=BeautifulSoup(response.body);
        link_set=set();
        links=soup.find_all('a');
        for link in links:
            sub_url=link.get('href')
            try:
                if (None<>sub_url)&(sub_url.__str__().lower().startswith("http")):
                       link_set.add(sub_url)
                elif(sub_url.__str__().lower().startswith("/")):
                    link_set.add('http://'+currnent_host+sub_url)
            except Exception as e:
                print e;
        for p in link_set:
            hostname = urlparse(p).hostname;
            if(hostname=='company.zhaopin.com' or hostname=='special.zhaopin.com' or IempSpider.is_jd_page(p)):
                yield scrapy.Request(p, callback=self.parse_singe_page)
            elif (hostname == 'sou.zhaopin.com'):
                print p;
                #if(re.search('http*p=([0-9]+)\w*',p))!=None:
                yield scrapy.Request(p, callback=self.parse);
            else:
                pass;
    @staticmethod
    def is_jd_page(url):
        job_page = 'http://jobs.zhaopin.com/([0-9]*).html*'
        return re.search(job_page,url);

    def parse_singe_page(self,response):
        page=IempItem();
        page["url"] = response.url;
        page["html_body"] = response.body.replace('\n','$').replace('\r',' ').replace('\t', ' ')
        return page;


