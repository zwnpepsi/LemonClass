#第一题 a=5,b=9,如何交换着两个值
a=5
b=9
a,b=b,a
print("a=",a)
print("b=",b)
print("\n")

#第二题  输入一个标准的日期如(20160503)，打印对应的年月日即2016年05月03日 a=input("请输入对应的日期")
while True:
    a = input("请输入对应的日期")
    if len(a)!=8:
         print("日期格式不正确，请重新输入8位数字日期")
    elif int(a[4:6])>12 or int(a[4:6])==00:
        print("输入的月份不正确，请输入01-12中的月份数字")
    elif int(a[6:])>31 or int(a[6:])==00:
        print("输入的日期不正确，请输入01-31中的日期数字")
    else:
        break

print("输入的日期为：", a[0:4], '年', a[4:6], '月', a[6:], '日')
print('\n')

'''第三题有一个字符串str=”python”,利用for..in 方法，把str里面的元素变成列表元素，最后效果如下：list=['p','y','t','h','o','n']
注意：提交代码请用自己的名字命名'''
str="python"
list=[]
for i in str:
    list.append(i)
print("list=",list)

