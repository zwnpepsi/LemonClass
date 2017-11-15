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
from Shizhan.public.test_interface import TestInterface
import unittest
import os
import HTMLTestRunner

class Recharge:
    def __init__(self,result,logger):
        self.logger = logger
        self.result = result
        self.http_request_obj = HttpRequest(projectpath.httpconf_path,self.logger)  # 生成一个http请求实例
        self.write_result = WriteData("recharge",self.logger,["序号","status","code","request_data","result_data","msg","description","result"])

    def recharge(self):
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        suite = unittest.TestSuite()
        for i in range(len(self.result)):
            test_data = self.result[i]  # 对列表的每个元素进行拆分，拆分后又是列表格式
            url = test_data[2]
            if test_data[3]=='':
                mobile = test_data[3]
            else:
                mobile = int(test_data[3])

            if test_data[4]=='':
                amount = test_data[4]
            elif str(test_data[4]).isdigit():
                amount = float(test_data[4])
            elif str(test_data[4]).isalpha():
                amount = test_data[4]
            else:
                amount = test_data[4]
            http_method = test_data[5].upper()    # 加自带函数自动全部大写进行判断
            request_method=test_data[1]
            expected=test_data[6]
            description=test_data[7]
            recharge_data = {"mobilephone": mobile, "amount": amount}

            suite.addTest(TestInterface(request_method,recharge_data,self.logger,i,self.http_request_obj,self.write_result,http_method,url,test_data,description,expected))

        filePath = os.path.join(projectpath.report_path, "充值接口测试结果" + now + ".html")
        fp = open(filePath, 'wb+')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="充值接口测试结果", verbosity=2)
        runner.run(suite)
        fp.close()
        recharge_result=projectpath.testresult_path+"\\充值接口测试结果" + now + ".xls"
        self.write_result.saveData(recharge_result)
        return filePath

#测试代码
# logger=CollectLog("充值操作").collectLog()
# result = ReadData(projectpath.testdata_path+"\\recharge_data.xlsx","RECHARGE_MODE","RECHARGE_CASELIST",logger).getData()
# run_result = Recharge(result,logger)
# run_result.recharge()
