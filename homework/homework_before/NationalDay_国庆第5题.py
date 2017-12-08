#-*-coding:utf-8-*-
import tkinter.filedialog
import requests
class TransmitIP:
    def __init__(self,ip):
        self.ip=ip

    def ReadTestData(self):
        try:
            filename=tkinter.filedialog.askopenfilename(title="打开作业压缩包内的指定测试数据")
            data=open(filename)
            data.seek(0,0)
        except IOError as e:
            print("出错啦%s" % e)
        else:
            list = data.read().split('\n')
            data.close()
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


class HttpRequest:
    def __init__(self,url,data,method):
        self.url = url
        self.data = data
        self.method=method

    def recharge(self):
        if self.method=="GET" or self.method=="get":
            try:
                result = requests.get(self.url,self.data)
                return result.text
            except Exception as e:
                print("出错了！%s"%e)

        elif self.method=="POST" or self.method=="post":
            try:
                result = requests.post(self.url,self.data)
                return result.text
            except Exception as e:
                print("出错了！%s"%e)

        else:
            print("请输入正确的传输方法")



class Storage:
    def __init__(self,result):
        self.result = result

    def storage(self,i):
        try:
            f = open(r'D:\第五题运行结果.txt', 'a+')
            f.write("请求URL：%s,请求数据：%s,请求结果：%s\n\n"%(result[i][0], result[i][1],
                              HttpRequest(result[i][0],result[i][1],result[i][2]).recharge()))
            f.close()
        except IOError as e:
            f = open(r'D:\第五题运行结果.txt', 'a+')
            f.write("出错啦%s\n" % e)
            f.close()


class LoopControl:
    def __init__(self,result):
        self.result = result

    def loopC(self):
        for i in range(len(result)):
            Storage(result[i]).storage(i)
            i+=1

ipconfig=TransmitIP("http://119.23.241.154:8080")
result=ipconfig.ReadTestData()
a=LoopControl(result)
a.loopC()



