#-*-coding:utf-8-*-
from homework.HttpRequestDemo import HttpRequest
import unittest
import requests


class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get(self,url='/futureloan/mvc/api/member/recharge',data={'mobilephone':'13667692121','amount':1000}):
        try:
            http_re = HttpRequest('http://119.23.241.154:8080')
            get_result=http_re.get(url,data)
            self.assertEqual(get_result["code"], "10001", "充值报错")
            requests.adapters.DEFAULT_RETRIES = 5

        except Exception as e:
            print('出错啦！错误参数是：%s' % e)



    def test_post(self,url='/futureloan/mvc/api/member/register',data={'mobilephone':'13667692121','pwd':'987654321'}):
        try:
            http_re = HttpRequest('http://119.23.241.154:8080')
            post_result=http_re.post(url,data)
            self.assertEqual(post_result["code"], "10000", "注册报错")
            requests.adapters.DEFAULT_RETRIES = 5

        except Exception as e:
            print('出错啦！错误参数是：%s' % e)

if __name__ =='__main__':
        unittest.main()