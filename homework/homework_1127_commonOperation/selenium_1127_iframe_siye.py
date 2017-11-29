# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/28 14:08
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : selenium_1127_iframe_siye.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class iFrameLocation:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://ke.qq.com/')   #打开腾讯课堂首页
        self.browser.maximize_window()  # 最大化窗口

    #判断元素是否存在的函数
    def isElementExist(self, element):
        time.sleep(2)
        flag = True
        try:
            self.browser.find_element_by_xpath(element)   #定位元素
            return flag     #元素存在，返回flag=True
        except Exception as  e:
            flag = False
            return flag     #元素不存在，返回flag=False

    #网站进行登录操作函数
    def loginWebsite(self):
        login_access="//div[@class='mod-entry']//a[text()='登录']"    #找到腾讯课堂首页banner图右侧登录按钮
        #login_access="//div[@id='js-mod-header-login']//a[text()="登录"]"    #找到腾讯课堂首页最上方登录按钮
        WebDriverWait(self.browser,10,1).until(EC.element_to_be_clickable((By.XPATH,login_access)))   #判断登录按钮可见
        self.browser.find_element_by_xpath(login_access).click()   #点击首页登录按钮

        user_login_option_path = "//div[@class='ptlogin-wrap']"
        #因为登录时有可能会出现先选择qq登录还是微信登录选项，所以调用判断函数，读取flag值
        flag = self.isElementExist(user_login_option_path)

        if flag:           #如果选择帐号登录类型界面元素存在
            WebDriverWait(self.browser, 10, 1).until(EC.visibility_of_element_located((By.XPATH, user_login_option_path)))  # 判断选择帐号登录类型界面可见
            self.browser.find_element_by_xpath("//a[text()='QQ登录']").click()    #点击qq登录按钮
            # 切换到登录iframe检查元素位置并操作
            self.browser.switch_to.frame("login_frame_qq")  # 切换到login_frame_qq iframe内
            user_login_path = "//div[@id='bottom_qlogin']//a[text()='帐号密码登录']"
            WebDriverWait(self.browser, 10, 1).until(EC.visibility_of_element_located((By.XPATH, user_login_path)))  # 判断帐号密码登录按钮可见
            self.browser.find_element_by_xpath(user_login_path).click()  # 点击帐号密码登录按钮

            user_path = "//*[@name='u']"  # 找到登录界面用户名元素
            WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, user_path)))  # 判断用户名输入框可见
            self.browser.find_element_by_xpath(user_path).clear()
            self.browser.find_element_by_xpath(user_path).send_keys("1076168822")  # 在用户名输入框内传入qq号信息

            password_path = "//*[@name='p']"  # 找到登录界面密码元素
            WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, password_path)))  # 判断密码输入框可见
            self.browser.find_element_by_xpath(password_path).clear()
            self.browser.find_element_by_xpath(password_path).send_keys("Zzz787616")  # 在密码输入框传入密码信息

            login_button_path = "//*[@id='login_button']"  # 找到登录界面登录按钮元素
            WebDriverWait(self.browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, login_button_path)))  # 判断登录按钮可点击
            self.browser.find_element_by_xpath(login_button_path).click()  # 找到登录按钮元素并点击完成登录操作

            #登陆后会弹出设置学习兴趣界面，所以需要点击下次再选按钮
            next_option_path="//a[@title='下次再选']"
            WebDriverWait(self.browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, next_option_path)))  # 判断下次再选按钮可点击
            self.browser.find_element_by_xpath(next_option_path).click()  # 找到下次再选按钮元素并点击完成登录操作

        else:        #如果选择帐号登录类型界面元素不存在，直接切换到login_frame_qq  iframe内进行操作
            # 切换到登录iframe检查元素位置并操作
            iframe_path="//iframe[@name='login_frame_qq']"
            WebDriverWait(self.browser, 10, 1).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, iframe_path)))  # 判断iframe可以被切换到
            self.browser.switch_to.frame("login_frame_qq")  # 切换到login_frame_qq iframe内

            user_login_path = "//div[@id='bottom_qlogin']//a[text()='帐号密码登录']"
            WebDriverWait(self.browser, 10, 1).until(EC.visibility_of_element_located((By.XPATH, user_login_path)))  # 判断帐号密码登录按钮可见
            self.browser.find_element_by_xpath(user_login_path).click()  # 点击帐号密码登录按钮

            user_path = "//*[@name='u']"  # 找到登录界面用户名元素
            WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, user_path)))  # 判断用户名输入框可见
            self.browser.find_element_by_xpath(user_path).clear()
            self.browser.find_element_by_xpath(user_path).send_keys("1076168822")  # 在用户名输入框内传入qq号信息

            password_path = "//*[@name='p']"  # 找到登录界面密码元素
            WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, password_path)))  # 判断密码输入框可见
            self.browser.find_element_by_xpath(password_path).clear()
            self.browser.find_element_by_xpath(password_path).send_keys("Zzz787616")  # 在密码输入框传入密码信息

            login_button_path = "//*[@id='login_button']"  # 找到登录界面登录按钮元素
            WebDriverWait(self.browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, login_button_path)))  # 判断登录按钮可点击
            self.browser.find_element_by_xpath(login_button_path).click()  # 找到登录按钮元素并点击完成登录操作

            # 登陆后会弹出设置学习兴趣界面，所以需要点击下次再选按钮
            next_option_path = "//a[@title='下次再选']"
            WebDriverWait(self.browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, next_option_path)))  # 判断下次再选按钮可点击
            self.browser.find_element_by_xpath(next_option_path).click()  # 找到下次再选按钮元素并点击完成登录操作

    # 关闭浏览器函数
    def closeBrowser(self):
        time.sleep(3)
        self.browser.close()  # 关闭当前窗口
        self.browser.quit()  # 关闭浏览器

#测试代码
test_selenium=iFrameLocation()
test_selenium.loginWebsite()
test_selenium.closeBrowser()
