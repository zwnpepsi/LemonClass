# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/10/26 21:15
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : class_1026_xlsxwriter.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import xlsxwriter
import tkinter.filedialog
workbook = xlsxwriter.Workbook(tkinter.filedialog.asksaveasfilename(filetypes=[('xls','.xls'),('xlsx','.xlsx'),('All file','*')],
                                                     title="保存指定的excel文档",defaultextension='.xlsx'))
worksheet=workbook.add_worksheet()

# worksheet.write(i,j,value)   #写数据

#增加表格设置
format=workbook.add_format()
format.set_font_color("red")
format.set_font_size("12")
format.set_bold(bold=True)
format.set_bg_color("yellow")

worksheet.write(0,0,"111")
worksheet.write_string(1,0,"121",format)
worksheet.write_number(1,1,333,format)


worksheet.insert_image(4,4,"logo.jpg")


workbook.close()   #关闭等同于xlwt3的保存