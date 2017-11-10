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
    def __init__(self,sheet_name,logger):
        self.sheet_name=sheet_name
        self.logger=logger
        self.wb = xlwt3.Workbook()  # 获取一个工作表,创建一个对象
        self.sheet = self.wb.add_sheet(self.sheet_name)  # 创建一个表单

    def writeData(self,i,result):
        try:
            self.sheet.write(i, 0, i+1)
            self.sheet.write(i, 1, result)
            self.logger.info("写入Excel成功")
        except Exception as e:
            self.logger.error('写入Excel出错啦！错误参数是：%s' % e)

    def saveData(self,path):
        try:
            self.wb.save(path)
            self.logger.info("保存Excel成功")
        except Exception as e:
            self.logger.error('保存Excel出错啦！错误参数是：%s' % e)
