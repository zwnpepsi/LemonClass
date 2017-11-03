# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/25 16:09
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_run.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from homework.homework_1102_ddt.httprequest import HttpRequest
from homework.homework_1102_ddt.readexcel import ReadExcel
from homework.homework_1102_ddt.writeexcel import WriteExcel
from ddt import ddt,data,unpack
import unittest
import time
import HTMLTestRunner

result=ReadExcel("config.conf").read_excel()
http_request_obj = HttpRequest("http://119.23.241.154:8080")
write_result=WriteExcel()

@ddt
class TestRun(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    @data(*result)
    @unpack
    def test_run(self,i,url,mobilephone,amount,method,expected):
        try:
            recharge_data = {"mobilephone": str(int(mobilephone)), "amount": int(amount)}
            if method == "GET":
                request_result = http_request_obj.get(url, recharge_data)
                self.assertEqual(request_result['code'],str(int(expected)),"充值失败")
            elif method == "POST":
                request_result = http_request_obj.post(url, recharge_data)
                self.assertEqual(request_result['code'], str(int(expected)), "充值失败")
            else:
                print("请求数据错误")
        except AssertionError as e:
            print("充值接口出现异常：%s"%e)
        finally:
            write_result.write_excel(int(i)-1,str(request_result))
            write_result.save_excel()

    def tearDown(self):
        print("测试结束")

if __name__ =='__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(TestRun('test_run'))
    # now = time.strftime('%Y-%m-%d_%H_%M_%S')
    # # 执行测试集合
    # filePath = "pyResult" + now + ".html"
    # fp = open(filePath, 'wb')
    # # 生成报告的Title,描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Python Test Report', description='This  is Python  Report')
    # runner.run(suite)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRun)
    unittest.TextTestRunner().run(suite)

