# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/3 16:39
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_login_main.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import HTMLTestRunner
from homework.homework_pageobject_siye.TestCases.test_login import TestLogin
import unittest
import time
from homework.homework_pageobject_siye.Common.projectpath import *


if __name__ =='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
        # 执行测试集合
    filePath = os.path.join(TestReport_path,"前程贷登录模块测试报告" + now + ".html")
    fp = open(filePath, 'wb')
        # 生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='前程贷登录模块测试报告', description='前程贷登录模块测试报告')
    runner.run(suite)
    fp.close()