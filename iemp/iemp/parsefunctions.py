__author__ = 'cdchwei'
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

