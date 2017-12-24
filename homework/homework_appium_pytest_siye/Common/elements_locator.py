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
    #首页-"精选项目"下方推荐的标信息
home_commendProjectMessage_locator = "com.xxzb.fenwoo:id/layout_loan_item"

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
# 我的账户页面-余额
myAccount_balance_locator = "//android.widget.TextView[@resource-id='com.xxzb.fenwoo:id/tv_leave']"
# 我的账户页面-首页按钮
myAccount_home_locator = "//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.LinearLayout[1]"
# 我的账户页面-我的投资按钮
myAccount_mytender_locator = "//android.widget.GridView[@resource-id='com.xxzb.fenwoo:id/gv_functions']/android.widget.LinearLayout[1]"

#----------------------------项目页元素-----------------------------
# 项目页面-标名
project_num_locator = "%s"
# 项目界面-投标金额
project_amount_locator = "com.xxzb.fenwoo:id/et_investamount"
# 项目界面-立即投资按钮
project_invest_locator = "com.xxzb.fenwoo:id/btn_investnow"
# 项目界面-投标成功提示文字
project_successtip_locator = "com.xxzb.fenwoo:id/tv_title"
# 投标界面-投标成功提示确定按钮
project_confirm_locator = "com.xxzb.fenwoo:id/btn_confirm"
# 投标界面-返回按钮
project_back_locator = "com.xxzb.fenwoo:id/btn_back"

#----------------------------我的投资页面元素-----------------------------
# 我的投资页面-最上面一个投资记录
mytender_firsttender_locator = "com.xxzb.fenwoo:id/layout_content"
# 我的投资页面-投资记录按钮
mytender_tenderlist_locator = "com.xxzb.fenwoo:id/layout_investrecord"
# 投资记录界面-投资人
tendelist_investor_locator = "com.xxzb.fenwoo:id/tv_user_name"
# 投资记录界面-投资时间
tendelist_time_locator = "com.xxzb.fenwoo:id/tv_createtime"
# 投资记录界面-投资金额
tendelist_amount_locator = "com.xxzb.fenwoo:id/tv_invest_money"
# 投资记录界面-左上角关闭按钮
tendelist_close_locator = "com.xxzb.fenwoo:id/btn_back"
# 投资记录界面-左上角返回按钮
tendelist_back_locator = "com.xxzb.fenwoo:id/btn_back"




