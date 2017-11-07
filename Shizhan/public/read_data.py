# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/7 21:43
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : read_data.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import  xlrd

class ReadData:
    def __init__(self,file_path):
        self.file_path=file_path

    def getData(self):
        workbook = xlrd.open_workbook(self.file_path)
        sheet_obj = workbook.sheets()[0]  # 获取sheet1   #根据索引获取excel里面的表单对象
        result=[]
        for i in range(1,sheet_obj.nrows,1):
            result.append(sheet_obj.row_values(i))
        return result