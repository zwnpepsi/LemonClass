__author__ = '读取数据'

class SaveData:

    def __init__(self,path):
        self.path=path

    def save_data(self,result):
        file=open(self.path,"a+")
        file.write(result+"\n")
        file.close()
