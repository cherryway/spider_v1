# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from scrapy import signals;

class IempPipeline(object):

    def __init__(self):
        self.file = codecs.open('zhaopin.txt', 'wb')
        self.file2 = codecs.open('zhaopinsearch.txt', 'wb')

    def process_item(self, item, spider):
        #self.file = codecs.open('zhaopin.json', 'a', encoding='utf-8')
        #line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        if item["url"].find('sou.zhaopin.com')<>-1:
            self.file2.write(item["url"]+"\u004"+item["html_body"]+"\n")
        else:
            self.file.write(item["url"]+"\u004"+item["html_body"]+"\n")
        #self.file.close()
        return item

    def spider_closed(self, spider):
        self.file.close()
        self.file2.close();
