# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/2 22:48
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : tenderInfo_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from homework.homework_pageobject_siye.Common.elements_locator import *


class TenderInfoPage:

    def __init__(self,driver):
        self.driver = driver

    #正常投标函数
    def bid_normal(self,amount):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, tenderInfo_num_locator)))  # 判断元素加载完成
        self.driver.find_element_by_xpath(tenderInfo_num_locator).send_keys(amount)
        self.driver.find_element_by_xpath(tenderInfo_bidButton_locator).click()
        tender_date = time.strftime('%Y-%m-%d')
        tender_time = time.strftime('%H:%M')
        return tender_date,tender_time

    #非10倍数进行投标函数
    def bid_normal_no10xNum(self,amount):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, tenderInfo_num_locator)))  # 判断元素加载完成
        self.driver.find_element_by_xpath(tenderInfo_num_locator).send_keys(amount)
        WebDriverWait(self.driver, 5, 1).until(EC.visibility_of_element_located((By.XPATH, tenderInfo_bidButton_locator)))  # 判断元素加载完成
        return self.driver.find_element_by_xpath(tenderInfo_bidButton_locator).text    #获取按钮上文字信息

    #勾选全投进行投标函数
    def bid_allBid(self):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, tenderInfo_num_locator)))  # 判断元素加载完成
        self.driver.find_element_by_xpath(tenderInfo_allBid_locator).click()
        self.driver.find_element_by_xpath(tenderInfo_bidButton_locator).click()

    #获取投标成功提示信息
    def get_success_info(self):
        WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, tenderInfo_success_info_locator)))  # 判断投标成功界面显示文字完成
        return self.driver.find_element_by_xpath(tenderInfo_success_info_locator).text

    #获取投标失败提示信息
    def get_error_info(self):
        WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, tenderInfo_error_info_locator )))  # 判断投标失败提示显示文字完成
        return self.driver.find_element_by_xpath(tenderInfo_error_info_locator ).text

    #获取完整标名
    def get_bid_name(self):
        WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, tenderInfo_bidName_locator)))  # 判断投标失败提示显示文字完成
        return self.driver.find_element_by_xpath(tenderInfo_bidName_locator).text

    #关闭投标成功提示
    def close_success_info(self):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, tenderInfo_success_close_locator)))  # 判断元素加载完成
        self.driver.find_element_by_xpath(tenderInfo_success_close_locator).click()
