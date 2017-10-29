# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/25 16:09
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : run.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from homework.homework_1028_excel_nationalday_config.httprequest import HttpRequest
from homework.homework_1028_excel_nationalday_config.readexcel import ReadExcel
from homework.homework_1028_excel_nationalday_config.writeexcel import WriteExcel
import  configparser
class Run:
    def __init__(self,result):
        self.result=result
        self.http_request_obj = HttpRequest("http://119.23.241.154:8080")  # 生成一个http请求实例
        self.write_result=WriteExcel()

    def run(self):
        for i in range(len(self.result)):
            test_data = self.result[i]  # 对列表的每个元素进行拆分，拆分后又是列表格式
            url = test_data[0]
            mobile = str(int(test_data[1]))
            amount = int(test_data[2])
            http_method = test_data[3]
            recharge_data = {"mobilephone": mobile, "amount": amount}
            if http_method == "GET":
                request_result = self.http_request_obj.get(url, recharge_data)
            elif http_method == "POST":
                request_result = self.http_request_obj.post(url, recharge_data)
            else:
                print("请求数据错误")
            self.write_result.write_excel(i,request_result)
        self.write_result.save_excel()

result=ReadExcel("config.conf").read_excel()
run_result=Run(result)
run_result.run()
