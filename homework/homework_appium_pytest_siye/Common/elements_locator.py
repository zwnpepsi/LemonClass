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
home_me_locator = "//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.LinearLayout[4]"
    #首页-"项目"按钮
home_project_locator = "//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.LinearLayout[3]"
    #首页-"注册/登录"按钮
home_login_locator = "com.xxzb.fenwoo:id/btn_login"
    #登录完毕提示开启手势验证提示框的以后再说按钮
home_cancel_locator = "com.xxzb.fenwoo:id/btn_cancel"

#-----------------------------登录页元素-----------------------------
# 手机号码输入框
login_phone_locator = "com.xxzb.fenwoo:id/et_phone"
# 密码输入框
login_password_locator = "com.xxzb.fenwoo:id/et_pwd"
# 输入完手机号，"下一步"按钮
login_afterphone_next_button_locator = "com.xxzb.fenwoo:id/btn_next_step"
# 输入完密码，"确定按钮"
login_confirm_locator = "com.xxzb.fenwoo:id/btn_next_step"
# "忘记密码"
login_forget_password_locator = "忘记密码?"
# 密码报错信息
# error_info_locator = ""

#----------------------------我的账户页元素-----------------------------
# 我的账户页面-我的昵称
myAccount_nickname_locator = "com.xxzb.fenwoo:id/tv_name"
# 我的账户页面-设置按钮
myAccount_option_locator = "com.xxzb.fenwoo:id/iv_switch_slider"
# 我的账户页面-设置页面-退出当前账号按钮
myAccount_logout_locator = "com.xxzb.fenwoo:id/btn_login_out"
# 我的账户页面-设置页面-确认注销按钮
myAccount_confirm_logout_locator = "com.xxzb.fenwoo:id/btn_confirm"
# # 我的账户页面-投资项目里第一个标的名称
# myAccount_tender_name_locator = "//div[@class='deal_tab_font1']//a"

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