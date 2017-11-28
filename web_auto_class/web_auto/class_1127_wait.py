# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/27 22:02
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : class_1127_wait.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


browser = webdriver.Chrome()
browser.maximize_window()#最大化窗口
browser.get('http://www.baidu.com/')

# login_access="//*[@id='u1']//a[text()='登录']"
# WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,login_access)))
# browser.find_element_by_xpath(login_access).click()
#
# login_popup="//*[@id='TANGRAM__PSP_10__userName']"
# WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.XPATH,login_popup)))
# browser.find_element_by_xpath(login_popup).send_keys("111111")

xuantingweizhi=browser.find_element_by_xpath("//*[@id='u1']/a[text()='设置']")
ActionChains(browser).move_to_element(xuantingweizhi).perform()


time.sleep(2)

browser.find_element_by_xpath("//div[@class='bdpfmenu']//a[text()='高级搜索']").click()
