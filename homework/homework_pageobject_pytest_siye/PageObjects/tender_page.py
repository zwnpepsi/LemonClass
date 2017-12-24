# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/4 0:01
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : project_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from homework.homework_pageobject_pytest_siye.Common.elements_locator import *


class TenderPage:

    def __init__(self,driver):
        self.driver = driver

    #正常投标操作
    def bid_normal(self,bid_name,amount):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, bidding_num_locator %bid_name)))  # 判断元素加载完成
        self.driver.find_element_by_xpath(bidding_num_locator %bid_name).send_keys(amount)
        self.driver.find_element_by_xpath(bidding_bidButton_locator %bid_name).click()
        tender_time = time.strftime('%Y-%m-%d %H:%M:%S')
        return tender_time

    #勾选全投进行投标操作
    def bid_allBid(self,bid_name):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, bidding_num_locator %bid_name)))  # 判断元素加载完成
        self.driver.find_element_by_xpath(bidding_allBid_locator %bid_name).click()
        self.driver.find_element_by_xpath(bidding_bidButton_locator %bid_name).click()

    #获取投标成功信息
    def get_success_info(self):
        WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, bidding_success_info_locator)))  # 判断投标成功界面显示文字完成
        return self.driver.find_element_by_xpath(bidding_success_info_locator).text

    #获取投标失败信息
    def get_error_info(self):
        WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, bidding_error_info_locator )))  # 判断投标成功界面显示文字完成
        return self.driver.find_element_by_xpath(bidding_error_info_locator ).text

    #获取完整标名
    def get_bid_name(self,bid_name):
        WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, bidding_bidName_locator %bid_name)))  # 判断投标失败提示显示文字完成
        return self.driver.find_element_by_xpath(bidding_bidName_locator %bid_name).text

    #关闭投标成功提示操作
    def close_success_info(self):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, bidding_success_close_locator)))  # 判断元素加载完成
        self.driver.find_element_by_xpath(bidding_success_close_locator).click()