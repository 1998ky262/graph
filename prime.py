import math
from matplotlib import pyplot as pyp
def prime_tf(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    a = math.ceil(math.sqrt(num))
    for i in range(2, a+1):
        if num % i == 0:
            return False
    return True
z=0
data=[]
data2=[]
for b in range(50):
    data2.append(z)
    count = 0
    for c in range(1000):
        z+=1
        if(prime_tf(z)):
            count+=1
    data.append(count)
pyp.plot(data2,data,marker="o")
pyp.show()
#素数の割合は反比例の関数に近似して基本的に減少していく
