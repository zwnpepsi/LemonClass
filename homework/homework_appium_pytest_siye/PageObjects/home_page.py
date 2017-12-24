# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/2 22:47
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : home_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from appium import webdriver
from homework.homework_appium_pytest_siye.Common.elements_locator import *

class HomePage:

    def __init__(self,driver):
        self.driver = driver

    #点击页面右上角注册/登录按钮
    def click_loginButton(self):
        self.driver.find_element_by_id(home_login_locator).click()

    #点击登录成功提示开启手势密码提示框的以后再说按钮
    def click_cancelButton(self):
        self.driver.find_element_by_id(home_cancel_locator).click()

    #点击“我”按钮进入我的账户页面
    def click_meButton(self):
        self.driver.find_element_by_xpath(home_me_locator).click()

    #点击"项目"按钮进入项目页面
    def click_projectButton(self):
        self.driver.find_element_by_xpath(home_project_locator).click()

    #点击"精选项目"推荐的标
    def click_commendProjectMessage(self):
        self.driver.find_element_by_id(home_commendProjectMessage_locator).click()

    

