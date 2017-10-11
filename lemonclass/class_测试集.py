import unittest
import time
import HTMLTestRunner
from ddt import ddt,data,unpack
from lemonclass.class_10102 import TestMath

suite=unittest.TestSuite()
suite.addTest(TestMath('test_sum'))
suite.addTest(TestMath('test_sub'))
now = time.strftime('%Y-%m-%d_%H_%M_%S')
#执行测试集合
filePath = "pyResult"+now+".html"
fp = open(filePath,'wb')

#生成报告的Title,描述
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Python Test Report',description='This  is Python  Report')
runner.run(suite)


