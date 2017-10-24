# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/24 14:47
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : class_1024_excel.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import xlrd
import xlwt3
import tkinter.filedialog

workbook=xlrd.open_workbook(tkinter.filedialog.askdirectory(title="打开指定的excle文档"))
#workbook.sheet_names()     #获取excel里面的所有表单名
sheet_obj = workbook.sheets()[0] #获取sheet1   #根据索引获取excel里面的表单对象

# sheet_obj=sheet_by_index(0) 根据顺序索引获取表单对象
# sheet_obj=sheet_by_name('summer') 通过名称获取表单对象
# sheet_obj.nrows 获取行数
# sheet_obj.ncols 获取列数
# sheet_obj.row_values(0) 获取第1行的值
# 9sheet_obj.col_values(1) 获取第2列的值
# sheet_obj.cell_value(1,1)

