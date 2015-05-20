# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from bs4 import BeautifulSoup
from iemp.items import *
import scrapy

__author__ = 'cdchwei'
import scrapy


class IempSpider(scrapy.spider.Spider):
    name = "iemp"
    allowed_domains = ["zhaopin.com"]
    start_urls = [
        "http://sou.zhaopin.com/jobs/searchresult.ashx"
    ]
    def parse(self, response):
        file = open("url_list.txt",'a');
        file.write(response.url);
        soup=BeautifulSoup(response.body);
        divs=soup.find_all('div',class_='newlist_list_content')[0]
        for row in divs.find_all('table'):
            if row.select('tr').__len__()>=2: #排除table的head行
                jd=row.select('tr')
                info=jd[0]
                detail=jd[1]
                zwmc=info.find_all('td',class_="zwmc")[0].div.a.string
                gsmc=info.find_all('td',class_="gsmc")[0].string
                zwyx=info.find_all('td',class_="zwyx")[0].string
                gzdd=info.find_all('td',class_="gzdd")[0].string
                gxsj=info.find_all('td',class_="gxsj")[0].span.string
                jds=detail.find_all('li',class_='newlist_deatil_two')[0].find_all("span")
                jds2=detail.find_all('li',class_='newlist_deatil_last')[0].string
                print zwmc,gsmc,zwyx,gzdd,gxsj,jds.__len__(),jds[0].string,jds[1].string,jds[2].string,jds2
                jobItem=IempItem()
                jobItem['zwmc']=zwmc;

        next_page=soup.find_all('li',class_='pagesDown-pos')
        if next_page.__len__()==1:
            url=next_page[0].a['href']
            print url;
            yield scrapy.Request(url, callback=self.parse)

#        for div in sel.xpath('//div[@id="newlist_list_content_table"]'):
#            for row in div.xpath('//table[@class="newlist"]/tr'):
                #if(row.xpath('.//td[@class="zwmc"]/div/a/text()').extract().__len__()>0):
                 #   a=row.xpath('.//td[@class="zwmc"]/div/a/text()').extract()[0].encode('gbk')
                  #  b= row.xpath('.//td[@class="gsmc"]/a/text()').extract()[0].encode('gbk')
                   # c= row.xpath('.//td[@class="zwyx"]/text()').extract()[0].encode('gbk')
                   # d= row.xpath('.//td[@class="gzdd"]/text()').extract()[0].encode('gbk')
                   # e= row.xpath('.//td[@class="gxsj"]/span/text()').extract()[0].encode('gbk')
                    #print row

