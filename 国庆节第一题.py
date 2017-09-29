#-*-coding:utf-8-*-
import requests

class HttpRequest:
    def __init__(self,data,function,method,url="http://119.23.241.154:8080/futureloan/mvc/api/member/"):
        self.url = url
        self.data = data
        self.function=function
        self.method=method

    def recharge(self):
        if self.method=="GET" or self.method=="get":
            try:
                result = requests.get(self.url+self.function,self.data)
                print(result.text)
            except Exception as e:
                print("出错了！%s"%e)

        elif self.method=="POST" or self.method=="post":
            try:
                result = requests.post(self.url+self.function,self.data)
                print(result.text)
            except Exception as e:
                print("出错了！%s"%e)

        else:
            print("请输入正确的传输方法")

    def login(self):
        self.recharge()

    def register(self):
        self.recharge()

recharge_data={"mobilephone":"13667692121","amount":1000}
result1=HttpRequest(recharge_data,"recharge","GET")
result1.recharge()

login_data={"mobilephone":"13667692121","pwd":"123456"}
reslult2=HttpRequest(login_data,"login","get")
reslult2.login()

register_data={"mobilephone":"13810737247","pwd":"123456"}
reslult3=HttpRequest(register_data,"register","POST")
reslult3.register()