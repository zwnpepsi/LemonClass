# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/7 23:47
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : conftest.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium import webdriver
import pytest
from homework.homework_pageobject_pytest_siye.PageObjects.tender_page import TenderPage
from homework.homework_pageobject_pytest_siye.PageObjects.tenderInfo_page import TenderInfoPage
from homework.homework_pageobject_pytest_siye.PageObjects.login_page import LoginPage
from homework.homework_pageobject_pytest_siye.PageObjects.home_page import HomePage
from homework.homework_pageobject_pytest_siye.PageObjects.myAccountInfo_page import MyAccountInfoPage
from homework.homework_pageobject_pytest_siye.TestData.COMM_DATA import *


@pytest.fixture()
def init_testbid_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()  # 最大化窗口
    LoginPage(driver).login(web_url, login_username, login_password)
    homepage = HomePage(driver)
    tenderinfopage = TenderInfoPage(driver)
    tenderpage = TenderPage(driver)
    myaccountpage = MyAccountInfoPage(driver)
    yield [driver,homepage,tenderinfopage,tenderpage,myaccountpage]
    driver.close()
    driver.quit()

@pytest.fixture()
def init_testlogin_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()  # 最大化窗口
    loginpage = LoginPage(driver)
    yield [driver, loginpage]
    driver.close()
    driver.quit()