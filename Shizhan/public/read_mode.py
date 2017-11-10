# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/9 22:10
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : read_mode.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import configparser

class ReadMode:
    def __init__(self,path,mode_option,caselist_option):
        cf = configparser.ConfigParser()
        cf.read(path)  # code_config地址还没写
        self.mode = cf.getint("FLAG", mode_option)
        self.case_list = eval(cf.get("FLAG", caselist_option))

    def getMode(self):
        return self.mode

    def getCase_list(self):
        return self.case_list

