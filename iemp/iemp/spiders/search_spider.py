__author__ = 'cdchwei'
import scrapy
from bs4 import BeautifulSoup;
from iemp.items import IempItem;
from iemp.tools import tools;
class SearchSpider(scrapy.spider.Spider):
    name = "search"
    allowed_domains = ["zhaopin.com"]
    start_urls = tools().searchurls();
def parse(self, response):
    soup = BeautifulSoup(response.url);
    links=soup.find_all('a');
    job_links=[];
    company_links=[];
    for link in links:
        url=link.get('href');
        print url;
