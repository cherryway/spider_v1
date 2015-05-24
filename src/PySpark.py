__author__ = 'cdchwei'
from bs4 import BeautifulSoup;
import sys

from pyspark import SparkContext
from pyspark import SparkConf;
import pymongo
import json;
def parseJobs(page):
    sys.setrecursionlimit(1000000)
    url=page.split("\t")[0];
    content=page.split("\t")[1];
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
    return {'job_name':job_name,'company_url': company_url ,'label':label,'job_item':job_item,'jd':jd};

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[*]").setAppName("parseJobs")
    sc = SparkContext(conf)
    te=sc.textFile(sys.argv[0]);
    jobs=te.map(lambda x:parseJobs(x));
    conn=pymongo.MongoClient(host="127.0.0.1",port=27017);
    db=conn.spider;
    db.job_info;
    def mongo_save(x):
        db.job_info.save(x);
    for i in jobs.collect():
        mongo_save(json.dumps(dict(i)));
    sc.stops();


