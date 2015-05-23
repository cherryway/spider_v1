# coding=utf-8
__author__ = 'cdchwei'

import re;
from bs4 import BeautifulSoup;
import urllib2;


def parseJobs(page):
    soup = BeautifulSoup(page.replace('\u001\u002\u003', '\n'));
    job_labels = soup.find_all('div', class_='inner-left fl')[0];
    print job_labels.h1.string;
    print job_labels.h2.a.get('href');
    label = [];
    for l in job_labels.div.find_all('span'):
        label.append(l.string);
        print l.string;
    print label;
    job_item = soup.find_all('ul', class_='terminal-ul clearfix')[0].find_all('li');
    job_items = [];
    for i in job_item:
        key = i.span.string
        value = i.strong.string;
        if (key == '工作地点：'):
            print 'xxx'
            value = i.strong.a.string
        elif (key == '发布日期：'):
            value = i.strong.span.string;
        elif (key == '职位类别：'):
            print '****'
            for v in i.strong.find_all('a'):
                value = value + v.string
        else:
            print 's'
            value = i.strong.string
        job_items.append((key, value));
        print key, value


if __name__ == '__main__':
    job_page = re.compile('http://jobs.zhaopin.com/([0-9]*).htm*')
    result = job_page.match('http://jobs.zhaopin.com/674881428250028.htm?ssidkey=y&ss=201&ff=03')
    company_patten = 'http://company.zhaopin.com/(CC[0-9]+).html*'
    job_patten = 'http://jobs.zhaopin.com/([0-9]+).htm*'
    print result.string
    print re.search(job_patten, 'http://jobs.zhaopin.com/674881428250028.htm?ssidkey=y&ss=201&ff=03').group(1)
    print re.search(company_patten, 'http://company.zhaopin.com/CC674881428.htm').group(1);
    parseJobs(urllib2.urlopen("http://jobs.zhaopin.com/674881428250028.htm").read())



