# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/23 20:19
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : robotframework_test.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import warnings

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from SeleniumLibrary.base import DynamicCore
from SeleniumLibrary.keywords import (AlertKeywords,
                                      BrowserManagementKeywords,
                                      CookieKeywords,
                                      ElementKeywords,
                                      FormElementKeywords,
                                      JavaScriptKeywords,
                                      RunOnFailureKeywords,
                                      ScreenshotKeywords,
                                      SelectElementKeywords,
                                      TableElementKeywords,
                                      WaitingKeywords)
from SeleniumLibrary.locators import ElementFinder, TableElementFinder
from SeleniumLibrary.utils import (BrowserCache, Deprecated, LibraryListener,
                                   timestr_to_secs)

