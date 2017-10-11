import unittest
from lemonclass.class_928课堂练习 import Math
from ddt import ddt,data,unpack

@ddt
class TestMath(unittest.TestCase):

     def setup(self):
         pass

     @data([ 1, 1, 2], [ 2, 2, 4], [ 3, 3, 6])
     @unpack

     def test_sum(self,first,second,third):
         t=Math(first,second)
         result1=t.sum()
         self.assertEqual(result1,third,"加法报错")
         #print("测试数据是",name)

     @data([1, 1, 2], [2, 2, 4], [3, 3, 6])
     @unpack
     def test_sub(self,first,second,third):
         s=Math(third,second)
         result2=s.sub()
         self.assertEqual(result2,first,"减法报错")
         #print("测试数据是", name)


     def teardown(self):
         print("this is the down")

if __name__ =='__main__':
        unittest.main()



