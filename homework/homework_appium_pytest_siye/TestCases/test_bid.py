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


#测试投标功能
class TestBid:

    # 通过点击抢投标按钮进入投标信息界面进行合规金额投标
    @pytest.mark.usefixtures("init_driver")
    @pytest.mark.smoke
    def test_bid_bybidGrabLink_bybidName_okNum(self,init_driver):
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
            #点击项目按钮进入项目界面
            MyAccountInfoPage(init_driver).click_projectButton()
            #验证投标提示文字是否正确
            ProjectPage(init_driver).bid_normal(bid_name,amount)
            bidname=init_testbid_driver[2].get_bid_name()
            tender_date, tender_time=init_testbid_driver[2].bid_normal(money_right)
            success_info=init_testbid_driver[2].get_success_info()
            assert tip_success_bid in success_info

            #验证投标后余额是否正确
            init_testbid_driver[2].close_success_info()
            init_testbid_driver[1].click_myaccount()
            balance_after = init_testbid_driver[4].get_balance()
            print("投标前账户余额为:%s" % balance_before)
            print("投标金额为:%s"%money_right)
            print("投标后账户余额为:%s" % balance_after)
            assert int(balance_after) == int(balance_before)-int(money_right)

            #验证投标信息是否正确
            bidinfo = init_testbid_driver[4].get_bidInfo()
            assert [tender_date,tender_time,bidname] == bidinfo
        except AssertionError as e:
            img_name="test_bid_bybidGrabLink_bybidName_okNum_error.png"
            init_testbid_driver[0].save_screenshot(image_path+"/"+img_name)
            print('投标测试不通过！异常原因是：%s' % e)
            raise e
    #
    # # 通过点击抢投标按钮进入投标信息界面进行不合规金额投标
    # @pytest.mark.usefixtures("init_testbid_driver")
    # @pytest.mark.smoke
    # def test_bid_bybidGrabLink_bybidName_incorrectNum(self,init_testbid_driver):
    #     try:
    #         #验证
    #         init_testbid_driver[1].click_bidGrabLink_bybidName(bid_name)
    #         init_testbid_driver[2].bid_normal(money_wrong)
    #         error_info=init_testbid_driver[2].get_error_info()
    #         assert check_wrongmoney in error_info
    #     except AssertionError as e:
    #         img_name = "test_bid_bybidGrabLink_bybidName_incorrectNum_error.png"
    #         init_testbid_driver[0].save_screenshot(image_path + "/" + img_name)
    #         print('投标测试不通过！异常原因是：%s' % e)
    #         raise e
    #
    # # 通过点击抢投标按钮进入投标信息界面进行非10倍数金额投标
    # @pytest.mark.usefixtures("init_testbid_driver")
    # @pytest.mark.smoke
    # def test_bid_bybidGrabLink_bybidName_no10xNum(self,init_testbid_driver):
    #     try:
    #         #验证
    #         init_testbid_driver[1].click_bidGrabLink_bybidName(bid_name)
    #         no10xInfo = init_testbid_driver[2].bid_normal_no10xNum(money_no10)
    #         assert check_no10money in no10xInfo
    #     except AssertionError as e:
    #         img_name = "test_bid_bybidGrabLink_bybidName_no10xNum_error.png"
    #         init_testbid_driver[0].save_screenshot(image_path + "/" + img_name)
    #         print('投标测试不通过！异常原因是：%s' % e)
    #         raise e
    #
    # # 通过点击标名进入投标信息界面进行合规金额投标
    # @pytest.mark.usefixtures("init_testbid_driver")
    # @pytest.mark.smoke
    # def test_bid_bybidName_okNum(self,init_testbid_driver):
    #     try:
    #         # 查余额
    #         init_testbid_driver[1].click_myaccount()
    #         balance_before = init_testbid_driver[4].get_balance()
    #         init_testbid_driver[0].back()
    #         # 验证投标提示文字是否正确
    #         init_testbid_driver[1].click_bidName(bid_name)
    #         bidname = init_testbid_driver[2].get_bid_name()
    #         tender_date, tender_time = init_testbid_driver[2].bid_normal(money_right)
    #         success_info = init_testbid_driver[2].get_success_info()
    #         assert tip_success_bid in success_info
    #
    #         # 验证投标后余额是否正确
    #         init_testbid_driver[2].close_success_info()
    #         init_testbid_driver[1].click_myaccount()
    #         balance_after = init_testbid_driver[4].get_balance()
    #         print("投标前账户余额为:%s" % balance_before)
    #         print("投标金额为:%s" %money_right)
    #         print("投标后账户余额为:%s" % balance_after)
    #         assert int(balance_after) == int(balance_before) - int(money_right)
    #
    #         # 验证投标信息是否正确
    #         bidinfo = init_testbid_driver[4].get_bidInfo()
    #         assert [tender_date, tender_time, bidname] == bidinfo
    #     except AssertionError as e:
    #         img_name = "test_bid_bybidName_okNum_error.png"
    #         init_testbid_driver[0].save_screenshot(image_path + "/" + img_name)
    #         print('投标测试不通过！异常原因是：%s' % e)
    #         raise e
    #
    # # 通过点击页面上方投标按钮进入投标界面选择一个标进行合规金额投标
    # @pytest.mark.usefixtures("init_testbid_driver")
    # @pytest.mark.smoke
    # def test_bid_bybidButton_okNum(self,init_testbid_driver):
    #     try:
    #         # 查余额
    #         init_testbid_driver[1].click_myaccount()
    #         balance_before = init_testbid_driver[4].get_balance()
    #         init_testbid_driver[0].back()
    #         #验证
    #         init_testbid_driver[1].click_bidButton()
    #         bidname = init_testbid_driver[3].get_bid_name(bid_name)
    #         tender_date, tender_time =init_testbid_driver[3].bid_normal(bid_name,money_right)
    #         success_info = init_testbid_driver[3].get_success_info()
    #         assert tip_success_bid in success_info
    #
    #         # 验证投标后余额是否正确
    #         init_testbid_driver[3].close_success_info()
    #         init_testbid_driver[1].click_myaccount()
    #         balance_after = init_testbid_driver[4].get_balance()
    #         print("投标前账户余额为:%s" % balance_before)
    #         print("投标金额为:%s" %money_right)
    #         print("投标后账户余额为:%s" % balance_after)
    #         assert int(balance_after) == int(balance_before) - int(money_right)
    #
    #         # 验证投标信息是否正确
    #         bidinfo = init_testbid_driver[4].get_bidInfo()
    #         assert [tender_date, tender_time, bidname] == bidinfo
    #     except AssertionError as e:
    #         img_name = "test_bid_bybidButton_okNum_error.png"
    #         init_testbid_driver[0].save_screenshot(image_path + "/" + img_name)
    #         print('投标测试不通过！异常原因是：%s' % e)
    #         raise e


