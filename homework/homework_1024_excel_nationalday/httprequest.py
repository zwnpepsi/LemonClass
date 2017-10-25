# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/25 14:29
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : httprequest.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import requests
import logging

class HttpRequest:
    def __init__(self,ip):
        self.ip = ip

    def get(self,url,data):
        url = self.ip+url
        try:
            rget = requests.get(url,data)
            return rget.text
        except Exception as e:
            logging.error('出错啦！错误参数是：%s'%e)

    def post(self,url,data):
        url = self.ip+url
        try:
            rpost = requests.post(url,data)
            return rpost.text
        except Exception as e:
            logging.error('出错啦！错误参数是：%s'%e)