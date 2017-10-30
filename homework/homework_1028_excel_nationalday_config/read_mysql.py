# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/29 21:29
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : read_mysql.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import mysql.connector
import  configparser

class ReadMysql:
    def __init__(self,table):
        self.table=table

    def read_Mysql(self):
        # 进行实例化
        cf = configparser.ConfigParser()
        # 读取配置文件
        cf.read("config.conf", encoding="utf-8")  # 自带Read函数读取
        cnn = mysql.connector.connect(**eval(cf.get("Mysql", "config")))
        cursor = cnn.cursor(buffered=True)
        select = "select * from (%s)"%self.table  # 查询操作
        cursor.execute(select)
        result = cursor.fetchall()  # 输出列表类型数据
        cursor.close()
        cnn.close()
        return result

# 测试代码
# a=ReadMysql("test_case")
# a.read_Mysql()