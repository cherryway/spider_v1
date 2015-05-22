#coding=utf8
__author__ = 'JM'
from bs4 import BeautifulSoup;
import urllib2
def search_parser(content):
    soup=BeautifulSoup(content);
    divs=soup.find_all('div',class_='newlist_list_content')[0];
    jobs=[];
    for row in divs.find_all('table'):
        if row.select('tr').__len__()>=2:
            jd=row.select('tr')
            info=jd[0]
            detail=jd[1]
            zwmc=info.find_all('td',class_="zwmc")[0].div.a.string
            gsmc=info.find_all('td',class_="gsmc")[0].string
            zwyx=info.find_all('td',class_="zwyx")[0].string
            gzdd=info.find_all('td',class_="gzdd")[0].string
            gxsj=info.find_all('td',class_="gxsj")[0].span.string
            jds=detail.find_all('li',class_='newlist_deatil_two')[0].find_all("span")
            jds2=detail.find_all('li',class_='newlist_deatil_last')[0].string
            company_desc=[];
            for i in jds:
                company_desc.append(i.string)
            job=(zwmc,gsmc,zwyx,gzdd,gxsj,company_desc);
            jobs.append(job);
    return jobs;


if __name__ == '__main__':
    jobs=open('../iemp/zhaopin.txt')
    text=jobs.read()
    jobs.close();
    soup=BeautifulSoup(text);
    #get job infor div div class=newlist_list_content
    divs=soup.find_all('div',class_='newlist_list_content')[0]
    i=1;
    for row in divs.find_all('table'):
         if row.select('tr').__len__()>=2: #remove table head
            jd=row.select('tr')
            info=jd[0]
            detail=jd[1]
            zwmc=info.find_all('td',class_="zwmc")[0].div.a.string
            gsmc=info.find_all('td',class_="gsmc")[0].string
            zwyx=info.find_all('td',class_="zwyx")[0].string
            gzdd=info.find_all('td',class_="gzdd")[0].string
            gxsj=info.find_all('td',class_="gxsj")[0].span.string
            jds=detail.find_all('li',class_='newlist_deatil_two')[0].find_all("span")
            jds2=detail.find_all('li',class_='newlist_deatil_last')[0].string
            print i,zwmc,gsmc,zwyx,gzdd,gxsj,jds[0].string,jds[1].string,jds[2].string,jds[3].string,jds.__len__(),jds2,'#'
            i=i+1
    next_page=soup.find_all('li',class_='pagesDown-pos')
    print  next_page.__len__()
    if next_page.__len__()>0:
        url=next_page[0].a['href']
        print url;
        regex = url.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', url.IGNORECASE)
        print regex
    #print divs.encode('gbk')
    #print text;