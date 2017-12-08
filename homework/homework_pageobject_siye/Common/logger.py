import logging
from homework.homework_pageobject_siye.Common.projectpath import *


class CommLog:

    def __init__(self,logname):
        self.mylog = logging.getLogger(logname)
        self.mylog.setLevel(logging.INFO)
        self.logpath = Log_path + "\\"+logname+".log"
        print("日志路径：")
        print(self.logpath+"\n")

    def setFormatter(self):
        fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
        datefmt = '%a, %d %b %Y %H:%M:%S'
        formatter = logging.Formatter(fmt, datefmt)
        return formatter

    def add_StreamHandler(self,logLevel=None):
        handler = logging.StreamHandler()
        handler.setFormatter(self.setFormatter())
        if logLevel != None:
            handler.setLevel(logLevel)
        self.mylog.addHandler(handler)

    def add_RotatingFileHandler(self,logLevel=None,maxBytes=1024*1024*100,backupCount=10):
        from logging.handlers import RotatingFileHandler
        handler = RotatingFileHandler(self.logpath, maxBytes, backupCount, encoding = "UTF-8")
        handler.setFormatter(self.setFormatter())
        if logLevel != None:
            handler.setLevel(logLevel)
        self.mylog.addHandler(handler)

    def info(self,message):
        self.mylog.info(message)

    def warn(self,message):
        self.mylog.warning(message)

    def debug(self,message):
        self.mylog.debug(message)

    def error(self,message):
       self.mylog.error(message)

    def critical(self,mesaage):
        self.mylog.critical(mesaage)

    def exception(self,message):
        self.mylog.exception(message)


# myLog = CommLog("web_autoTest")
# myLog.add_StreamHandler(logging.INFO)
# myLog.add_RotatingFileHandler(logging.INFO)

