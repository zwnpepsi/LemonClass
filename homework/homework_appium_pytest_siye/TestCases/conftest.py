# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/7 23:47
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : conftest.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from appium import webdriver
import pytest
from homework.homework_appium_pytest_siye.Common.projectpath import *


@pytest.fixture()
def init_driver():
    desired_caps = eval(ReadConfig().readConfig(os.path.join(project_path,"Common","app_info.conf"),"APP_INFO","desired_caps"))
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()