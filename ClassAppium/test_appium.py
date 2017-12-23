# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/22 14:55
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_appium.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
#coding=utf-8
from appium import webdriver

#通过python写好要链接的手机的相关信息
desired_caps = {}
desired_caps['automationName'] = 'Appium'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '23'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.xxzb.fenwoo'
desired_caps['appActivity'] = '.activity.MainActivity'

#连接代理，获取连接到手机
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#操作元素
driver.find_element_by_xpath("//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.LinearLayout[4]").click()
# driver.find_element_by_name("5").click()
#
# driver.find_element_by_name("9").click()
#
# driver.find_element_by_name("DEL").click()
#
# driver.find_element_by_name("+").click()
#
# driver.find_element_by_name("6").click()
#
# driver.find_element_by_name("=").click()
#
# driver.quit()