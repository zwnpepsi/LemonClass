# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/2 22:46
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : login_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from homework.homework_appium_pytest_siye.Common.elements_locator import *
from appium import webdriver



class LoginPage:

    def __init__(self,driver):
        self.driver=driver

    def login(self,username,pwd):
        self.driver.find_element_by_id(login_phone_locator).send_keys(username)
        self.driver.find_element_by_id(login_afterphone_next_button_locator).click()
        self.driver.find_element_by_id(login_password_locator).send_keys(pwd)
        self.driver.find_element_by_id(login_confirm_locator).click()


