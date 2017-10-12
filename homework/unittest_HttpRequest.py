#-*-coding:utf-8-*-
from homework.HttpRequestDemo import HttpRequest
import unittest
import json


class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        print("测试开始" )
        pass

    def tearDown(self):
        print("测试结束")
        pass

    def test_get(self,url='/futureloan/mvc/api/member/recharge',data={'mobilephone':'13667692121','amount':1000}):
        try:
            http_re = HttpRequest('http://119.23.241.154:8080')
            get_result=http_re.get(url,data)
            self.assertEqual(json.loads(get_result)["code"], "10001", "充值报错")

        except Exception as e:
            print ('出错啦！错误参数是：%s' % e)

        else:
            print("充值测试通过")



    def test_post(self,url='/futureloan/mvc/api/member/register',data={'mobilephone':'18010073801','pwd':'123456'}):
        try:
            http_re = HttpRequest('http://119.23.241.154:8080')
            post_result=http_re.post(url,data)
            # print(post_result)
            self.assertEqual(json.loads(post_result)["code"], "10001", "注册报错")

        except Exception as e:
            print ('出错啦！错误参数是：%s' % e)

        else:
            print("注册测试通过")

if __name__ =='__main__':
        unittest.main()