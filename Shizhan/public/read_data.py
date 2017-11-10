# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/11/7 21:43
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : read_data.py
# @Software: PyCharm
#-------------------------------------------------------------------------------
import  xlrd
from Shizhan.public import projectpath
from Shizhan.public.read_mode import ReadMode


class ReadData:
    def __init__(self,file_path,mode_option,caselist_option,logger):
        self.file_path=file_path
        self.readmode_obj=ReadMode(projectpath.flag_path,mode_option,caselist_option)
        self.logger=logger


    def getData(self):
        if self.readmode_obj.getMode()==1:
            try:
                workbook = xlrd.open_workbook(self.file_path)
                sheet_obj = workbook.sheets()[0]  # 获取sheet1   #根据索引获取excel里面的表单对象
                result=[]
                for i in range(1,sheet_obj.nrows,1):
                    result.append(sheet_obj.row_values(i))
                self.logger.info("全部读取文件正确")
            except Exception as e:
                self.logger.error('全部读取文件出错啦！错误参数是：%s' % e)
            finally:
                return result

        else:
            try:
                workbook = xlrd.open_workbook(self.file_path)
                sheet_obj = workbook.sheets()[0]  # 获取sheet1   #根据索引获取excel里面的表单对象
                result = []
                for i in self.readmode_obj.getCase_list():
                    result.append(sheet_obj.row_values(i))
                self.logger.info("按需读取文件正确")
            except Exception as e:
                self.logger.error('按需读取文件出错啦！错误参数是：%s' % e)
            finally:
                return result