# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/2 22:48
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : myAccountInfo_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from homework.homework_pageobject_siye.Common.elements_locator import *


class MyAccountInfoPage:

    def __init__(self,driver):
        self.driver = driver

    #获取的我余额
    def get_balance(self):
        WebDriverWait(self.driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, myAccount_balance_locator)))  # 判断元素出现
        balance = self.driver.find_element_by_xpath(myAccount_balance_locator).text
        balance = int(int(re.sub("\D", "", balance))/100)
        return balance

    #获取已投标信息：日期，时间，名称
    def get_bidInfo(self):
        WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located((By.XPATH, myAccount_investment_locator)))  # 判断元素出现
        self.driver.find_element_by_xpath(myAccount_investment_locator).click()

        WebDriverWait(self.driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, myAccount_tender_seedate_locator)))  # 判断元素出现
        myAccount_tender_seedate=self.driver.find_element_by_xpath(myAccount_tender_seedate_locator).text
        myAccount_tender_seetime=self.driver.find_element_by_xpath(myAccount_tender_seetime_locator).text
        myAccount_tender_name=self.driver.find_element_by_xpath(myAccount_tender_name_locator).text
        return [myAccount_tender_seedate,myAccount_tender_seetime,myAccount_tender_name]

