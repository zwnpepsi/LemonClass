def printName(value):
    print("My name is",value)

printName(input())




def changeList(value):
    list = []
    for i in value:
        list.append(i)
    print(list)
changeList("Python")


def addInt(a,b):
    s = 0
    for i in range(a, b+1):  # 取1-100整数
        s = s + i  # 进行累加操作
    print(a,'---',b,"的累加值为：", s)

addInt(1,101)


