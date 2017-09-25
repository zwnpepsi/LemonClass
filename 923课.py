'''import requests
url="http://119.23.241.154:8080/futureloan/mvc/api/member/register"
data={"mobilephone":"13888888888","pwd":"123456"}
result=requests.post(url,data)
print(result.url)
print(result.text)
print(result.json())'''

def redPacket(money=input("请输入发红包金额")):

    try:
        a=float(money)
    except  :
        #print("输入错误，请输入0.01-200间的金额")
        redPacket(input("输入错误，请输入0.01-200间的金额"))
    else:
        if a<=0 or a>200:
           # print("您输入的金额错误，请输入0.01-200间的金额")
            redPacket(input("输入错误，请输入0.01-200间的金额"))
        else:
            print("红包发送成功，您此次发红包的金额为 %s"%money)
redPacket()


try:
    f=open("C:\\Users\\张伟男\\Desktop\\123.txt",'w+')
    f.write("啊hi沙嗲黑色的")
    print(f.tell())
    f.seek(10,0)
    print(f.read())
except IOError as e:
    print("出错啦%s"%e)
else:
    print("文件写入成功")
    f.close()


