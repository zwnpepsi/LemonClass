# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/28 12:43
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : selenium_1125_siye_update.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class HighElementLocation:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://120.76.42.189:8765/Index/')   #打开前程贷首页
        self.browser.maximize_window()  # 最大化窗口

    #网站进行登录操作函数
    def loginWebsite(self):
        login_access="//a[text()='登录']"    #找到前程贷首页登录按钮
        WebDriverWait(self.browser,5,1).until(EC.visibility_of_element_located((By.XPATH,login_access)))   #判断登录按钮可见
        self.browser.find_element_by_xpath(login_access).click()   #点击首页登录按钮

        phone_path="//*[@name='phone']"   #找到登录界面用户名元素
        WebDriverWait(self.browser,5,1).until(EC.visibility_of_element_located((By.XPATH, phone_path)))  # 判断用户名输入框可见
        self.browser.find_element_by_xpath(phone_path).clear()   #找到手机号元素
        self.browser.find_element_by_xpath(phone_path).send_keys("15815541763")   #在手机号元素处传入手机号信息

        password_path="//*[@name='password']"    #找到登录界面密码元素
        WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, password_path)))  # 判断密码输入框可见
        self.browser.find_element_by_xpath(password_path).clear()    #找到密码元素
        self.browser.find_element_by_xpath(password_path).send_keys("tudou111111")   #在密码元素处传入密码信息

        login_button_path="//button[text()='登录']"    #找到登录界面登录按钮元素
        WebDriverWait(self.browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, login_button_path)))  # 判断登录按钮可点击
        self.browser.find_element_by_xpath(login_button_path).click()     #找到登录按钮元素并点击完成登录操作

    #进行投标操作
    def submitTenders(self):
        #找到全栈一期web自动化测该标下面的抢投标按钮，并点击
        fight_bidding_path="//span[text()=' 全栈一期web自动化测']/ancestor::a/following-sibling::div//a[text()='抢投标']"
        WebDriverWait(self.browser, 10, 1).until(EC.element_to_be_clickable((By.XPATH, fight_bidding_path)))  # 判断抢投标按钮可点击
        self.browser.find_element_by_xpath(fight_bidding_path).click()    #点击抢投标按钮

        #在新打开的投标界面找到投标金额输入框并传入数值1000
        tendetnum_path="//input[@data-url='/Invest/invest']"
        WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, tendetnum_path)))  # 判断金额输入框可见
        self.browser.find_element_by_xpath(tendetnum_path).send_keys("1000")

        #找到投标按钮并点击
        bidding_path="//input[@data-url='/Invest/invest']//parent::div//parent::div//following-sibling::button"
        WebDriverWait(self.browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, bidding_path)))  # 判断投标按钮可点击
        self.browser.find_element_by_xpath(bidding_path).click()
        #记录投标操作时间
        global tender_time
        tender_time=time.strftime('%Y-%m-%d %H:%M')

        #定位到弹出的投标成功界面并点击右上角x按钮关闭该页面
        bidding_success_close_path="//div[@class='layui-layer-content']//div//div//img[contains(@src,'close')]"
        WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, bidding_success_close_path)))  # 判断投标成功界面右上角x按钮可见
        self.browser.find_element_by_xpath(bidding_success_close_path).click()

    # 检查投标项目
    def checkTender(self):
        # 找到我的账户按钮元素并点击
        my_account_path="//a[@href='/Member/index.html']"
        WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, my_account_path)))   #判断我的账户按钮可见
        self.browser.find_element_by_xpath(my_account_path).click()

        # 找到投资项目按钮元素并点击
        investment_projects_path="//div[text()='投资项目']"
        self.browser.execute_script("arguments[0].scrollIntoView();", self.browser.find_element_by_xpath(investment_projects_path))    #将网页滚动到投资项目按钮处，使其在屏幕中显示
        WebDriverWait(self.browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, investment_projects_path)))    #判断投资项目按钮可点击
        self.browser.find_element_by_xpath(investment_projects_path).click()

        # 找到投资项目列表中每个投标单位的投标日期和时间元素
        tender_see_date_path="//div[@ms-html='item.date']"
        WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, tender_see_date_path)))   #判断投标单位的日期元素可见
        self.tender_see_date = self.browser.find_elements_by_xpath(tender_see_date_path)     #将所有日期元素保存在self.tender_see_date列表里

        tender_see_time_path = "//div[@ms-html='item.time']"
        WebDriverWait(self.browser, 5, 1).until(EC.visibility_of_element_located((By.XPATH, tender_see_time_path)))    #判断投标单位的时间可见
        self.tender_see_time = self.browser.find_elements_by_xpath(tender_see_time_path)   #将所有时间元素保存在self.tender_see_time列表里

    # 对比投标项目
    def compareTender(self):
        for i in range(len(self.tender_see_date)):
            if self.tender_see_date[i].text+" "+self.tender_see_time[i].text==tender_time:
                #将对比投标项目中为刚才自己投的标背景高亮显示
                self.browser.execute_script("arguments[0].setAttribute('style', arguments[1]);", self.browser.find_elements_by_xpath("//div[@ms-controller='tz_list']//tr")[i],"background: yellow; border: 2px solid red;")
                print("第 %s 条投标记录为刚才您投的标"%(i+1))
                break
            else:
                # 当前页面没找到自己投的标，找到下一页按钮并点击
                next_page_path="//div[@ms-controller='tz_list']//a[text()='下一页']"
                WebDriverWait(self.browser, 5, 1).until(EC.element_to_be_clickable((By.XPATH, next_page_path)))  # 判断下一页按钮可点击
                self.browser.find_element_by_xpath(next_page_path).click()
                # 递归对比函数
                self.compareTender()

    # 关闭浏览器函数
    def closeBrowser(self):
        time.sleep(3)
        self.browser.close()  # 关闭当前窗口
        self.browser.quit()  # 关闭浏览器

#测试代码
test_selenium=HighElementLocation()
test_selenium.loginWebsite()
test_selenium.submitTenders()
test_selenium.checkTender()
test_selenium.compareTender()
test_selenium.closeBrowser()
