# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/2 22:46
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : login_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from homework.homework_pageobject_siye.Common.elements_locator import *


class LoginPage:

    def __init__(self,driver):
        self.driver=driver

    def login(self,url,username,pwd):
        self.driver.get(url)
        WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, login_username_locator)))  # 判断登录按钮可见
        self.driver.find_element_by_xpath(login_username_locator).send_keys(username)
        self.driver.find_element_by_xpath(login_password_locator).send_keys(pwd)
        self.driver.find_element_by_xpath(login_button_locator).click()

    def get_username_info(self):
        WebDriverWait(self.driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, username_info_locator)))  # 判断元素出现
        return self.driver.find_element_by_xpath(username_info_locator).text

    def get_password_info(self):
        WebDriverWait(self.driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, password_info_locator)))  # 判断元素出现
        return self.driver.find_element_by_xpath(password_info_locator).text

    def get_error_info(self):
        WebDriverWait(self.driver, 30, 0.1).until(EC.visibility_of_element_located((By.XPATH, error_info_locator)))  # 判断元素出现
        return self.driver.find_element_by_xpath(error_info_locator).text

