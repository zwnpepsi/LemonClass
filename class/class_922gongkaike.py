import random

for i in range(0,10):
    tel=random.sample("0123456789",8)
    str="138"
    for i in tel:
        str+=i
    print(str)