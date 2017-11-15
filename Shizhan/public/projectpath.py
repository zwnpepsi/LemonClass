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

config_file_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]   #获取该文件绝对路径地址

#根据配置文件读取当前项目所在的绝对路径
cf=configparser.ConfigParser()
cf.read(os.path.join(config_file_path,"conf","project.conf"))
project_path=cf.get("PROJECT_PATH","project_path")

#测试数据所在路径
testdata_path=os.path.join(project_path,"test_data")

#测试结果所在路径
testresult_path=os.path.join(project_path,"Results","test_result")

#测试结果集所在路径
Results_path=os.path.join(project_path,"Results")

#http.conf所在路径
httpconf_path=os.path.join(project_path,"conf","http.conf")

#flag.conf所在地址
flag_path=os.path.join(project_path,"conf","flag.conf")

#smtp.conf所在地址
smtp_path=os.path.join(project_path,"conf","smtp.conf")

#report存放地址
report_path=os.path.join(project_path,"Results","report")