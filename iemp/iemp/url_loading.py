__author__ = 'cdchwei'
class tools:

    def loadurls(self):
        file = open('../url.properties','r').read();
        return file.split("\n");
if __name__ == '__main__':
       x=tools().loadurls();
       print x