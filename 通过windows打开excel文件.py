#-*-coding:utf-8-*-
import win32ui
import tkinter.filedialog
import os
import xlrd
def sortRename():
    '''dlg = win32ui.CreateFileDialog(1,"111")   #通过win32ui库打开Windows自带选择框打开文件
    dlg.SetOFNTitle("打开总表文件")            #选择框默认名称
    dlg.SetOFNInitialDir('C:')                   #选择框默认位置
    dlg.DoModal()
    filename = dlg.GetPathName()'''
    filename2 = tkinter.filedialog.askopenfilename()     #通过tikinter库调用windows选择框打开指定文件

    directoryname =tkinter.filedialog.askdirectory()    #通过tikinter库调用windows选择框打开指定目录
    try:
        data = xlrd.open_workbook(filename2)
    except Exception as  e:
        print("文件打开错误 %s"%e)
    else:
        table = data.sheets()[0] #获取sheet1
        number=table.col_values(0) #第1列序号
        name=table.col_values(1) #第2列名称
        os.chdir(directoryname) #指定目录位置
        for i in range(len(name)):
            for j in range(len(name)):
                name2=os.listdir()    #定义指定目录下所有文件或文件夹的名字
                if str(name2[j]).encode('utf-8')==str(name[i]).encode('utf-8'):  #判断指定文件夹名称与excel文档中名称相等
                    newname1=int(number[i]),'-',name2[j]    #定义新名字为序号+“-”+原名字，新名字类型为元组
                    newname2=""                             #定义最终新名字为字符串
                    for k in newname1:
                        newname2 +=str(k)                  #将元组内元素转化为字符串
                    print(newname2)                        #打印最终名字
                    os.rename(name2[j], str(newname2))     #对文件夹进行重命名

sortRename()

