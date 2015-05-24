# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
class IempItem(scrapy.Item):
    url = scrapy.Field()
    html_body = scrapy.Field()
    pass
class JobItem(scrapy.Item):
    job_name = scrapy.Field()
    company_url = scrapy.Field()
    label = scrapy.Field()
    job_item = scrapy.Field()
    jd = scrapy.Field()
class CompanyItem(scrapy.Item):
    company_name = scrapy.Field()
    basic_info = scrapy.Field()
    company_desc = scrapy.Field()
