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
    def __init__(self,methodName,recharge_data ,logger,i,http_request_obj,write_result,http_method):
        super(TestInterface,self).__init__(methodName)
        self.recharge_data =recharge_data
        self.logger=logger
        self.i=i
        self.http_request_obj=http_request_obj
        self.write_result=write_result
        self.http_method=http_method


    def setUp(self):
        pass


    def test_recharge(self):
        pass

    def test_register(self):
        pass


    def tearDown(self):
        pass