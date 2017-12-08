# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/2 22:47
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : home_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from homework.homework_pageobject_siye.Common.elements_locator import *

class HomePage:

    def __init__(self,driver):
        self.driver = driver

    #点击页面上方投标按钮
    def click_bidButton(self):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, home_bid_button_locator)))  # 判断元素加载完成
        home_bidButton_ele = self.driver.find_element_by_xpath(home_bid_button_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", home_bidButton_ele)
        home_bidButton_ele.click()

    #通过传入标名点击该标名下方的抢投标按钮
    def click_bidGrabLink_bybidName(self,bid_name):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, home_bid_grad_locator %bid_name)))  # 判断元素加载完成
        home_bidGrab_ele=self.driver.find_element_by_xpath(home_bid_grad_locator %bid_name)
        self.driver.execute_script("arguments[0].scrollIntoView();", home_bidGrab_ele)
        home_bidGrab_ele.click()

    #通过传入标名点击该标名按钮
    def click_bidName(self,bid_name):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_all_elements_located((By.XPATH, home_bid_name_locator %bid_name)))  # 判断元素加载完成
        home_bidName_ele = self.driver.find_element_by_xpath(home_bid_name_locator % bid_name)
        home_bidName_ele.click()

    #点击明星蜂群按钮
    def click_starHiveButton(self):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, home_starHive_button_locator)))  # 判断元素加载完成
        home_tarHiveButton_ele = self.driver.find_element_by_xpath(home_starHive_button_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", home_tarHiveButton_ele)
        home_tarHiveButton_ele.click()

    #通过传入的蜂群名称点击该蜂群链接
    def click_starHiveLink_byhiveName(self,hive_name):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, home_starHive_locator %hive_name)))  # 判断元素加载完成
        home_starHive_locator_ele=self.driver.find_element_by_xpath(home_starHive_locator %hive_name)
        self.driver.execute_script("arguments[0].scrollIntoView();", home_starHive_locator_ele)
        home_starHive_locator_ele.click()

    #获取昵称
    def get_nickname(self):
        WebDriverWait(self.driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, home_myAccount_locator)))  # 判断元素出现
        return self.driver.find_element_by_xpath(home_myAccount_locator).text

    #打开我的账户页面
    def click_myaccount(self):
        WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, home_myAccount_locator)))  # 判断元素加载完成
        home_myAccount_locator_ele = self.driver.find_element_by_xpath(home_myAccount_locator)
        # self.driver("arguments[0].scrollIntoView();", home_myAccount_locator_ele)
        home_myAccount_locator_ele.click()

