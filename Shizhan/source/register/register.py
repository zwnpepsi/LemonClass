# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/7 22:18
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : register.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from Shizhan.public.http_request import HttpRequest
from Shizhan.public.read_data import ReadData
from Shizhan.public.write_data import WriteData

class Register:
    def __init__(self,result):
        self.result = result
        self.http_request_obj = HttpRequest("../../conf/http.conf")  # 生成一个http请求实例
        self.write_result = WriteData("register")

    def register(self):
        for i in range(len(self.result)):
            test_data = self.result[i]  # 对列表的每个元素进行拆分，拆分后又是列表格式
            mobile = str(int(test_data[0]))
            pwd = test_data[1]
            regname = test_data[2]
            url = test_data[3]

            register_data = {"mobilephone": mobile, "pwd": pwd,"regname":regname}
            request_result = self.http_request_obj.post(url, register_data)

            self.write_result.writeData(i,str(request_result))
        self.write_result.saveData("../../Results/test_result/register_result.xls")

result = ReadData("../../test_data/register_data.xls").getData()
run_result = Register(result)
run_result.register()