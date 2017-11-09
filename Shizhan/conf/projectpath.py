# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/9 21:38
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : projectpath.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import os
import  configparser

config_file_path=os.path.split(os.path.realpath(__file__))[0]     #获取该文件绝对路径地址
# print(config_file_path)

#根据配置文件读取当前项目所在的绝对路径
cf=configparser.ConfigParser()
cf.read(os.path.join(config_file_path),"project.conf")

project_path=cf.get("PROJECT_PATH","project_path")


#测试数据所在路径
testdata_path=os.path.join(project_path,"test_data")