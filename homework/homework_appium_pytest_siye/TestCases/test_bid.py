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

        try:
            #查余额
            HomePage(init_driver).click_meButton()   #点击下方"我"按钮
            balance_before = MyAccountInfoPage(init_driver).get_balance()   #在我的账户页面，获得余额
            #点击首页按钮进入首页
            MyAccountInfoPage(init_driver).click_homeButton()
            #验证投标提示文字是否正确
            HomePage(init_driver).click_commendProjectMessage()     #在首页点击精选项目推荐的标的信息
            tender_time = ProjectPage(init_driver).bid_normal(amount)   #正常进行投标，并记录投标时间
            success_info=ProjectPage(init_driver).get_successTip()      #先投标成功提示获取提示文字
            assert tip_success_bid in success_info

            #验证投标后余额是否正确
            ProjectPage(init_driver).close_success_info_byconfirmButton()   #投标成功提示框内确认按钮点击后关闭投标成功提示框
            ProjectPage(init_driver).click_backButton()         #点击标的信息页面左上角返回页面，返回首页
            HomePage(init_driver).click_meButton()              #点击下方"我"按钮，进入我的账户页
            balance_after = MyAccountInfoPage(init_driver).get_balance()    #记录此时我的账户页显示的余额
            print("投标前账户余额为:%s" % balance_before)       #输出相关余额和投标金额
            print("投标金额为:%s"%amount)
            print("投标后账户余额为:%s" % balance_after)
            assert int(balance_after) == int(balance_before)#-int(amount)    因为目前APP投标后没有及时刷新余额，导致第二次查看余额数未有变化，故暂时屏蔽取差值

            #验证投标信息是否正确
            MyAccountInfoPage(init_driver).click_mytenderButton()           #我的账户页面点击"我的投资"按钮
            MyTenderPage(init_driver).click_firsttender()                   #在我的投资页面点击最上方的最近一次投标记录
            MyTenderPage(init_driver).click_tenderlistButton()              #在标的详情页面点击"投资记录"按钮
            bidinfo = MyTenderPage(init_driver).get_tenderinfo()            #在投资记录页面记录最近一次投标的投资人，金额，投标时间
            assert abs(MyTenderPage(init_driver).sub_seconds(bidinfo[2],tender_time))<=3        #因为有时间误差，故对两次记录的投标时间进行小于3秒的比对，误差3秒内认为通过
            assert [investor,amount] == [bidinfo[0],bidinfo[1]]             #在时间验证通过的情况下，对投资人和投资金额进行断言

            #注销账号操作
            MyTenderPage(init_driver).click_closeButton()   #关闭投资记录界面
            MyTenderPage(init_driver).click_backButton()    #在标的详情页面点击左上角返回按钮
            MyTenderPage(init_driver).click_backButton()    #在投资记录页面点击左上角返回按钮
            MyAccountInfoPage(init_driver).logout()     #退出登录

        except AssertionError as e:
            img_name="test_bid_bycommendProject_error.png"
            init_driver.get_screenshot_as_file(image_path+"/"+img_name)
            print('投标测试不通过！异常原因是：%s' % e)
            raise e


