# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/7 22:14
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : recharge.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import time
from Shizhan.public.http_request import HttpRequest
from Shizhan.public.read_data import ReadData
from Shizhan.public.write_data import WriteData
from Shizhan.public import projectpath
from Shizhan.public.collect_log import CollectLog


class Recharge:
    def __init__(self,result,logger):
        self.logger = logger
        self.result = result
        self.http_request_obj = HttpRequest(projectpath.httpconf_path,self.logger)  # 生成一个http请求实例
        self.write_result = WriteData("recharge",self.logger)

    def recharge(self):
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
        recharge_result=projectpath.testresult_path+"\\recharge_result" + now + ".xls"
        self.write_result.saveData(recharge_result)
        return recharge_result

# logger=CollectLog("充值操作").collectLog()
# result = ReadData(projectpath.testdata_path+"\\recharge_data.xlsx","RECHARGE_MODE","RECHARGE_CASELIST",logger).getData()
# run_result = Recharge(result,logger)
# run_result.recharge()
