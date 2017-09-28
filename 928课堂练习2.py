import requests

class Req:
    def __init__(self,data,method,url="http://119.23.241.154:8080/futureloan/mvc/api/member/"):
        self.url = url
        self.data = data
        self.method=method

    def recharge(self):
        try:
            result = requests.get(self.url+self.method,self.data)
            print(result.text)
        except Exception as e:
            print("出错了！%s"%e)

    def login(self):
        self.recharge()

    def register(self):
        self.recharge()

result1=Req({"mobilephone":"13667692121","amount":1000},"recharge")
result1.recharge()

'''print(Req({"mobilephone":"13667692121","amount":1000},"login"))
print(Req({"mobilephone":"13667692121","amount":1000},"register"))'''