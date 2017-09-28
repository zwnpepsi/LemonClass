

class Math:
    def __init__(self,a,b=10):
        self.a=a
        self.b=b

    def sum(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

result1=Math(15)
result2=Math(12,5)
print(result1.sum())
print(result2.sub())