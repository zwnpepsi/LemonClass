# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/3 14:37
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_login.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium import webdriver
from homework.homework_pageobject_siye.PageObjects.login_page import LoginPage
from homework.homework_pageobject_siye.PageObjects.home_page import HomePage
import unittest
from homework.homework_pageobject_siye.Common.projectpath import *
from homework.homework_pageobject_siye.Common.logger import CommLog
from homework.homework_pageobject_siye.TestData.login_testdata import *
from homework.homework_pageobject_siye.TestData.COMM_DATA import *
import logging
myLog = CommLog("TestLogin")
myLog.add_StreamHandler(logging.INFO)
myLog.add_RotatingFileHandler(logging.INFO)



#测试登录功能
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # 最大化窗口
        self.loginpage = LoginPage(self.driver)
        myLog.info("------------测试开始------------")

    #测试登录成功功能
    def test_login_ok(self):
        try:
            self.loginpage.login(web_url, login_username_ok,login_password_ok)
            #验证
            homepage=HomePage(self.driver)
            nickname=homepage.get_nickname()
            self.assertIn(check_nickname ,nickname,"登录不成功")
            myLog.info("验证登录成功功能---测试通过")
        except AssertionError as e:
            # print("登录不成功，原因为：%s" % e)
            img_name = "test_login_ok_error.png"
            self.driver.save_screenshot(image_path + "/" + img_name)
            myLog.exception('登录测试不通过！异常原因是：%s' % e)
            raise e

    #测试不输入密码进行登录操作
    def test_login_noPassword(self):
        try:
            self.loginpage.login(web_url,login_username_ok,"")
            #验证
            password_info = self.loginpage.get_password_info()
            self.assertIn(check_noPassword_Info,password_info,"登录不成功")
            myLog.info("验证不输入密码进行登录操作---测试通过")
        except AssertionError as e:
            # print("登录不成功，原因为：%s" % e)
            img_name = "test_login_noPassword_error.png"
            self.driver.save_screenshot(image_path + "/" + img_name)
            myLog.exception('登录测试不通过！异常原因是：%s' % e)
            raise e

    #测试不输入用户名进行登录操作
    def test_login_noUsername(self):
        try:
            self.loginpage.login(web_url,"",login_password_ok)
            #验证
            username_info = self.loginpage.get_username_info()
            self.assertIn(check_noUsername_Info,username_info,"登录不成功")
            myLog.info("验证不输入用户名进行登录操作---测试通过")
        except AssertionError as e:
            # print("登录不成功，原因为：%s" % e)
            img_name = "test_login_noUsername_error.png"
            self.driver.save_screenshot(image_path + "/" + img_name)
            myLog.exception('登录测试不通过！异常原因是：%s' % e)
            raise e

    #测试输入非法的用户名进行登录操作
    def test_login_incorrectUsername(self):
        try:
            self.loginpage.login(web_url,login_username_wrong,login_password_ok)
            #验证
            error_info = self.loginpage.get_error_info()
            self.assertIn(check_wrongUsername_Info,error_info,"登录不成功")
            myLog.info("验证输入非法的用户名进行登录操作---测试通过")
        except AssertionError as e:
            # print("登录不成功，原因为：%s" % e)
            img_name = "test_login_incorrectUsername_error.png"
            self.driver.save_screenshot(image_path + "/" + img_name)
            myLog.exception('登录测试不通过！异常原因是：%s' % e)
            raise e

    #测试输入非法的密码进行登录操作
    def test_login_incorrectPassword(self):
        try:
            self.loginpage.login(web_url,login_username_ok,login_password_wrong)
            #验证
            error_info = self.loginpage.get_error_info()
            self.assertIn(check_wrongPassword_Info,error_info,"登录不成功")
            myLog.info("验证输入非法的密码进行登录操作---测试通过")
        except AssertionError as e:
            # print("登录不成功，原因为：%s" % e)
            img_name = "test_login_incorrectPassword_error.png"
            self.driver.save_screenshot(image_path + "/" + img_name)
            myLog.exception('登录测试不通过！异常原因是：%s' % e)
            raise e

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        myLog.info("------------测试结束------------")

# if __name__ =='__main__':
#     # suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin)
#     # unittest.TextTestRunner().run(suite)


