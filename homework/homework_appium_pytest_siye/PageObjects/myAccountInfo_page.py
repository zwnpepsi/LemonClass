# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/2 22:48
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : myAccountInfo_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from homework.homework_appium_pytest_siye.Common.elements_locator import *


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




