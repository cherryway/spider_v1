# encoding=utf8
# -*- coding: utf-8 -*-

# Scrapy settings for iemp project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'iemp'

SPIDER_MODULES = ['iemp.spiders']
NEWSPIDER_MODULE = 'iemp.spiders'

ITEM_PIPELINES = {
    'iemp.pipelines.IempPipeline': 100,
    }
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
CONCURRENT_REQUESTS = 100
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'iemp (+http://www.yourdomain.com)'
