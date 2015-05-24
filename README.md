# spider_v1
简单的爬虫程序，从智联招聘获取相应的职位,公司信息
从终端进入iemp 目录，运行 scrapy crawl iemp 命令即可运行爬虫
爬虫将从jobs.urls指定页面开始，存储获取到的职位详情页面(jobs.zhaopin.com/[0-9]).html，公司详情页面（company.zhaopin.com），公司专题页面(special.zhaopin.com).
爬虫提供了存储接口，目前仅实现了简单的分文件存储，存储原始网页，后期将会添加更多存储支持。
爬虫内部提供了解析函数用于提取职位，公司信息。
原本打算解析工作放到后端以pyspark的方式实现。目前pyspark 函数序列化遇到点问题，后期着重解决。



