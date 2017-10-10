class People:

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex


    def Sing(self):
        return self.name,self.age,self.sex,"不爱唱歌"

    def Dance(self):
        return self.name,self.age,self.sex, "不爱跳舞"

    def Swim(self):
        return self.name,self.age,self.sex, "不爱游泳"

    def Climb(self):
        return self.name,self.age,self.sex, "不爱爬树"

    def Code(self):
        return self.name,self.age,self.sex, "爱写代码"

t=People("sisi",10,"男")
print(t.Sing())
print(t.Dance())
print(t.Swim())
print(t.Climb())
print(t.Code())