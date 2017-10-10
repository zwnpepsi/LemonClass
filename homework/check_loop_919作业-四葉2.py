# 1.根据你输入的数据，来进行判断学生的成绩。输入数据函数：input()
def grade(value, value2=0):
    count = value + value2/10
    if 85 <= count <=100:
        print("恭喜你，你得分优秀!!!")
    elif 60 <= count < 85:
        print("恭喜你，你及格了!")
    elif 0 <= count <60:
        print("小伙加油吧，你没及格!!!")

    if count > 100 or count < 0:
        print("你咋不上天呢，请输入0-100内的分数")
        return True
    else:
        return False


def check_input():
    score = input("请输入你的分数：")
    if score.isdigit():
        if grade(int(score)) == True:
            check_input()
    else:
        scoreArr = score.split('.')
        arrLength = len(scoreArr)

        if arrLength <= 2:
            limit1 = False
            limit2 = True
            decimal = 0
            if scoreArr[0].isdigit():
                limit1 = int(scoreArr[0]) <= 100

            if arrLength == 2:
                if scoreArr[1].isdigit() and int(scoreArr[1]) < 10:
                    limit2 = True
                    decimal = int(scoreArr[1])
                else:
                    limit2 = False

            if limit1 and limit2:
                grade(int(scoreArr[0]), decimal)
            else:
                print("输入错误1：")
                check_input()
        else:
            print("输入错误2：")
            check_input()
check_input()
print("----------------------------------------------------------\n")

# 2.利用刚刚说的的for循环和range()函数，完成1-100的累加计算
s = 0
for i in range(1, 101, 1):  # 取1-100整数
    s = s + i  # 进行累加操作
print("1-100累加值为：",s)
print("----------------------------------------------------------\n")

# 3.完成这个列表的输出a=[5,6,7,9,10,23,45],要求是：把数据按照倒序输出。
a = [5, 6, 7, 9, 10, 23, 45]
a.reverse()  # 使用python内置函数reverse进行倒序排序 和a.sort(reverse=Ture)有啥区别啊
print("通过系统函数进行倒序排序，结果为:",a)
print("----------------------------------------------------------")

a = [5, 6, 7, 9, 10, 23, 45]
list = []
for i in range(7):
    list.insert(0, a[i])  # 将列表中每一个数值都重新插入到list列表中的第一个位置，这样后插入的就排在前面
print("通过列表插入进行倒序排序，结果为:",list)
print("----------------------------------------------------------\n")

# 4.利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序： 冒泡排序：小的排前面，大的排后面。
a = [1, 7, 4, 89, 34, 2]
for i in range(6):  # i取0-6
    for j in range(i):  # j取0-5
        if a[j] > a[i]:
            a[j], a[i] = a[i], a[j]  # 如果前面数值大于后面数值，将两个数值调换
        #else:
            #continue
print("对列表a进行冒泡排序，结果为:",a)
