# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/29 23:51
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : save_myqsl.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import mysql.connector
import  configparser
from homework.homework_1028_excel_nationalday_config.readexcel import ReadExcel

class SaveMysql:
    def __init__(self,result):
        self.result=result

    def save_Mysql(self):
        # 进行实例化
        cf = configparser.ConfigParser()
        # 读取配置文件
        cf.read("config.conf", encoding="utf-8")  # 自带Read函数读取
        cnn = mysql.connector.connect(**eval(cf.get("Mysql", "config")))
        cursor = cnn.cursor()
        sql_create_table = "create table test_case_result(\
            id int DEFAULT null PRIMARY key auto_increment,\
            status INT ,\
            code VARCHAR(10),\
            data1 VARCHAR(100)\
        )DEFAULT CHARSET=utf8;"
        cursor.execute(sql_create_table)

        for i in range(len(self.result)):
            result_data = self.result[i]  # 对列表的每个元素进行拆分，拆分后又是列表格式
            status = result_data['status']
            code = result_data['code']
            data = result_data['data']
            dict=(status,code,data)
            sql_insert="insert into test_case_result(status,code,data1) values(%s,%s,%s)"
            cursor.execute(sql_insert,dict)
        cursor.close()
        cnn.close()

#测试代码
result=ReadExcel("config.conf").read_excel()
print(type(result))
print(result)
# a=SaveMysql(result)
# a.save_Mysql()