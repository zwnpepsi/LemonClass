test_data=[
    ["http://119.23.241.154:8080/futureloan/mvc/api/member/recharge","13667692121",1000,"GET"],
    ["http://119.23.241.154:8080/futureloan/mvc/api/member/recharge","13667692121",2000,"POST"]
    ]

#测试数据解析：这是一个二维列表，我们在课堂作业讲过test_data[0][1] 读取的是什么数据？
#要知道数据结构，数据分别是：请求URL地址  充值手机号码  充值金额  http请求方法

import  requests

def HttpRequest(list):

    for i in  range(len(list)):
        #获得请求的url
        url = list[i][0]

        #获得请求的数据
        data = {"mobilephone":list[i][1],"amount":list[i][2]}

        #获得http请求方法
        http_method = list[i][3]

        #根据获得的请求方法来判断是调用get请求还是post请求
        if http_method == 'GET':
            try:
              result=requests.get(url,data)
              #return result.text
              print(result.text)
            except Exception as e:
                print("get请求出错啦！%s"%e)
        else:
            try:
              result=requests.post(url,data)
              #return result.text
              print(result.text)
            except Exception as e:
              print("get请求出错啦！%s"%e)

HttpRequest(test_data)




