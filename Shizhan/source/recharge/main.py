# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/15 13:40
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : main.py
# @Software: PyCharm
#-------------------------------------------------------------------------------


from Shizhan.public import projectpath
from Shizhan.public.collect_log import CollectLog
from Shizhan.public.read_data import ReadData
from Shizhan.source.recharge.recharge import Recharge
from Shizhan.public.smtp_results import SmtpResults




if __name__ == '__main__':
    # 创建logger
    logger = CollectLog("充值操作").collectLog()

    #从Excel里面读取测试数据
    result = ReadData(projectpath.testdata_path + "\\recharge_data.xlsx", "RECHARGE_MODE", "RECHARGE_CASELIST",
                      logger).getData()

    #创建存储数据的Excel对象
    run_result = Recharge(result,logger)
    filepath=run_result.recharge()

    #发送邮件
    sendEmail=SmtpResults(projectpath.smtp_path).MailSend([filepath])