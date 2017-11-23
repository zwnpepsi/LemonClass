
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/22 21:15
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_webauto.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium import webdriver
import time
import os
browser = webdriver.Chrome()
browser.maximize_window()#最大化窗口
# browser.set_window_size()#设置窗口大小

# time.sleep(4)   #强制等待4秒
browser.implicitly_wait(30)   #隐性等待30秒

#访问url
browser.get('http://www.baidu.com/')

#找元素、操作元素
# browser.find_element_by_id("kw").clear()#先清除输入框
# input_locator=browser.find_element_by_css_selector("input#kw") #通过css语句找到指定元素
browser.find_element_by_name("wd")
browser.find_element_by_id("kw").send_keys("selenium")#找到并进行输入

browser.find_element_by_id("su").click()#点击搜索按钮
time.sleep(4)
browser.back()#回退
browser.forward()#前进

#截图
time.sleep(2)
browser.get_screenshot_as_file(os.getcwd()+ "/test.png")

#退出
browser.close()#关闭当前窗口
browser.quit()#关闭浏览器