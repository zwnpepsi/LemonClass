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
         self.addTypeEqualityFunc(result1,c,"加法计算错误")
         print("测试数据是",name)

     def test_sub(self,name,a,b,c):
         s=Math(c,b)
         result2=s.sub()
         self.addTypeEqualityFunc(result2,a,"减法计算错误")
         print("测试数据是", name)

     def tearDown(self):
         pass


     if __name__ =='__main__':
        unittest.main()


