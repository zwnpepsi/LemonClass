# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/7 23:47
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : conftest.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from appium import webdriver
import pytest
from homework.homework_appium_pytest_siye.Common.projectpath import *
from homework.homework_appium_pytest_siye.PageObjects.home_page import HomePage
from homework.homework_appium_pytest_siye.PageObjects.login_page import LoginPage
from homework.homework_appium_pytest_siye.TestData.COMM_DATA import *
from homework.homework_appium_pytest_siye.PageObjects.myAccountInfo_page import MyAccountInfoPage


@pytest.fixture()
def init_driver():
    desired_caps = eval(ReadConfig().readConfig(appInfo_path,"APP_INFO","desired_caps"))
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # 完成登录操作
    # 点击页面右上角注册/登录按钮进入登录页
    HomePage(driver).click_loginButton()
    # 进行登录操作
    LoginPage(driver).login(login_username, login_password)
    # 关闭开启手势密码提示框
    HomePage(driver).click_cancelButton()
    yield driver
    MyAccountInfoPage(init_driver).logout()  # 退出登录
    driver.quit()

@pytest.fixture()
def init_login_driver():
    desired_caps = eval(ReadConfig().readConfig(appInfo_path,"APP_INFO","desired_caps"))
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    MyAccountInfoPage(init_driver).logout()  # 退出登录
    driver.quit()