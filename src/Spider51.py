__author__ = 'cdchwei'
#coding=utf-8
__author__ = 'cdchwei'
from sgmllib import SGMLParser
import urllib;
class GetIdList(SGMLParser):
    def reset(self):
        self.IDlist = []
        self.flag = False
        self.getdata = False
        self.verbatim = 0
        SGMLParser.reset(self)
    def start_div(self,attr):
        if self.flag == True:
            self.verbatim +=1
            return
if __name__ == "__main__":
    job51=urllib.urlopen('http://search.51job.com/list/%2B,%2B,%2B,%2B,%2B,%2B,hadoop,1,%2B.html?lang=c&stype=1&image_x=0&image_y=0').read()
    list=GetIdList();
    list.feed(job51);
    list.printID()