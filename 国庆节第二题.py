#-*-coding:utf-8-*-
import random
class RandomMessage:
    def __init__(self,sequence,k):
        self.sequence = sequence
        self.k = k

    def RandomSample(self):
        try:
            sample = random.sample(self.sequence,self.k)
            return sample
        except Exception as e:
            print("出错了！%s" % e)

    def ListToStr(self):
        try:
            list = self.RandomSample()
            name = ''.join(list)
            return name
        except Exception as e:
            print("出错了！%s" % e)

    def RandintInt(self,a,b):
        try:
            age = random.randint(a,b)
            return age
        except Exception as e:
            print("出错了！%s" % e)

    def ChoiceSex(self):
        try:
            sex = random.choice(["男","女"])
            return sex
        except Exception as e:
            print("出错了！%s" % e)

    def OutputMessage(self,a,b):
        print("姓名：%s ,年龄：%s, 性别: %s"%(self.ListToStr(),self.RandintInt(a,b),self.ChoiceSex()))


sequence=["Lisa","sisi","xiaohei","ergui","zhizhuo","siye","yuangungun"]
result=RandomMessage(sequence,2)
print("随机指定长度为1的列表为：",result.RandomSample())
print("随机指定长度为1的列表转化为字符串后为：",result.ListToStr())
result.OutputMessage(18,40)