import requests
class RequestsTest:
    url="http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
    data1 = {'mobilephone': '13667692121', 'amount': 1000}
    data2 = {'mobilephone': '13667692121', 'amount': 2000}

    def chargeGet(self):
        try:
            result1=requests.get(self.url,self.data1)
        except Exception as e:
            print("充值出错，异常为%s"%e)
        else:
            return result1.text

    def chargePost(self):
        try:
            result2=requests.post(self.url,self.data2)
        except Exception as e:
            print("充值出错，异常为%s"%e)
        else:
            return result2.text

object1=RequestsTest()
object2=RequestsTest()
print(object1.chargeGet())
print(object2.chargePost())