__author__ = 'cdchwei'
from bs4 import BeautifulSoup;
from urlparse import urlparse;
import re;
import scrapy
from iemp.items import IempItem;
class SearchSpider(scrapy.spider.Spider):
    name = "search"
    allowed_domains = ["zhaopin.com"];
    start_urls =[];
    def __init__(self, category=None, *args, **kwargs):
        super(scrapy.spider.Spider, self).__init__(*args, **kwargs);
        self.start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?p=%s' % category]
    def parse(self, response):
        current_url=response.url;
        current_page_number=int(re.search('http*p=([0-9]+)\w*',current_url).group(1))
        if current_page_number>=1:
            pass;
        else:
            current_page_number=1;
        soup=BeautifulSoup(response.body);
        link_set = set();
        links = soup.find_all('a');
        for link in links:
            sub_url = link.get('href');
            try:
                if (None != sub_url) and (sub_url.__str__().lower().startswith("http")):
                    link_set.add(sub_url)
            except Exception as e:
                print e;
        for p in link_set:
            hostname = urlparse(p).hostname;
            if (hostname == 'sou.zhaopin.com') and  int(re.search('http*p=([0-9]+)\w*',p).group(1))>current_page_number:
                yield scrapy.Request(p, callback=self.parse);
            elif(hostname == 'jobs.zhaopin.com' or hostname == 'company.zhaopin.com' or
                         hostname == 'special.zhaopin.com'):
                yield scrapy.Request(p, callback=self.parse_singe_page);
            else:
                pass;

    def parse_singe_page(self,response):
        page=IempItem();
        page["url"] = response.url;
        page["html_body"] = response.body.replace('\n',"\001\002").replace('\r','')
        return page;
        pass;
