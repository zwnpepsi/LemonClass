# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/9 21:38
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : projectpath.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import os
from homework.homework_appium_pytest_siye.Common.read_config import ReadConfig

config_file_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]   #获取该文件绝对路径地址

#根据配置文件读取当前项目所在的绝对路径
project_path = ReadConfig().readConfig(os.path.join(config_file_path,"Common","project.conf"),"PROJECT_PATH","project_path")
#截图所在路径
image_path=os.path.join(project_path,"Images")

#测试报告所在路径
TestReport_path=os.path.join(project_path,"TestReport")


