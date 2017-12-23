# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/4 0:01
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : project_page.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import time
from homework.homework_appium_pytest_siye.Common.elements_locator import *


class ProjectPage:

    def __init__(self,driver):
        self.driver = driver

    #正常投标操作
    def bid_normal(self,bid_name,amount):
        self.driver.find_element_by_name(project_num_locator %bid_name).click()
        self.driver.find_element_by_id(project_amount_locator).send_keys(amount)
        self.driver.find_element_by_id(project_invest_locator).click()
        invest_date = time.strftime('%Y-%m-%d')
        invest_time = time.strftime('%H:%M')
        return invest_date, invest_time

