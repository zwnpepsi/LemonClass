#1.对任意数字列表，编写一个函数，实现用冒泡排序法，对list进行一个排序。
def bubbleSort(list):
    for i in range(len(list)):
        for j in range(i):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]  # 如果前面数值大于后面数值，将两个数值调换
            else:
                continue
    print("对指定列表进行冒泡排序，结果为:", list)
    print("----------------------------------------------------------\n")

bubbleSort([1,3,5,15,21,4,2,7])


#2.对任意字符串，编写一个函数，实现转换成一个列表，每个字符对应列表里面的一个元素。
def strTolist(string):
    list=[]
    for i in range(len(string)):
        list.append(string[i])
    print(list)
    print("----------------------------------------------------------\n")

strTolist("pythonadhashida")


#3写一个函数，可以完成任意有序整数序列的和的计算：考虑下range函数
def addSum(int1,int2):
    s = 0
    for i in range(int1,int2+1):  #
        s +=  i  # 进行累加操作
    #print("您输入的数字序列",int1,"--",int2,"的累加值为：", s)
    print("您输入的数字序列%d--%d的累加值为："%(int1,int2), s)
    print("----------------------------------------------------------\n")

addSum(1,200)

#4写一个函数，输入任何列表，可以完成倒序的操作。
def reverseOutput(list):
    outList = []
    for i in range(len(list)):
        outList.insert(0, list[i])  # 将列表中每一个数值都重新插入到list列表中的第一个位置，这样后插入的就排在前面
    print("通过列表插入进行倒序排序，结果为:", outList)
    print("----------------------------------------------------------\n")
reverseOutput([1,2,3,4,5,6,7,8,9,10])

#5写一个函数，可以根据你输入的数字来判断是奇数还是偶数。
def checkOddorEven():
    value=input("请输入你要判断的数字：")
    if value.isdigit():
        if int(value) == 0:
            print("请输入非零整数")
            checkOddorEven()
        elif int(value)%2==0:
            print("您输入的数字 %s 为偶数"%value)
        else:
            print("您输入的数字 %s 为奇数"%value)
    else:
        print("请输入非零整数")
        checkOddorEven()

checkOddorEven()