# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/29 21:29
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : run_mysql.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from homework.homework_1028_excel_nationalday_config.httprequest import HttpRequest
from homework.homework_1028_excel_nationalday_config.readexcel import ReadExcel
from homework.homework_1028_excel_nationalday_config.write_mysql import WriteMysql
from homework.homework_1028_excel_nationalday_config.read_mysql import ReadMysql

class RunMysql:
    def __init__(self,result):
        self.result=result
        self.http_request_obj = HttpRequest("http://119.23.241.154:8080")  # 生成一个http请求实例
        self.write_result=WriteMysql()

    def run_mysql(self):
        for i in range(len(self.result)):
            test_data = self.result[i]  # 对列表的每个元素进行拆分，拆分后又是列表格式
            url = test_data[1]
            mobile = test_data[2]
            amount = test_data[3]
            http_method = test_data[4]
            recharge_data = {"mobilephone": mobile, "amount": amount}
            global request_result
            if http_method == "GET":
                request_result = self.http_request_obj.get(url, recharge_data)
            elif http_method == "POST":
                request_result = self.http_request_obj.post(url, recharge_data)
            else:
                print("请求数据错误")
            self.write_result.save_Mysql(request_result)


write=WriteMysql()
write.write_Mysql(ReadExcel("config.conf").read_excel())
result=ReadMysql("test_case").read_Mysql()
run_result=RunMysql(result)
run_result.run_mysql()
