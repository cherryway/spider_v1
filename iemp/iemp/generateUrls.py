#coding=utf-8
__author__ = 'cdchwei'
from urllib import quote
class searchUrl:
    normal_search = 'http://sou.zhaopin.com/jobs/searchresult.ashx'
    ctype = -1;
    salary = (-1,-1)
    filter = 1
    education = -1
    experience = -1
    job_type = -1
    days = -1
    job_label = [];
    company_id = '';
    url='';
    def __init__(self,work_area,work_type,industry, filter, salary, ctype, education, experience, job_type,days,label):
        self.work_area = work_area;
        self.work_type = work_type;
        self.industry = industry;
        self.filter = filter;
        self.salary = salary;
        self.ctype = ctype;
        self.education = education;
        self.experience = experience;
        self.job_type = job_type;
        self.days = days;
        self.job_label = job_label;
    def __init__(self,company_id):
        self.normal_search='http://sou.zhaopin.com/jobs/companysearch.ashx'
        self.company_id=company_id;
        self.url=self.normal_search+'?'+'?CompID='+self.company_id;
    def __init__(self,days):
        self.url=self.normal_search+'?isfilter=1&pd='+str(days);
    def __init__(self):
        self.url=self.normal_search;
    def __init__(self,work_area):
        areas='';
        for area in work_area:
            if areas=='':
                areas=area;
            else:
                areas=areas+"+"+area;
        self.url=self.normal_search+"?jl="+quote(areas);
    def __init__(self,work_area,days):
        areas='';
        for area in work_area:
            if areas=='':
                areas=area;
            else:
                areas=areas+"+"+area;
        self.url=self.normal_search+"?jl="+quote(areas)+"&pd="+str(days);
    def get_urls(self):
        return self.url;
if __name__ == '__main__':
     open("../jobs.urls",'a').write("\n"+searchUrl(work_area=['北京','上海'],days=7).get_urls())