__author__ = 'cdchwei'
from iemp.tools import tools;
class handle:
    @staticmethod
    def print_save(key,content,pre=''):
        print key,content;
    @staticmethod
    def hash_save(key,content,pre='',partion_num=10):
        open(pre+'.'+str(tools.getPartitions(key,partion_num)),'a').write(content);
    @staticmethod
    def hdfs_save(key,content,hdfs,pre='',):
        pass;
    @staticmethod
    def hbase_save(key,content,hbase,pre=''):
        pass;
    @staticmethod
    def mongo_save(key,content,momgo,pre=''):
        pass
    @staticmethod
    def kafka_save(key,content,kafka,pre=''):
        pass
