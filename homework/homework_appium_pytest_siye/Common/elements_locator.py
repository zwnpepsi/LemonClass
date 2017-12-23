# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/7 22:00
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : elements_locator.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
#-----------------------------所用需要用到的元素的位置-----------------------------

#-----------------------------首页元素-----------------------------
    #首页-"我"按钮
home_me_locator = "//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[4]"
    #首页-"项目"按钮
home_project_locator = "//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[3]"
    #首页-"注册/登录"按钮
home_login_locator = "com.xxzb.fenwoo:id/btn_login"

#-----------------------------登录页元素-----------------------------
# 手机号码输入框
login_phone_locator = "com.xxzb.fenwoo:id/et_phone"
# 密码输入框
login_password_locator = "//*[@name='password']"
# 登录按钮
login_button_locator = "//button[text()='登录']"
# 密码提示信息
password_info_locator = "//input[@name='password']//following-sibling::div[@class='form-error-info']"
# 账号提示信息
username_info_locator = "//input[@name='phone']//following-sibling::div[@class='form-error-info']"
# 报错信息
error_info_locator = "//div[@class='layui-layer-content']"

#----------------------------我的账户页元素-----------------------------
# 我的账户页面-我的余额
myAccount_balance_locator = "//li[@class='color_sub']"
# 我的账户页面-投资项目按钮
myAccount_investment_locator = "//div[text()='投资项目']"
# 我的账户页面-投资项目里第一个标的日期
myAccount_tender_seedate_locator = "//div[@ms-html='item.date']"
# 我的账户页面-投资项目里第一个标的时间
myAccount_tender_seetime_locator = "//div[@ms-html='item.time']"
# 我的账户页面-投资项目里第一个标的名称
myAccount_tender_name_locator = "//div[@class='deal_tab_font1']//a"

#----------------------------投标页元素-----------------------------
# 投标页面-投标金额
bidding_num_locator = "//span[contains(text(),'%s')]/ancestor::div[@class='title']/following-sibling::div[1]//input[@data-url='/Invest/invest']"
# 投标页面-投标金额下方投标按钮
bidding_bidButton_locator = "//span[contains(text(),'%s')]/ancestor::div[@class='title']/following-sibling::div[1]//button"
# 投标页面-投标金额右侧全投按钮
bidding_allBid_locator = "//span[contains(text(),'%s')]/ancestor::div[@class='title']/following-sibling::div[1]//input[@class='set-all']"
# 投标页面-投标成功提示文字
bidding_success_info_locator = "//div[@class='layui-layer-content']//div//div[@class='capital_font1 note']"
# 投标页面-金额错误提示文字
bidding_error_info_locator = "//div[@class='text-center']"
# 投标页面-标名
bidding_bidName_locator = "//span[contains(text(),'%s')]"
# 投标页面-投标成功页面右上角x按钮
bidding_success_close_locator = "//div[@class='layui-layer-content']//div//div//img[contains(@src,'close')]"

#----------------------------投标信息页元素-----------------------------
# 投标信息页面-投标金额
tenderInfo_num_locator = "//input[@data-url='/Invest/invest']"
# 投标信息页面-投标金额下方投标按钮
tenderInfo_bidButton_locator = "//input[@data-url='/Invest/invest']//parent::div//parent::div//following-sibling::button"
# 投标信息页面-投标金额右侧全投按钮
tenderInfo_allBid_locator = "//input[@class='set-all']"
# 投标信息页面-投标成功提示文字
tenderInfo_success_info_locator = "//div[@class='layui-layer-content']//div//div[@class='capital_font1 note']"
# 投标信息页面-金额错误提示文字
tenderInfo_error_info_locator = "//div[@class='text-center']"
# 投标信息界面-标名
tenderInfo_bidName_locator = "//div[@class='float_left']//span//following-sibling::span"
# 投标信息界面-投标成功页面右上角x按钮
tenderInfo_success_close_locator = "//div[@class='layui-layer-content']//div//div//img[contains(@src,'close')]"