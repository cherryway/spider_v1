#coding=utf-8
__author__ = 'cdchwei'
from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
def parseLinks(page):
    soup=BeautifulSoup(page.replace('\u001\u002\u003','\n'))
    links=soup.find_all('a');
    lk=[]
    for link in links:
        lk.append(link.get('href'))
    return lk;

def parseJobs(page):
    soup=BeautifulSoup(page.replace('\u001\u002\u003','\n'));
    job_labels=soup.find_all('div',class_='inner-left fl')[0];
    print job_labels.h1.string;
    print job_labels.h2.a.get('href');
    label=[];
    for l in job_labels.div.find_all('span'):
        label.append(l.string);
    print label;
    job_item=soup.find_all('ul',class_='terminal-ul clearfix')[0].find_all('li');
    job_items=[];
    for i in job_item:
        key=i.span.string
        value='';
        if(key=='职位月薪：' or key=='工作性质：' or key=='工作经验：' or  key== '最低学历：' or key=='招聘人数：'):
            value=i.strong.string;
        elif(key=='工作地点：'):
            value=i.strong.a.get("href")
        elif(key=='发布日期：'):
            value=i.strong.span.string;
        elif(key=='职位类别：'):
            value=i.find_all('a',targrt='_blank')[0].string
        job_items.append((key,value));
    print job_items

