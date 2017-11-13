# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/13 12:08
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_run.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
from Shizhan.public.collect_log import CollectLog
from Shizhan.public.read_data import ReadData
from Shizhan.public import projectpath
from Shizhan.public.smtp_results import SmtpResults
from Shizhan.source.register.register import Register
from Shizhan.source.recharge.recharge import Recharge

# logger1=CollectLog("注册操作").collectLog()
# result1 = ReadData(projectpath.testdata_path+"\\register_data.xls","REGISTER_MODE","REGISTER_CASELIST",logger1).getData()
# run_result1 = Register(result1,logger1)
# mail=SmtpResults(projectpath.smtp_path)
# mail.MailSend(run_result1.register())

logger2=CollectLog("充值操作").collectLog()
result2 = ReadData(projectpath.testdata_path+"\\recharge_data.xlsx","RECHARGE_MODE","RECHARGE_CASELIST",logger2).getData()
run_result2 = Recharge(result2,logger2)
mail=SmtpResults(projectpath.smtp_path)
mail.MailSend(run_result2.recharge())




