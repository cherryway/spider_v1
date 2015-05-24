# -*- coding: utf-8 -*-
__author__ = 'cdchwei'
from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
import urllib2;
class parser:
    @staticmethod
    def parseJobs(page):
        url=page.split("\t")[0];
        content=page.split("\t")[1];
        print url,content
        soup=BeautifulSoup(content.replace('$','\n'));
        job_labels=soup.find_all('div',class_='inner-left fl')[0];
        job_name = job_labels.h1.string;
        company_url = job_labels.h2.a.get('href');
        label=[];
        for l in job_labels.div.find_all('span'):
            label.append(l.string);
        job_item=soup.find_all('ul',class_='terminal-ul clearfix')[0].getText();
        jd=soup.find_all('div','tab-inner-cont')[0].getText();
        #print job_name,company_url,label,job_item,jd
        return (job_name, company_url ,label,job_item,jd)

    @staticmethod
    def parseCompany(page):
        url=page.split("\t")[0];
        content=page.split("\t")[1];
        soup=BeautifulSoup(content.replace('\001\002','\n'));
        com1 = soup.find_all('div',class_='main3 main4')[0]
        company_name = com1.h1.string
        basic_info=com1.find_all('dl',class_="basic-information")[0].getText().replace(" ","").replace("\n",":")
        company_desc=com1.find_all("div",class_="company-introduction")[0].getText();
        return (company_name,basic_info,company_desc);



