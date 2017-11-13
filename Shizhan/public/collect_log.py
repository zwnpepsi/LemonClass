#-*-coding:utf-8-*-
import logging
from Shizhan.public import projectpath
import os

class CollectLog:
    def __init__(self,logger_name):
        self.logger_name = logger_name

    def collectLog(self):
        #创建logger并设置收集log信息级别
        logger=logging.getLogger(self.logger_name)
        logger.setLevel(logging.INFO)
        if not logger.handlers:
        #创建一个文件handler，用于写入日志文件，并设置写入log信息过滤级别
            filehandler=logging.FileHandler(os.path.join(projectpath.Results_path,self.logger_name+".log"),encoding="utf-8")
            filehandler.setLevel(logging.INFO)
        #创建一个控制台handler，用户控制台输出日志信息，并设置输出log信息过滤级别
            streamhandler=logging.StreamHandler()
            streamhandler.setLevel(logging.INFO)
        #设置handler的日志输出格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
        #给handler添加格式
            filehandler.setFormatter(formatter)
            streamhandler.setFormatter(formatter)
        #给logger添加handler
            logger.addHandler(filehandler)
            logger.addHandler(streamhandler)

        # logging.basicConfig(level=logging.INFO,
        #                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        #                     datefmt='%m-%d %H:%M')
        return logger



# log=CollectLog()
# log.Collection()
