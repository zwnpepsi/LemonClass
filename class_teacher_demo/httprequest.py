__author__ = '来自Jayden同学的代码'

import requests

class HttpRequest:

    def __init__(self,ip):
        self.ip=ip

    def get(self,url,data):
        url = self.ip+url
        try:
            rget = requests.get(url,data)
            return rget.text
        except Exception as e:
            print('出错啦！错误参数是：%s'%e)

    def post(self,url,data):
        url = self.ip+url
        try:
            rpost = requests.post(url,data)
            return  rpost.text
        except Exception as e:
            print('出错啦！错误参数是：%s'%e)
