#1.写入一段文字到TXT中，相对头部偏移5个位置，读取出出偏移后的文字
#前提D:\\123.txt文件存在
try:
    f=open("D:\\123.txt",'w+')
    f.write("四葉棒棒哒美华华老师教的也老给力了！")
except IOError as e:
    print("出错啦%s"%e)
else:
    #f.write("四葉棒棒哒美华华老师教的也老给力了！")
    f.seek(10,0)
    print(f.read())
    print("文件写入成功")
    f.close()

#2.txt里面存了很多数据，都是用逗号隔开的，一个逗号隔开的就是一个数据，一个数据对应列表里面的一个元素。怎么样才能把这些数据读取到出来并且存到list中。
#前提D:\\1234.txt存在，且内容为1,2,3,4,5,6,7,8,9,10这种情况
try:
    f = open("D:\\1234.txt", 'a+')
except IOError as e:
    print("出错啦%s"%e)
else:
    f.seek(0, 0)
    list=f.read().split(',')
    list2=[]
    for i in list:
        list2.append(i)
    print("读取文件后直接转化为列表，表现为：",list2)
    for j in range(len(list2)):
        try:
            float(list2[j])
        except:
            list2[j] = list2[j]
        else:
            if str(float(list2[j]))==list2[j]:
                list2[j] = float(list2[j])
            else:
                list2[j] = list2[j]
        try:
            int(float(list2[j]))
        except:
            list2[j] = list2[j]
        else:
            if str(int(float(list2[j]))) == list2[j]:
                list2[j] = int(float(list2[j]))
    print("经过对数据进行调整达到满足条件后，表现为",list2)
    f.close()
    print("----------------------------------------------------------------------------------------------------------\n")



#3.txt中存了很多数据，一行为一个数据，怎么样才能把这些数据读取到并且存到list中。 请在代码里面做好try except 异常判断处理。
#前提D:\\12345.txt存在，且内容为内容1回车内容2回车内容3回车内容4回车内容5回车。。。。这种情况，其中每行内容可以纯数字，字符，小数，负数等各种类型
try:
    f = open("D:\\12345.txt", 'a+')
except IOError as e:
    print("出错啦%s"%e)
else:
    f.seek(0, 0)
    list=f.read().split('\n')
    print("读取文件后直接转化为列表，表现为：", list)
    list2 = []
    for i in list:
        list2.append(i)
    for j in range(len(list2)):
        try:
            float(list2[j])
        except:
            list2[j] = list2[j]
        else:
            if str(float(list2[j]))==list2[j]:
                list2[j] = float(list2[j])
            else:
                list2[j] = list2[j]
        try:
            int(float(list2[j]))
        except:
            list2[j] = list2[j]
        else:
            if str(int(float(list2[j]))) == list2[j]:
                list2[j] = int(float(list2[j]))
    print("经过对数据进行调整达到满足条件后，表现为", list2)
    f.close()