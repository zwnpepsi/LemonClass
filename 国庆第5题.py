#-*-coding:utf-8-*-
import tkinter.filedialog
class TransmitIP:
    def __init__(self,ip):
        self.ip=ip

    def ReadTestData(self):
        try:
            filename=tkinter.filedialog.askopenfilename()
            data=open(filename)
            data.seek(0,0)
        except IOError as e:
            print("出错啦%s" % e)
        else:
            list = data.read().split('\n')
            sum_data=[]
            for i in range(len(list)):
                list2=list[i].split(",")
                url=list2[0]
                data={"mobilephone":list2[1],"amount":list2[2]}
                method=list2[3]
                result=[self.ip+url,data,method]
                sum_data.append(result)
                i+=1
            return sum_data




a=TransmitIP("http://192.168.1.1:8080")
print(a.ReadTestData())