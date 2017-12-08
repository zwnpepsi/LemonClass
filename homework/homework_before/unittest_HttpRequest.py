#-*-coding:utf-8-*-
from homework.homework_before.HttpRequestDemo import HttpRequest
import unittest
import json
from homework.homework_before.logger_1012作业_四葉 import CollectLog

class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        # pass
        self.logger=CollectLog().Collection()
        self.logger.info("测试开始" )


    def test_get(self,url='/futureloan/mvc/api/member/recharge',data={'mobilephone':'13667692121','amount':1000}):
        try:
            http_re = HttpRequest('http://119.23.241.154:8080')
            get_result=http_re.get(url,data)
            self.assertEqual(json.loads(get_result)["code"], "10001", "充值报错")
        except AssertionError as e:
            self.logger.error ('出错啦！错误参数是：%s' % e)
            raise AssertionError
        else:
            self.logger.info("充值测试通过")

    def test_post(self,url='/futureloan/mvc/api/member/register',data={'mobilephone':'18010073801','pwd':'123456'}):
        try:
            http_re = HttpRequest('http://119.23.241.154:8080')
            post_result=http_re.post(url,data)
            self.assertEqual(json.loads(post_result)["code"], "10001", "注册报错")
        except AssertionError as e:
            self.logger.error ('出错啦！错误参数是：%s' % e)
            raise AssertionError
        else:
            self.logger.info("注册测试通过")

    def tearDown(self):
        # pass
        self.logger.info("测试结束")


if __name__ =='__main__':
        unittest.main()

# log=CollectLog()
# log.Collection()
