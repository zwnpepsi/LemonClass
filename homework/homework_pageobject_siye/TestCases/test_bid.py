# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/4 0:31
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_bid.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium import webdriver
from homework.homework_pageobject_siye.PageObjects.tender_page import TenderPage
from homework.homework_pageobject_siye.PageObjects.tenderInfo_page import TenderInfoPage
from homework.homework_pageobject_siye.PageObjects.login_page import LoginPage
from homework.homework_pageobject_siye.PageObjects.home_page import HomePage
from homework.homework_pageobject_siye.PageObjects.myAccountInfo_page import MyAccountInfoPage
import unittest
from homework.homework_pageobject_siye.Common.projectpath import *
from homework.homework_pageobject_siye.TestData.investment_testdata import *
from homework.homework_pageobject_siye.Common.logger import CommLog
from homework.homework_pageobject_siye.TestData.COMM_DATA import *
import logging
myLog = CommLog("TestBid")
myLog.add_StreamHandler(logging.INFO)
myLog.add_RotatingFileHandler(logging.INFO)


#测试投标功能
class TestBid(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # 最大化窗口
        LoginPage(self.driver).login(web_url, login_username,login_password)
        self.homepage = HomePage(self.driver)
        self.tenderinfopage=TenderInfoPage(self.driver)
        self.tenderpage=TenderPage(self.driver)
        self.myaccountpage=MyAccountInfoPage(self.driver)
        myLog.info("------------测试开始------------")

    # 通过点击抢投标按钮进入投标信息界面进行合规金额投标
    def test_bid_bybidGrabLink_bybidName_okNum(self):
        try:
            myLog.info("验证点击抢投标按钮进入投标信息界面进行合规金额投标功能-投标成功提示文字---测试开始")
            #查余额
            self.homepage.click_myaccount()
            balance_before = self.myaccountpage.get_balance()
            self.driver.back()

            #验证投标提示文字是否正确
            self.homepage.click_bidGrabLink_bybidName(bid_name)
            bidname=self.tenderinfopage.get_bid_name()
            tender_date, tender_time=self.tenderinfopage.bid_normal(money_right)
            success_info=self.tenderinfopage.get_success_info()
            self.assertIn(tip_success_bid,success_info,"投标不成功")
            myLog.info("验证点击抢投标按钮进入投标信息界面进行合规金额投标功能-投标成功提示文字---测试通过")

            #验证投标后余额是否正确
            myLog.info("验证点击抢投标按钮进入投标信息界面进行合规金额投标功能-投标后余额是否正确---测试开始")
            self.tenderinfopage.close_success_info()
            self.homepage.click_myaccount()
            balance_after = self.myaccountpage.get_balance()
            myLog.info("投标前账户余额为:%s" % balance_before)
            myLog.info("投标金额为:%s"%money_right)
            myLog.info("投标后账户余额为:%s" % balance_after)
            self.assertEqual(int(balance_after),int(balance_before)-int(money_right),"余额数值不对")
            myLog.info("验证点击抢投标按钮进入投标信息界面进行合规金额投标功能-投标消耗金额---测试通过")

            #验证投标信息是否正确
            myLog.info("验证点击抢投标按钮进入投标信息界面进行合规金额投标功能-投标信息是否正确---测试开始")
            bidinfo = self.myaccountpage.get_bidInfo()
            self.assertEqual([tender_date,tender_time,bidname],bidinfo,"这次投标信息错误")
            myLog.info("验证点击抢投标按钮进入投标信息界面进行合规金额投标功能-投标信息---测试通过")
        except AssertionError as e:
            # print("投标不成功，原因为：%s" % e)
            img_name="test_bid_bybidGrabLink_bybidName_okNum_error.png"
            self.driver.save_screenshot(image_path+"/"+img_name)
            myLog.exception('投标测试不通过！异常原因是：%s' % e)
            raise e

    # 通过点击抢投标按钮进入投标信息界面进行不合规金额投标
    def test_bid_bybidGrabLink_bybidName_incorrectNum(self):
        try:
            #验证
            myLog.info("验证点击抢投标按钮进入投标信息界面进行不合规金额投标功能---测试开始")
            self.homepage.click_bidGrabLink_bybidName(bid_name)
            self.tenderinfopage.bid_normal(money_wrong)
            error_info=self.tenderinfopage.get_error_info()
            self.assertIn(check_wrongmoney,error_info,"投标不成功")
            myLog.info("验证点击抢投标按钮进入投标信息界面进行不合规金额投标功能---测试通过")
        except AssertionError as e:
            # print("投标不成功，原因为：%s" % e)
            img_name = "test_bid_bybidGrabLink_bybidName_incorrectNum_error.png"
            self.driver.save_screenshot(image_path + "/" + img_name)
            myLog.exception('投标测试不通过！异常原因是：%s' % e)
            raise e

    # 通过点击抢投标按钮进入投标信息界面进行非10倍数金额投标
    def test_bid_bybidGrabLink_bybidName_no10xNum(self):
        try:
            #验证
            myLog.info("验证点击抢投标按钮进入投标信息界面进行非10倍数金额投标功能---测试开始")
            self.homepage.click_bidGrabLink_bybidName(bid_name)
            no10xInfo = self.tenderinfopage.bid_normal_no10xNum(money_no10)
            self.assertIn(check_no10money,no10xInfo,"投标不成功")
            myLog.info("验证点击抢投标按钮进入投标信息界面进行非10倍数金额投标功能---测试通过")
        except AssertionError as e:
            # print("投标不成功，原因为：%s" % e)
            img_name = "test_bid_bybidGrabLink_bybidName_no10xNum_error.png"
            self.driver.save_screenshot(image_path + "/" + img_name)
            myLog.exception('投标测试不通过！异常原因是：%s' % e)
            raise e

    # 通过点击标名进入投标信息界面进行合规金额投标
    def test_bid_bybidName_okNum(self):
        try:
            myLog.info("验证点击标名进入投标信息界面进行合规金额投标功能-投标成功提示文字---测试开始")
            # 查余额
            self.homepage.click_myaccount()
            balance_before = self.myaccountpage.get_balance()
            self.driver.back()
            # 验证投标提示文字是否正确
            self.homepage.click_bidName(bid_name)
            bidname = self.tenderinfopage.get_bid_name()
            tender_date, tender_time = self.tenderinfopage.bid_normal(money_right)
            success_info = self.tenderinfopage.get_success_info()
            self.assertIn(tip_success_bid,success_info,"投标不成功")
            myLog.info("验证点击标名进入投标信息界面进行合规金额投标功能---测试通过")

            # 验证投标后余额是否正确
            myLog.info("验证点击标名进入投标信息界面进行合规金额投标功能-投标后余额是否正确---测试开始")
            self.tenderinfopage.close_success_info()
            self.homepage.click_myaccount()
            balance_after = self.myaccountpage.get_balance()
            myLog.info("投标前账户余额为:%s" % balance_before)
            myLog.info("投标金额为:%s" %money_right)
            myLog.info("投标后账户余额为:%s" % balance_after)
            self.assertEqual(int(balance_after), int(balance_before) - int(money_right), "余额数值不对")
            myLog.info("验证点击标名进入投标信息界面进行合规金额投标功能-投标消耗金额---测试通过")

            # 验证投标信息是否正确
            myLog.info("验证点击标名进入投标信息界面进行合规金额投标功能-投标信息是否正确---测试开始")
            bidinfo = self.myaccountpage.get_bidInfo()
            self.assertEqual([tender_date, tender_time, bidname], bidinfo, "这次投标信息错误")
            myLog.info("验证点击标名进入投标信息界面进行合规金额投标功能-投标信息---测试通过")
        except AssertionError as e:
            # print("投标不成功，原因为：%s" % e)
            img_name = "test_bid_bybidName_okNum_error.png"
            self.driver.save_screenshot(image_path + "/" + img_name)
            myLog.exception('投标测试不通过！异常原因是：%s' % e)
            raise e

    # 通过点击页面上方投标按钮进入投标界面选择一个标进行合规金额投标
    def test_bid_bybidButton_okNum(self):
        try:
            myLog.info("验证点击页面上方投标按钮进入投标界面选择一个标进行合规金额投标功能-投标成功提示文字---测试开始")
            # 查余额
            self.homepage.click_myaccount()
            balance_before = self.myaccountpage.get_balance()
            self.driver.back()
            #验证
            self.homepage.click_bidButton()
            bidname = self.tenderpage.get_bid_name(bid_name)
            tender_date, tender_time =self.tenderpage.bid_normal(bid_name,money_right)
            success_info = self.tenderpage.get_success_info()
            self.assertIn(tip_success_bid,success_info,"投标不成功")
            myLog.info("验证点击页面上方投标按钮进入投标界面选择一个标进行合规金额投标功能---测试通过")

            # 验证投标后余额是否正确
            myLog.info("验证点击页面上方投标按钮进入投标界面选择一个标进行合规金额投标功能-投标后余额是否正确---测试开始")
            self.tenderpage.close_success_info()
            self.homepage.click_myaccount()
            balance_after = self.myaccountpage.get_balance()
            myLog.info("投标前账户余额为:%s" % balance_before)
            myLog.info("投标金额为:%s" %money_right)
            myLog.info("投标后账户余额为:%s" % balance_after)
            self.assertEqual(int(balance_after), int(balance_before) - int(money_right), "余额数值不对")
            myLog.info("验证点击页面上方投标按钮进入投标界面选择一个标进行合规金额投标功能-投标消耗金额---测试通过")

            # 验证投标信息是否正确
            myLog.info("验证点击页面上方投标按钮进入投标界面选择一个标进行合规金额投标功能-投标信息是否正确---测试开始")
            bidinfo = self.myaccountpage.get_bidInfo()
            self.assertEqual([tender_date, tender_time, bidname], bidinfo, "这次投标信息错误")
            myLog.info("验证点击页面上方投标按钮进入投标界面选择一个标进行合规金额投标功能-投标信息---测试通过")
        except AssertionError as e:
            # print("投标不成功，原因为：%s" % e)
            img_name = "test_bid_bybidButton_okNum_error.png"
            self.driver.save_screenshot(image_path + "/" + img_name)
            myLog.exception('投标测试不通过！异常原因是：%s' % e)
            raise e

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        myLog.info("------------测试结束------------")

# if __name__ =='__main__':
#     suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestBid)
#     unittest.TextTestRunner().run(suite)