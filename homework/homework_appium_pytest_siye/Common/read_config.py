# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/23 14:41
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : read_config.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import  configparser


class ReadConfig:

    def __init__(self):
        pass

    def readConfig(self,path,section,option):
        cf = configparser.ConfigParser()
        cf.read(path)
        value = cf.get(section,option)
        return value


