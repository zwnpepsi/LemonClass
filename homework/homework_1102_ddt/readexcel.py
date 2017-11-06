# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/25 14:32
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : readexcel.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import xlrd
import  configparser

class ReadExcel:
    def __init__(self,config):
        self.config=config
        self.cf = configparser.ConfigParser()
        # 读取配置文件
        self.cf.read(self.config, encoding="utf-8")
    def read_excel(self):
        workbook = xlrd.open_workbook("1102作业读取数据源.xlsx")
        sheet_obj = workbook.sheets()[0]  # 获取sheet1   #根据索引获取excel里面的表单对象
        if int(self.cf.get("FLAG","mode"))==1:
            result=[]
            for i in range(1,sheet_obj.nrows,1):
                result.append(sheet_obj.row_values(i))
            return result

        elif int(self.cf.get("FLAG","mode"))==0:
            result = []
            # key = 1
            for i in eval(self.cf.get("FLAG","case_list")):
                result.append(sheet_obj.row_values(i))
                # result[key-1][0] = key
                # key += 1
            for j in range(len(eval(self.cf.get("FLAG","case_list")))):
                result[j][0]=j+1
            return result

        else:
            print("配置文件设置错误")

# 测试代码
# a=ReadExcel("config.conf")
# a.read_excel()
