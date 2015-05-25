#encoding=utf8
__author__ = 'JM'
from bs4 import BeautifulSoup;
import sys
if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    import urllib2;
    page= urllib2.urlopen("http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&sm=0&p=1").read();
    print page;
    soup=BeautifulSoup(page)
    for i in soup.find_all("a"):
        print i["href"]
