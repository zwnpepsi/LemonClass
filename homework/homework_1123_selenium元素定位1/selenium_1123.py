# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/23 15:14
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : selenium_1123.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

class ElementLocation:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://www.lemfix.com/')
        self.browser.implicitly_wait(5)

    def loginWebsite(self):
        login_element=self.browser.find_element_by_link_text("登录")
        login_element.click()
        time.sleep(1)

        self.browser.find_element_by_id("name").clear()
        self.browser.find_element_by_id("name").send_keys("zwnpepsi")
        self.browser.find_element_by_id("pass").clear()
        self.browser.find_element_by_id("pass").send_keys("zwn870706")

        self.browser.find_element_by_css_selector("input.span-primary").click()
        time.sleep(1)

    def readingArticle(self):
        self.browser.maximize_window()  # 最大化窗口
        self.browser.find_element_by_xpath("//*[@id='topic_list']/div[1]/div/a").click()
        time.sleep(1)
        self.browser.back()#回退

        time.sleep(1)
        self.browser.forward()#前进

    def replyArticle(self):
        time.sleep(1)
        reply_form=self.browser.find_element_by_css_selector("div.CodeMirror-scroll")   #定义回复栏位置
        ActionChains(self.browser).move_to_element(reply_form).click().perform()     #点击回复栏，激活回复栏输入状态
        time.sleep(1)
        self.browser.find_element_by_xpath("//form[@id='reply_form']/div/div/div[2]/div/textarea").send_keys("这是一篇不错的文章")    #在回复栏文本框内输入文字
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='reply_form']/div/div/div[3]/input").click()

    def closeBrowser(self):
        time.sleep(1)
        self.browser.close()#关闭当前窗口
        self.browser.quit()#关闭浏览器


test_selenium=ElementLocation()
test_selenium.loginWebsite()
test_selenium.readingArticle()
test_selenium.replyArticle()
test_selenium.closeBrowser()


