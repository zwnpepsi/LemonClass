# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/25 14:32
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : writeexcel.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import xlwt3
import tkinter.filedialog
class WriteExcel:
    def __init__(self):
        self.wb = xlwt3.Workbook()  # 获取一个工作表,创建一个对象
        self.sheet = self.wb.add_sheet("test")  # 创建一个表单

    def write_excel(self,i,result):
        self.sheet.write(i, 0, result)

    def save_excel(self,path=tkinter.filedialog.asksaveasfilename(filetypes=[('xls','.xls'),('xlsx','.xlsx'),('All file','*')],
                                                     title="保存指定的excel文档",defaultextension='.xls')):
        self.wb.save(path)


#测试代码
# a=WriteExcel()
# for i in range(10):
#     a.write_excel(i,"111")
# a.save_excel()