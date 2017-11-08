# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/7 22:06
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : write_data.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import xlwt3

class WriteData:
    def __init__(self,sheet_name):
        self.sheet_name=sheet_name
        self.wb = xlwt3.Workbook()  # 获取一个工作表,创建一个对象
        self.sheet = self.wb.add_sheet(self.sheet_name)  # 创建一个表单

    def writeData(self,i,result):
        self.sheet.write(i, 0, i+1)
        self.sheet.write(i, 1, result)

    def saveData(self,path):
        self.wb.save(path)