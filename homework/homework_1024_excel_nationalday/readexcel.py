# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/25 14:32
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : readexcel.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import xlrd
import tkinter.filedialog

class ReadExcel:
    def __init__(self):
        pass

    def read_excel(self):
        workbook = xlrd.open_workbook(tkinter.filedialog.askopenfilename(title="打开指定的excle文档"))
        sheet_obj = workbook.sheets()[0]  # 获取sheet1   #根据索引获取excel里面的表单对象
        result=[]
        for i in range(1,sheet_obj.nrows,1):
            result.append(sheet_obj.row_values(i))
        return result


#测试代码
# a=ReadExcel()
# a.read_excel()
