# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/14 21:12
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_interface.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import unittest

class TestInterface(unittest.TestCase):
    def __init__(self,methodName,recharge_data,logger,i,http_request_obj,write_result,http_method,url,test_data,description,expected):
        super(TestInterface,self).__init__(methodName)
        self.recharge_data =recharge_data
        self.logger=logger
        self.i=i
        self.http_request_obj=http_request_obj
        self.write_result=write_result
        self.http_method=http_method
        self.url=url
        self.test_data=test_data
        self.description=description
        self.expected=expected

    def setUp(self):
        self.logger.info("单元测试开始啦！")

    def test_recharge(self):
        global result
        global response
        if self.http_method == "GET":
            try:
                response = self.http_request_obj.get(self.url, self.recharge_data)
                self.assertEqual(response['code'], str(int(self.expected)), "充值失败")
            except Exception as e:
                result = "FAIL"
                self.logger.error("充值单元测试失败，错误原因为: %s" % e)
                raise e
            else:
                self.logger.info("充值单元测试成功")
                result="PASS"

        elif self.http_method == "POST":
                try:
                    response = self.http_request_obj.post(self.url, self.recharge_data)
                    self.assertEqual(response['code'], str(int(self.expected)), "充值失败")
                except Exception as e:
                    result = "FAIL"
                    self.logger.error("充值单元测试失败，错误原因为: %s" % e)
                    raise e
                else:
                    self.logger.info("充值单元测试成功")
                    result = "PASS"
        else:
            print("请求数据错误")
        self.write_result.writeData(self.i, response,self.test_data,self.description,result)

    def test_register(self):
        pass


    def tearDown(self):
        self.logger.info("单元测试结束啦！")