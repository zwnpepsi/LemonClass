mark=input("请输入你的成绩")
if mark.isalpha():
    print("请输入数字")
elif int(mark)<0:
    print("请输入0-100之前的数字")
elif   int(mark)>100:
    print("请输入0-100之前的数字")
elif int(mark)>=60:
    print("恭喜你及格")
else:
    print("非常遗憾的告诉你，你没有及格")



print(list(range(-1,5,1)))
a=[1,5,7,9,10,11]
list=[]
for i in range(6):
    list.insert(0,a[i])
print(list)

b=[1,5,7,9,10,11]
b.reverse()
print(b)