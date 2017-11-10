# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/7 21:26
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : http_request.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import requests
import logging
import configparser



class HttpRequest:
    def __init__(self,http_config,logger):
        self.config = http_config
        self.logger=logger
        cf = configparser.ConfigParser()
        # 读取配置文件
        cf.read(self.config, encoding="utf-8")
        self.ip = cf["HTTP"]["ip"]+":"+cf["HTTP"]["port"]

    def get(self,url,data):
        url = self.ip+url
        try:
            rget = requests.get(url,data)
            self.logger.info("get请求成功")
            return rget.json()
        except Exception as e:
            self.logger.error('出错啦！错误参数是：%s'%e)

    def post(self,url,data):
        url = self.ip+url
        try:
            rpost = requests.post(url,data)
            self.logger.info("post请求成功")
            return rpost.json()
        except Exception as e:
            self.logger.error('出错啦！错误参数是：%s'%e)