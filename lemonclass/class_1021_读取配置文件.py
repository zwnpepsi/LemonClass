# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/21 15:45
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : class_1021_读取配置文件.py.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import  configparser
#进行实例化
cf=configparser.ConfigParser()
#读取配置文件
cf.read("class_1021_config.conf",encoding="utf-8")   #自带Read函数读取
print(cf.sections())
print(cf.options("Mysql"))
age=cf.get("STUDENT","age")
print(age)

age1=cf["STUDENT"]["age"]     #固定格式读取  cf[section][option]
print(age1)


age2=cf.getint("STUDENT","age")       #强制整型读取
print(age2)

dict=eval(cf.get("Dict","dict"))
print(type(dict))
print(dict)

list=cf["List"]["list"]
print(type(eval(list)))
print(list)