# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/25 20:18
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : selenium_1125_siye.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class HighElementLocation:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://120.76.42.189:8765/Index/')   #打开前程贷首页
        self.browser.maximize_window()  # 最大化窗口
        self.browser.implicitly_wait(5)    #隐性等待5秒

    #网站进行登录操作函数
    def loginWebsite(self):
        login_element=self.browser.find_element_by_xpath("//a[text()='登录']")      #找到前程贷首页登录按钮
        login_element.click()    #点击首页登录按钮
        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@name='phone']").clear()   #找到手机号元素
        self.browser.find_element_by_xpath("//*[@name='phone']").send_keys("15815541763")   #在手机号元素处传入手机号信息
        self.browser.find_element_by_xpath("//*[@name='password']").clear()    #找到密码元素
        self.browser.find_element_by_xpath("//*[@name='password']").send_keys("tudou111111")   #在密码元素处传入密码信息

        self.browser.find_element_by_xpath("//button[text()='登录']").click()     #找到登录按钮元素并点击完成登录操作
        time.sleep(1)

    #进行投标操作
    def submitTenders(self):
        #找到全栈一期web自动化测该标下面的抢投标按钮，并点击
        self.browser.find_element_by_xpath("//span[text()=' 全栈一期web自动化测']/ancestor::a/following-sibling::div//a[text()='抢投标']").click()
        time.sleep(1)
        #在新打开的投标界面找到投标金额输入框并传入数值1000
        self.browser.find_element_by_xpath("//input[@data-url='/Invest/invest']").send_keys("1000")
        time.sleep(1)
        #找到投标按钮并点击
        self.browser.find_element_by_xpath("//input[@data-url='/Invest/invest']//parent::div//parent::div//following-sibling::button").click()
        #记录投标操作时间
        global tender_time
        tender_time=time.strftime('%Y-%m-%d %H:%M')
        time.sleep(1)
        #定位到弹出的投标成功界面并点击右上角x按钮关闭该页面
        self.browser.find_element_by_xpath("//div[@class='layui-layer-content']//div//div//img[contains(@src,'close')]").click()
        time.sleep(1)

    # 检查投标项目
    def checkTender(self):
        # 找到我的账户按钮元素并点击
        self.browser.find_element_by_xpath("//a[@href='/Member/index.html']").click()  # 在回复栏文本框内输入文字
        time.sleep(1)
        # 找到投资项目按钮元素并点击
        self.browser.find_element_by_xpath("//div[text()='投资项目']").click()
        time.sleep(1)
        # 找到投资项目列表中每个投标单位的投标日期和时间元素
        self.tender_see_date = self.browser.find_elements_by_xpath("//div[@ms-html='item.date']")
        self.tender_see_time = self.browser.find_elements_by_xpath("//div[@ms-html='item.time']")

    # 对比投标项目
    def compareTender(self):
        time.sleep(2)
        for i in range(len(self.tender_see_date)):
            if self.tender_see_date[i].text+" "+self.tender_see_time[i].text==tender_time:
                # self.browser.execute_script(tender_see_date[i].setAttribute('style', 'background: yellow; border: 2px solid red;'),tender_see_date[i].text)
                print("第 %s 条投标记录为刚才您投的标"%(i+1))
                break
            else:
                # 当前页面没找到自己投的标，找到下一页按钮并点击
                self.browser.find_element_by_xpath("//div[@ms-controller='tz_list']//a[text()='下一页']").click()
                # 递归对比函数
                self.compareTender()

    def closeBrowser(self):
        time.sleep(1)
        self.browser.close()#关闭当前窗口
        self.browser.quit()#关闭浏览器


test_selenium=HighElementLocation()
test_selenium.loginWebsite()
test_selenium.submitTenders()
test_selenium.checkTender()
test_selenium.compareTender()
# test_selenium.closeBrowser()