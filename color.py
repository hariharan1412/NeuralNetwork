import random
import numpy as np


class dataSet:

    def __init__(self):

        self.x = random.randint(1 , 2)
        self.y = random.randint(1 , 2)
        # print(self.x , self.y)

        if self.x == 1 and self.y == 1:
            self.label = 1
        else:
            self.label = 2

class Precptron:

    def __init__(self):
        
        self.weight = [random.uniform(-1 , 1) for i in range(2)]
        self.lr = 0.1
        
    def sign(self , s):    

        if s >= 0.5:
            return 2
        return 1

    def guess(self , input):
        
        self.s = 0
        for i in range(2):
            self.s +=  input[i] * self.weight[i] 
        
        h = 1 / (1 + np.exp(-self.s))
        return self.sign(h)

    def train(self , input , target):
        
        self.result = self.guess(input)
        self.error = target - self.result
     
        for i in range(len(self.weight)):
            self.weight[i] += self.error * input[i] * self.lr

p = Precptron()
n = 10000
points = [dataSet() for i in range(n)]

s , n = 0 , 0 
for i in points:
    val = [i.x , i.y]
    target = i.label
    p.train(val , target)

i = [1 , 1]

re = lambda x :  "Red" if x == 1  else "Blue"
print( re(p.guess(i)))
