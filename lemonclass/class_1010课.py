import unittest
from lemonclass.class_928课堂练习 import Math
from parameterized import parameterized

class TestMath(unittest.TestCase):

     @parameterized.expand([
     ("第一条",1,1,2),
     ("第二条",2,2,4),
     ("第三条",3,3,6),
     ])

     def setUp(self):
         pass

     def test_sum(self,name,a,b,c):
         t=Math(a,b)
         result1=t.sum()
         self.addTypeEqualityFunc(a+b,c,"加法计算错误")
         print("测试数据是",name)

     @parameterized.expand([
         ("01", 1, 1, 2),
         ("02", 2, 2, 4),
         ("03", 3, 3, 6),
     ])
     def test_sub(self,name,a,b,c):
         s=Math(c,b)
         result2=s.sub()
         self.addTypeEqualityFunc(c-b,a,"减法计算错误")
         print("测试数据是", name)

     def tearDown(self):
         pass





