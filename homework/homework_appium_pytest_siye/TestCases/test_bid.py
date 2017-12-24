# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/4 0:31
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_bid.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import pytest
from homework.homework_appium_pytest_siye.TestData.investment_testdata import *
from homework.homework_appium_pytest_siye.Common.projectpath import *
from homework.homework_appium_pytest_siye.PageObjects.home_page import HomePage
from homework.homework_appium_pytest_siye.PageObjects.login_page import LoginPage
from homework.homework_appium_pytest_siye.TestData.COMM_DATA import *
from homework.homework_appium_pytest_siye.PageObjects.myAccountInfo_page import MyAccountInfoPage
from homework.homework_appium_pytest_siye.PageObjects.project_page import ProjectPage
from homework.homework_appium_pytest_siye.PageObjects.mytender_page import MyTenderPage



#测试投标功能
class TestBid:

    # 通过点击抢投标按钮进入投标信息界面进行合规金额投标
    @pytest.mark.usefixtures("init_driver")
    @pytest.mark.smoke
    def test_bid_bycommendProject(self,init_driver):
        #完成登录操作
        # 点击页面右上角注册/登录按钮进入登录页
        HomePage(init_driver).click_loginButton()
        # 进行登录操作
        LoginPage(init_driver).login(login_username, login_password)
        # 关闭开启手势密码提示框
        HomePage(init_driver).click_cancelButton()

        try:
            #查余额
            HomePage(init_driver).click_meButton()
            balance_before = MyAccountInfoPage(init_driver).get_balance()
            #点击项目按钮进入首页
            MyAccountInfoPage(init_driver).click_homeButton()
            #验证投标提示文字是否正确
            HomePage(init_driver).click_commendProjectMessage()
            tender_time = ProjectPage(init_driver).bid_normal(amount)
            success_info=ProjectPage(init_driver).get_successTip()
            assert tip_success_bid in success_info

            #验证投标后余额是否正确
            ProjectPage(init_driver).close_success_info_byconfirmButton()
            ProjectPage(init_driver).click_backButton()
            HomePage(init_driver).click_meButton()
            balance_after = MyAccountInfoPage(init_driver).get_balance()
            print("投标前账户余额为:%s" % balance_before)
            print("投标金额为:%s"%amount)
            print("投标后账户余额为:%s" % balance_after)
            assert int(balance_after) == int(balance_before)-int(amount)

            #验证投标信息是否正确
            MyAccountInfoPage(init_driver).click_mytenderButton()
            MyTenderPage(init_driver).click_firsttender()
            MyTenderPage(init_driver).click_tenderlistButton()
            bidinfo = MyTenderPage(init_driver).get_tenderinfo()
            assert [investor,tender_time,amount] == bidinfo
        except AssertionError as e:
            img_name="test_bid_bycommendProject_error.png"
            init_driver.get_screenshot_as_file(image_path+"/"+img_name)
            print('投标测试不通过！异常原因是：%s' % e)
            raise e


