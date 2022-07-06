import random
import numpy as np


class dataSet:

    def __init__(self):

        self.x = random.randint(0 , 1)
        self.y = random.randint(0 , 1)
        
        if self.x and self.y:
            self.label = 1

        else:
            self.label = 0    

class Precptron:

    def __init__(self):
        
        
        self.weight = [random.uniform(-1 , 1) for i in range(2)]
        print(self.weight)
        self.lr = 0.1
        
    def sign(self , s):    

        if s >= 0.5:
            return 1
        return 0

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
n = 1
points = [dataSet() for i in range(n)]

s , n = 0 , 0 
for i in points:
    val = [i.x , i.y]
    target = i.label
    p.train(val , target)

i = [1 , 0]
print(p.guess(i))
