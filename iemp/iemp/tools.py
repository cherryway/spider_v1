__author__ = 'cdchwei'
import sys,os
class tools:
    @staticmethod
    def loadurls():
        file = open(os.getcwd()+'/jobs.urls','r').read();
        return file.split("\n");

    @staticmethod
    def  searchurls():
        file = open(os.getcwd()+'/search.urls').read();

    @staticmethod
    def getPartitions(con,num=10):
        return hash(con)%num;
