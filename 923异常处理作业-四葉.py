'''①有一组数据：放在字典里面的，如下所示：test_data=[ [“http://119.23.241.154:8080/futureloan/mvc/api/member/recharge”,”13667692121”,1000,”GET”], [“http://119.23.241.154:8080/futureloan/mvc/api/member/recharge”,”13667692121”,2000,”POST“] ]
第一个数据是：请求的url地址，第二个数据：充值的手机号码 mobilephone  第三个数据：充值的金额 amount 第四个数据：HTTP请求的方法
要求：1）根据test_data字典里面的http请求方法，利用requests去进行请求。
2）用到for循环、 if..else判断
3）要求返回测试结果
4）加上异常判断'''
import requests
test_data=[["http://119.23.241.154:8080/futureloan/mvc/api/member/recharge","13667692121",1000,"GET"],
           ["http://119.23.241.154:8080/futureloan/mvc/api/member/recharge","13667692121",2000,"POST"]]
#result=requests.get(test_data[0][0],mobilephone=test_data[0][1])
payload1 = {'mobilephone': test_data[0][1], 'amount': test_data[0][2]}
payload2 = {'mobilephone': test_data[1][1], 'amount': test_data[1][2]}
url=test_data[0][0]

def chargeGet(url,payload):
    try:
     result1=requests.get(url,payload)
    except Exception as e:
     print("充值出错，异常为%s"%e)
    else:
     print(result1.text)
     print(result1.json())
chargeGet(url,payload1)

def chargePost(url,payload):
    try:
     result2=requests.post(url,payload)
    except Exception as e:
     print("充值出错，异常为%s"%e)
    else:
     print(result2.text)
     print(result2.json())
chargePost(url,payload2)














