# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/29 21:29
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : write_mysql.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from homework.homework_1028_excel_nationalday_config.readexcel import ReadExcel
import mysql.connector
import  configparser

class WriteMysql:
    def __init__(self):
        pass

    def write_Mysql(self,excel_contents):
        # 进行实例化
        cf = configparser.ConfigParser()
        # 读取配置文件
        cf.read("config.conf", encoding="utf-8")  # 自带Read函数读取
        cnn = mysql.connector.connect(**eval(cf.get("Mysql", "config")))
        cursor = cnn.cursor(buffered=True)

        judge_sql="select TABLE_NAME from information_schema.tables WHERE TABLE_NAME ='test_case'"   #检查是否存在这个数据库，对是否存在进行判断，然后进行后续操作
        cursor.execute(judge_sql)
        judge_result = cursor.fetchall()
        if judge_result==[]:        #test_case表不存在
            sql_create_table = "create table test_case(\
                        id int DEFAULT null PRIMARY key auto_increment,\
                        url varchar(100),\
                        mobilephone VARCHAR(11),\
                        amount INT ,\
                        http_method VARCHAR(10)\
                    )DEFAULT CHARSET=utf8;"
            cursor.execute(sql_create_table)                   #建立test_case表
            for i in range(len(excel_contents)):
                test_data = excel_contents[i]  # 对列表的每个元素进行拆分，拆分后又是列表格式
                url = test_data[0]
                mobile = str(int(test_data[1]))
                amount = int(test_data[2])
                http_method = test_data[3]
                b=(url,mobile,amount,http_method)
                sql_insert="insert into test_case(url,mobilephone,amount,http_method) values(%s,%s,%s,%s)"
                cursor.execute(sql_insert,b)                            #把excel读出的数据写入test_case表
            cursor.close()
            cnn.close()
        else:                                     #test_case表存在 ,直接写入excel读出的数据
            for i in range(len(excel_contents)):
                test_data = excel_contents[i]  # 对列表的每个元素进行拆分，拆分后又是列表格式
                url = test_data[0]
                mobile = str(int(test_data[1]))
                amount = int(test_data[2])
                http_method = test_data[3]
                b=(url,mobile,amount,http_method)
                sql_insert="insert into test_case(url,mobilephone,amount,http_method) values(%s,%s,%s,%s)"
                cursor.execute(sql_insert,b)
            cursor.close()
            cnn.close()


    def save_Mysql(self,http_result):
        # 进行实例化
        cf = configparser.ConfigParser()
        # 读取配置文件
        cf.read("config.conf", encoding="utf-8")  # 自带Read函数读取
        cnn = mysql.connector.connect(**eval(cf.get("Mysql", "config")))
        cursor = cnn.cursor()
        judge_sql = "select TABLE_NAME from information_schema.tables WHERE TABLE_NAME ='test_case_result'"  # 检查是否存在这个数据库，对是否存在进行判断，然后进行后续操作
        cursor.execute(judge_sql)
        judge_result = cursor.fetchall()
        if judge_result == []:  # test_case表不存在
            sql_create_table = "create table test_case_result(\
            id int DEFAULT null PRIMARY key auto_increment,\
            status INT ,\
            code VARCHAR(10),\
            msg VARCHAR (10),\
            data VARCHAR(300)\
            )DEFAULT CHARSET=utf8;"
            cursor.execute(sql_create_table)
            result_data = eval(http_result)  # 对列表的每个元素进行拆分，拆分后又是列表格式
            status = result_data['status']
            code = result_data['code']
            data = str(result_data['data'])
            msg  = result_data['msg']
            tuple=(status,code,msg,data)
            sql_insert="insert into test_case_result(status,code,msg,data) values(%s,%s,%s,%s)"
            cursor.execute(sql_insert,tuple)
            cursor.close()
            cnn.close()
        else:
            result_data = eval(http_result)  # 对列表的每个元素进行拆分，拆分后又是列表格式
            status = result_data['status']
            code = result_data['code']
            data = str(result_data['data'])
            msg = result_data['msg']
            tuple = (status, code, msg,data)
            sql_insert = "insert into test_case_result(status,code,msg,data) values(%s,%s,%s,%s)"
            cursor.execute(sql_insert, tuple)
            cursor.close()
            cnn.close()
#测试代码
# a=WriteMysql()
# a.write_Mysql(ReadExcel("config.conf").read_excel())


