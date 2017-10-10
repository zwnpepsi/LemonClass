import unittest
from Lemonclass.a928课堂练习 import Math
from parameterized import parameterized

class TestMath(unittest.TestCase):

     @parameterized.expand([
     ("01",1,1,2),
     ("02",2,2,4),
     ("03",3,3,6),
     ])

     def setUp(self):
        pass

     def test_sum(self,name,a,b,c):
        print(type(Math(a,b).sum()))
        self.addTypeEqualityFunc(Math(a,b).sum(),c,"加法计算错误")
        print("测试数据是",name)

     def test_sub(self,name,a,b,c):
        self.addTypeEqualityFunc(Math(c,b).sub(),a,"减法计算错误")
        print("测试数据是", name)

     def tearDown(self):
        pass




