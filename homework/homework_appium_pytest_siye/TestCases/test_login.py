# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/3 14:37
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_login.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import pytest
from homework.homework_appium_pytest_siye.PageObjects.home_page import HomePage
from homework.homework_appium_pytest_siye.PageObjects.login_page import LoginPage
from homework.homework_appium_pytest_siye.TestData.login_testdata import *
from homework.homework_appium_pytest_siye.PageObjects.myAccountInfo_page import MyAccountInfoPage
from homework.homework_appium_pytest_siye.Common.projectpath import *


#测试登录功能
class TestLogin():

    # 测试登录成功功能
    @pytest.mark.usefixtures("init_driver")
    @pytest.mark.smoke
    def test_login_ok(self,init_driver):
        try:
            #点击页面右上角注册/登录按钮进入登录页
            HomePage(init_driver).click_loginButton()
            #进行登录操作
            LoginPage(init_driver).login(login_username_ok,login_password_ok)
            #关闭开启手势密码提示框
            HomePage(init_driver).click_cancelButton()
            #点击页面右下方"我"按钮进入我的账户界面
            HomePage(init_driver).click_meButton()
            #验证
            nickname=MyAccountInfoPage(init_driver).get_nickname()
            assert check_nickname == nickname

            #退出登录
            MyAccountInfoPage(init_driver).logout()
        except AssertionError as e:
            img_name = "test_login_ok_error.png"
            init_driver.save_screenshot(image_path + "/" + img_name)
            print('登录测试不通过！异常原因是：%s' % e)
            raise e





