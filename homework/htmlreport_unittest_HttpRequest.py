import unittest
import time
import HTMLTestRunner
from homework.unittest_HttpRequest import TestHttpRequest

suite=unittest.TestSuite()
suite.addTest(TestHttpRequest('test_get'))
suite.addTest(TestHttpRequest('test_post'))
now = time.strftime('%Y-%m-%d_%H_%M_%S')
#执行测试集合
filePath = "pyResult"+now+".html"
fp = open(filePath,'wb')

#生成报告的Title,描述
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Python Test Report',description='This  is Python  Report')
runner.run(suite)
