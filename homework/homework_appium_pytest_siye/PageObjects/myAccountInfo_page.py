# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/2 22:48
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : myAccountInfo_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from homework.homework_appium_pytest_siye.Common.elements_locator import *
import re


class MyAccountInfoPage:

    def __init__(self,driver):
        self.driver = driver

    #获取我的昵称
    def get_nickname(self):
        nickname = self.driver.find_element_by_id(myAccount_nickname_locator).text
        return nickname

    #退出登录
    def logout(self):
        self.driver.find_element_by_id(myAccount_option_locator).click()
        self.driver.find_element_by_id(myAccount_logout_locator).click()
        self.driver.find_element_by_id(myAccount_confirm_logout_locator).click()

    #获取余额
    def get_balance(self):
        balance = self.driver.find_element_by_xpath(myAccount_balance_locator).get_attribute('text')
        balance = int(int(re.sub("\D", "", balance)) / 100)
        return balance

    #点击"项目"按钮进入项目页面
    def click_projectButton(self):
        self.driver.find_element_by_xpath(home_project_locator).click()

    #点击"首页"进入首页页面
    def click_homeButton(self):
        self.driver.find_element_by_xpath(myAccount_home_locator).click()

    #点击"我的投资"进入我的投资页面
    def click_mytenderButton(self):
        self.driver.find_element_by_xpath(myAccount_mytender_locator).click()




