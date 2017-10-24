__author__ = '读取数据'

class ReadData:

    def __init__(self,path):
        self.path=path

    def read_data(self):
        file=open(self.path,"r+")
        result=file.readlines()#数据格式是列表
        return result
        file.close()

#测试代码
#t=ReadData("E:\\test_data.txt")
#print(t.read_data())
