#-*-coding:utf-8-*-
import os
import tkinter.filedialog

class DirOpen:
    def __init__(self):
        pass

    def dirOpen(self,path):
        try:
            os.chdir(path)
            f = open(r'D:\目录信息.txt', 'a+')
            f.write(path + "--------\n")
            f.seek(0, 2)
            # print(path + "---------")

        except Exception as  e:
            print("目录打开错误 %s" % e)

        else:
            name = os.listdir()
            for i in range(len(name)):
                if os.path.isdir(path + "/" + name[i]) == True:
                    self.dirOpen(path + "/" + name[i])
                    i += 1
                else:
                    # print(path + "/" + name[i])
                    f.write(path + "/" + name[i]+"\n")
        f.close()

dir=DirOpen()
dir.dirOpen(tkinter.filedialog.askdirectory(title="打开想要测试的目录"))


