# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/7 22:14
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : recharge.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from Shizhan.public.http_request import HttpRequest
from Shizhan.public.read_data import ReadData
from Shizhan.public.write_data import WriteData
import time
import configparser
from Shizhan.conf import projectpath
from Shizhan.public.read_mode import ReadMode

class Recharge:
    def __init__(self,result,mode,case_list):
        self.result = result
        self.http_request_obj = HttpRequest("../../conf/http.conf")  # 生成一个http请求实例
        self.write_result = WriteData("recharge")
        self.mode=mode
        self.case_list=case_list


    def recharge(self):
        if self.mode==1:
            for i in range(len(self.result)):
                test_data = self.result[i]  # 对列表的每个元素进行拆分，拆分后又是列表格式
                url = test_data[0]
                mobile = str(int(test_data[1]))
                amount = int(test_data[2])
                http_method = test_data[3].upper()  # 加自带函数自动全部大写进行判断
                recharge_data = {"mobilephone": mobile, "amount": amount}

                if http_method == "GET":
                    request_result = self.http_request_obj.get(url, recharge_data)
                elif http_method == "POST":
                    request_result = self.http_request_obj.post(url, recharge_data)
                else:
                    print("请求数据错误")
                self.write_result.writeData(i, str(request_result))
            now = time.strftime('%Y-%m-%d_%H_%M_%S')
            self.write_result.saveData("../../Results/test_result/recharge_result" + now + ".xls")

        else:
            for i in self.case_list:
                test_data = self.result[i]  # 对列表的每个元素进行拆分，拆分后又是列表格式
                url = test_data[0]
                mobile = str(int(test_data[1]))
                amount = int(test_data[2])
                http_method = test_data[3].upper()  # 加自带函数自动全部大写进行判断
                recharge_data = {"mobilephone": mobile, "amount": amount}

                if http_method == "GET":
                    request_result = self.http_request_obj.get(url, recharge_data)
                elif http_method == "POST":
                    request_result = self.http_request_obj.post(url, recharge_data)
                else:
                    print("请求数据错误")
                self.write_result.writeData(i, str(request_result))
            now = time.strftime('%Y-%m-%d_%H_%M_%S')
            self.write_result.saveData("../../Results/test_result/recharge_result" + now + ".xls")









result = ReadData("../../test_data/recharge_data.xlsx").getData()
run_result = Recharge(result)
run_result.recharge()
