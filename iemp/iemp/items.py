# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class IempItem(scrapy.Item):
    zwmc = scrapy.Field()
    gsmc = scrapy.Field()
    zwyx = scrapy.Field()
    gzdd = scrapy.Field()
    gxsj = scrapy.Field()
    area = scrapy.Field()
    type = scrapy.Field()
    scale = scrapy.Field()
    exp = scrapy.Field()
    education =scrapy.Field()
    salary=scrapy.Field()
    jd=scrapy.Field()
    pass
