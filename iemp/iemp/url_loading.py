__author__ = 'cdchwei'
import sys,os
class tools:

    def loadurls(self):
        file = open(os.getcwd()+'/url.properties','r').read();
        return file.split("\n");