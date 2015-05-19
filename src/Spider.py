__author__ = 'cdchwei'
import urllib;
import urllib2;
import bs4;
from bs4 import BeautifulSoup;
from sgmllib import SGMLParser

class ListName(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_h4 = ""
        self.name = []
    def start_h4(self, attrs):
        self.is_h4 = 1
    def end_h4(self):
        self.is_h4 = ""
    def handle_data(self, text):
        if self.is_h4 == 1:
            self.name.append(text)

content = urllib2.urlopen('http://list.taobao.com/browse/cat-0.htm').read()
listname = ListName()
listname.feed(content)
for item in listname.name:
    print item.decode('gbk').encode('utf8')

def getHtml(url):
    return urllib.urlopen(url).read()

if __name__ == "__main__":
    #print(getHtml("http://www.baidu.com"))
    print('***********')
    page=urllib2.urlopen('http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&sj=044%3b047%3b053&in=210500&jl=%E6%88%90%E9%83%BD&sm=0&we=-1&ct=-1&el=-1&pd=-1&isfilter=1&et=-1&sg=2740fcd7b3ae4b9aaace4a32ce9d5c5b&p=2');
    soup=BeautifulSoup(page)
    #print soup.getText
    print soup.title.string
    print soup.select('div').__len__()
    for link in soup.select('a[href^=http://news]'):
        print link['href']
    #for div in soup.select('div[id^=newlist_list_content_table]'):
    #    print(div)
    #div=soup.select('div[id^=newlist_list_content_table]')[0]
    #print div,"sss";
    #print soup.table
    css_soup = BeautifulSoup('<p class="body strikeout"></p>')
    print css_soup.find_all("p", class_="strikeout")
    print soup.select('table')[0]
#    for tab in soup.select('table'):
#        single=BeautifulSoup(tab.text)
#        print single