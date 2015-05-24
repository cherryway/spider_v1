# encoding=utf8
__author__ = 'cdchwei'
from iemp.tools import tools;
from kazoo.client import KazooClient
from samsa.cluster import Cluster
#import pymongo;
import json
class handle:
    @staticmethod
    def print_save(key,content,pre=''):
        print key,content;
    @staticmethod
    def hash_save(key,content,pre='',partion_num=10):
        open(pre+'.'+str(tools.getPartitions(key,partion_num))+".csv",'a').write(content+"\n");
    @staticmethod
    def hdfs_save(key,content,hdfs,pre='',):
        pass;
    @staticmethod
    def hbase_save(key,content,hbase,pre=''):
        pass;
    @staticmethod
    def mongo_save(key,content,momgo,pre=''):
        #conn = pymongo.Connection("127.0.0.1",27017);
        #db = conn.test;
        #tabs=pre+'.'+str(tools.getPartitions(key,10));
        #db.demo.save(json.dumps(dict(content)))
        pass
    @staticmethod
    def kafka_save(key,content,kafka,pre=''):
        zookeeper = KazooClient()
        zookeeper.start()
        cluster = Cluster(zookeeper)
        topic = cluster.topics['topicname']
        topic.publish('msg')
        pass
