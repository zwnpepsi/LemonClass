# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/28 15:33
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : selenium_1127_actionchains_siye.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class ActionChainsLocation:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.qian100.com/')   #打开前程贷首页
        self.browser.maximize_window()  # 最大化窗口

    #网站进行登录操作函数
    def loginWebsite(self):
        login_access="//a[text()='登录']"    #找到前程贷首页登录按钮
        WebDriverWait(self.browser,5,1).until(EC.visibility_of_element_located((By.XPATH,login_access)))   #判断登录按钮可见
        self.browser.find_element_by_xpath(login_access).click()   #点击首页登录按钮

        phone_path="//*[@id='PhoneNum']"   #找到登录界面用户名元素
        WebDriverWait(self.browser,5,1).until(EC.visibility_of_element_located((By.XPATH, phone_path)))  # 判断用户名输入框可见
        self.browser.find_element_by_xpath(phone_path).clear()
        self.browser.find_element_by_xpath(phone_path).send_keys("18010073976")   #在手机号元素处传入手机号信息

        password_path="//*[@id='PassWord']"    #找到登录界面密码元素
        WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, password_path)))  # 判断密码输入框可见
        self.browser.find_element_by_xpath(password_path).clear()
        self.browser.find_element_by_xpath(password_path).send_keys("aaa123456")   #在密码元素处传入密码信息

        login_button_path="//dd[@class='login_input']//div[text()='登录']"    #找到登录界面登录按钮元素
        WebDriverWait(self.browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, login_button_path)))  # 判断登录按钮可点击
        self.browser.find_element_by_xpath(login_button_path).click()     #找到登录按钮元素并点击完成登录操作

    #进行鼠标操作
    def actionChainsOperation(self):
        #找到我的账户按钮，并鼠标悬停
        WebDriverWait(self.browser, 10, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='myzhanghao']")))  # 判断我的账户按钮可见
        myaccount_path1 = self.browser.find_element_by_xpath("//div[@class='myzhanghao']")
        ActionChains(self.browser).move_to_element(myaccount_path1).perform()
        #鼠标悬停我的账户按钮后，在下拉菜单中点击账户充值按钮
        recharge_path="//li//a[text()='账户充值']"
        WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, recharge_path)))  # 判断账户充值选项可见
        self.browser.find_element_by_xpath(recharge_path).click()   #点击充值按钮
        time.sleep(5)   #在充值界面等待5秒查看充值界面信息
        self.browser.back()

        # 再次去我的账户按钮处鼠标悬停
        WebDriverWait(self.browser, 10, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='myzhanghao']")))  # 判断我的账户按钮可见
        myaccount_path2 = self.browser.find_element_by_xpath("//div[@class='myzhanghao']")
        ActionChains(self.browser).move_to_element(myaccount_path2).perform()
        # 鼠标悬停我的账户按钮后，在下拉菜单中点击站内消息按钮
        info_path = "//li//a[text()='站内消息']"
        WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, info_path)))  # 判断站内消息选项可见
        self.browser.find_element_by_xpath(info_path).click()  # 点击站内消息按钮
        time.sleep(5)  # 在站内消息界面等待5秒查看站内消息界面信息
        self.browser.back()

        # 再次去我的账户按钮处鼠标悬停
        WebDriverWait(self.browser, 10, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='myzhanghao']")))  # 判断我的账户按钮可见
        myaccount_path3 = self.browser.find_element_by_xpath("//div[@class='myzhanghao']")
        ActionChains(self.browser).move_to_element(myaccount_path3).perform()
        # 鼠标悬停我的账户按钮后，在下拉菜单中点击我的投资按钮
        myInvestment_path = "//li//a[text()='我的投资']"
        WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, myInvestment_path)))  # 判断我的投资选项可见
        self.browser.find_element_by_xpath(myInvestment_path).click()  # 点击我的投资按钮
        time.sleep(5)  # 在站内消息界面等待5秒查看站内消息界面信息
        self.browser.back()

        # 再次去我的账户按钮处鼠标悬停
        WebDriverWait(self.browser, 10, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='myzhanghao']")))  # 判断我的账户按钮可见
        myaccount_path4 = self.browser.find_element_by_xpath("//div[@class='myzhanghao']")
        ActionChains(self.browser).move_to_element(myaccount_path4).perform()
        # 鼠标悬停我的账户按钮后，在下拉菜单中点击退出按钮
        logout_path = "//li//a[text()='退出']"
        WebDriverWait(self.browser, 5, 1).until(
            EC.visibility_of_element_located((By.XPATH, logout_path)))  # 判断我的投资选项可见
        self.browser.find_element_by_xpath(logout_path).click()  # 点击退出按钮

    #关闭浏览器函数
    def closeBrowser(self):
        time.sleep(3)
        self.browser.close()  # 关闭当前窗口
        self.browser.quit()  # 关闭浏览器

#测试代码
test_selenium=ActionChainsLocation()
test_selenium.loginWebsite()
test_selenium.actionChainsOperation()
test_selenium.closeBrowser()