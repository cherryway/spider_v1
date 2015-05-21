#coding=utf8
__author__ = 'JM'
from bs4 import BeautifulSoup;
class SeachParser:
    def parse(self, response):
        soup=BeautifulSoup(response.body);
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
