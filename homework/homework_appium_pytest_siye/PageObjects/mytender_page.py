# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/2 22:48
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : mytender_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from homework.homework_appium_pytest_siye.Common.elements_locator import *
import re
import datetime


class MyTenderPage:

    def __init__(self,driver):
        self.driver = driver

    #点击最上面一条投资记录
    def click_firsttender(self):
        self.driver.find_element_by_id(mytender_firsttender_locator).click()

    #标详情界面点击投资记录按钮
    def click_tenderlistButton(self):
        self.driver.find_element_by_id(mytender_tenderlist_locator).click()

    #获取投资记录内最新一个记录的时间，投资人，投资金额信息
    def get_tenderinfo(self):
        investor = self.driver.find_element_by_id(tendelist_investor_locator).get_attribute('text')
        tender_time=self.driver.find_element_by_id(tendelist_time_locator).get_attribute('text')
        tender_amount = self.driver.find_element_by_id(tendelist_amount_locator).get_attribute('text')
        tender_amount = int(re.sub("\D", "", tender_amount))
        return [investor,tender_amount,tender_time]

    #计算时间差多少秒的函数
    def sub_seconds(self,before_time,after_time):

        starttime = datetime.datetime.strptime(before_time, '%m-%d %H:%M:%S')
        endtime = datetime.datetime.strptime(after_time, '%m-%d %H:%M:%S')
        return (endtime-starttime).seconds
