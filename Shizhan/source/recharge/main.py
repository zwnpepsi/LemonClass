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
    # 创建http请求对象
    # http_request_obj=HttpRequest(projectpath.http_config)

    logger = CollectLog("充值操作").collectLog()

    #从Excel里面读取测试数据

    result = ReadData(projectpath.testdata_path + "\\recharge_data.xlsx", "RECHARGE_MODE", "RECHARGE_CASELIST",
                      logger).getData()
    # mode=Mode(globalparam.mode_config).get_mode()
    # case_list=Mode(globalparam.mode_config).get_case_list()
    # test_data=ReadData(mode,case_list).get_data(projectpath.testdata_path+"")

    #创建存储数据的Excel对象
    # save_data_obj=SaveData("recharge_test_result")
    run_result = Recharge(result,logger)
    filepath=run_result.recharge()
    # filepath=MemberRecharge(http_request_obj,test_data,save_data_obj).recharge()

    #发送邮件

    sendEmail=SmtpResults(projectpath.smtp_path).MailSend([filepath])