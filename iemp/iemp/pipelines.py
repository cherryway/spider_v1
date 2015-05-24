# encoding=utf8
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from scrapy import signals;
from handleStorage import handle;
from urlparse import urlparse;


class IempPipeline(object):

    def __init__(self):
        pass;

    def process_item(self, item, spider):
        up=urlparse(item['url'])
        handle.hash_save(item['url'], item['url']+'\t'+item['html_body'], up.hostname);
        handle.mongo_save(item['url'],item,[])
        return item

    def spider_closed(self, spider):
        pass
