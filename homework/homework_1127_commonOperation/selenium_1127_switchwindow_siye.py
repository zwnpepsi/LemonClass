# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/28 23:03
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : selenium_1127_switchwindow_siye.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class SwitchWindowLocation:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.baidu.com/')   #打开前程贷首页
        self.browser.maximize_window()  # 最大化窗口

    #网站进行搜索函数
    def searchKeyword(self):
        search_form_path="//input[@id='kw']"    #找到百度首页搜索栏
        WebDriverWait(self.browser,60,1).until(EC.visibility_of_element_located((By.XPATH,search_form_path)))   #判断搜索框可见
        self.browser.find_element_by_xpath(search_form_path).send_keys("selenium webdriver")   #搜索框传入指定参数

        search_button_path="//input[@id='su']"   #找到搜索输入框元素
        WebDriverWait(self.browser,60,1).until(EC.element_to_be_clickable((By.XPATH, search_button_path)))  # 判断百度一下按钮可用
        self.browser.find_element_by_xpath(search_button_path).click()   #点击百度一下按钮

        result_selenium_path="//div[text()=' The biggest change in ']//preceding-sibling::h3//a"    #找到官网链接结果元素
        WebDriverWait(self.browser, 60, 1).until(EC.element_to_be_clickable((By.XPATH, result_selenium_path)))  # 判断官网链接可点击
        self.browser.find_element_by_xpath(result_selenium_path).click()   #点击官网链接关键字元素

        WebDriverWait(self.browser, 60, 1).until(EC.new_window_is_opened)  # 一用就报错，用不好
        #获取当前所有窗口
        windows=self.browser.window_handles
        #切换到最新打开的窗口
        self.browser.switch_to.window(windows[-1])

        download_button_path="//div[@class='downloadBox']"      #定位到新网页右侧下载按钮位置
        #download_button_path="//li[@id='menu_download']"       #定位到新网页上方下载按钮位置
        WebDriverWait(self.browser, 60, 1).until(EC.element_to_be_clickable((By.XPATH, download_button_path)))  # 判断download按钮可点击
        self.browser.find_element_by_xpath(download_button_path).click()     #点击download按钮

        time.sleep(3)  #等待3秒查看下载界面信息
        self.browser.close()    #关闭当前窗口
        self.browser.switch_to.window(windows[0])          #切换到原始窗口
        self.browser.close()    #关闭原始窗口
        self.browser.quit()     #关闭浏览器

#测试代码
test_selenium=SwitchWindowLocation()
test_selenium.searchKeyword()
