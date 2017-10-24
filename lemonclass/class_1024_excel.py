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
from datetime import datetime

class ExcelDemo:
    def __init__(self):
        self.style0=style0 = xlwt3.easyxf('font: name Times New Roman, color-index red, bold on',
                            num_format_str='#,##0.00')
        self.style1 = xlwt3.easyxf(num_format_str='D-MMM-YY')
        pass

    def ExcelOpen(self):
        workbook=xlrd.open_workbook(tkinter.filedialog.askopenfilename(title="打开指定的excle文档"))
        sheet_obj = workbook.sheets()[0] #获取sheet1   #根据索引获取excel里面的表单对象
        #row1=sheet_obj.row_values(0)     #获取第1行的值
        col1=sheet_obj.col_values(0)     #取第1列的值
        # print(col1)
        for i in range(sheet_obj.nrows):
            print(col1[i])

    def ExcelWrite(self):
        wb = xlwt3.Workbook()  # 获取一个工作表,创建一个对象
        sheet = wb.add_sheet("test")    #创建一个表单
        sheet.write(0, 0, 1234.56, self.style0)
        sheet.write(1, 0, datetime.now(), self.style1)
        sheet.write(2, 0, 1)
        sheet.write(2, 1, 1)
        sheet.write(2, 2, xlwt3.Formula("A3+B3"))
        sheet.write(3, 1, 1)
        wb.save(tkinter.filedialog.asksaveasfilename(filetype=[('xls','.xls'),('xlsx','.xlsx')],
                                                     title="保存指定的excle文档",defaultextension='.xls'))

#测试代码
file=ExcelDemo()
file.ExcelWrite()
file.ExcelOpen()


'''帮助文档
1：workbook=xlrd.open_workbook(path) 打开excel，path是指excel所在的路径
2：workbook.sheet_names() 获取excel里面的所有表单名
3：sheet_obj=sheets()[0] 根据索引获取excel里面的表单对象
4：sheet_obj=sheet_by_index(0) 根据顺序索引获取表单对象
5：sheet_obj=sheet_by_name('summer') 通过名称获取表单对象
6：sheet_obj.nrows 获取行数
7：sheet_obj.ncols 获取列数
8：sheet_obj.row_values(0) 获取第1行的值
9：sheet_obj.col_values(1) 获取第2列的值
10：sheet_obj.cell_value(1,2)   第2行第3列的值
'''

'''写入数据到excel的常用方法：
1：wb=xlwt3.Workbook()#获取一个工作表,创建一个对象
2：sheet=wb.add_sheet("summer & python&2") 创建一个表单
3：sheet.write(i,j,value[i][j]) 确定好位置写入具体的值
4：wb.save(path) 把你写入的数据保存好，一定要记得操作，不然数据就没有正常保
存啦！
操作顺序：
先创建一个excel对象---新建一个表单对象---插入数据---保存excel'''

