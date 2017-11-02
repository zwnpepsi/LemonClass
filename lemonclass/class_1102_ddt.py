# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/2 21:34
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : class_1102_ddt.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from ddt import ddt,data,unpack
import unittest
from homework.homework_1024_excel_nationalday.readexcel import ReadExcel
a=ReadExcel()
result=a.read_excel()
@ddt
class TestDdt(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    @data(1,2,3)
    def test_ddt1(self,a):
        print("运行单元测试test_ddt1的值为：%s"%a)

    @data([1,2],[3,4])
    def test_ddt2(self, a):
        print("运行单元测试test_ddt2的值为：%s" %a)

    @data([1,2],[3,4])
    @unpack
    def test_ddt3(self, a,b):
        print("运行单元测试test_ddt3的值为：",a,b)

    @data([{"name":"siye","age":18},{"name":"huahua","age":16}])
    @unpack
    def test_ddt4(self, a,b):
        print("运行单元测试test_ddt4的值为：", a,b)

    @data(*result)
    @unpack
    def test_ddt5(self, a,b,c,d):
        print("从Excel中获取的数据为：",a,str(int(b)),int(c),d)

    def tearDown(self):
        print("测试结束")


if __name__ =='__main__':
        unittest.main()