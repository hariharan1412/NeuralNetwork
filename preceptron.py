import random
import pygame
import time

pygame.init()
width , heigth = 400 , 400
screen = pygame.display.set_mode((width , heigth))


class Point:

    def __init__(self):
        self.x = random.randint(0 , width)
        self.y = random.randint(0 , heigth)

        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1     

class Preceptron:

    def __init__(self):
        self.weight = [random.uniform(-1 , 1) for i in range(2)]
        self.lr = 0.1
        self.bias = 1

    def sign(self, s):
       
        if s >= 0:
            return 1
        else:
            return -1        


    def guess(self , input):
        self.sum = 0 

        for i in range(len(self.weight)):
            self.sum += input[i] * self.weight[i]

        self.sum += self.bias

        a = self.sign(self.sum)
        return a

    def train(self , input , target):
        
        self.result = self.guess(input)
        self.error = target - self.result

        for i in range(len(self.weight)):
            self.weight[i] += self.error * input[i] * self.lr
        
        self.bias = self.bias + self.lr * self.error
n = 500
p = Preceptron()

points = [Point() for i in range(n)]
color = (0 , 0 , 255)
done = False

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_n:
                del points
                del p
                p = Preceptron()
                points = [Point() for i in range(n)]

            if event.key == pygame.K_t:
                for i in points:
                    input = [i.x , i.y]
                    target = i.label
                    p.train(input , target)
            

            if event.key == pygame.K_j:
                for i in range(1000):
                    for i in points:
                        input = [i.x , i.y]
                        target = i.label
                        p.train(input , target)


    screen.fill((255 ,255 , 255))

    for i in points:
        input = [i.x , i.y]
        target = i.label
        guess = p.guess(input)
        
        if guess == target:
            print(f"GUESS : {guess} , TARGET : {target} IN")
            color = (0 , 255 , 0)
        else:
            print(f"GUESS : {guess} , TARGET : {target} OUT")
            color = (255 , 0 , 0)

        pygame.draw.circle(screen , color , (i.x , i.y) , 4)
        
    pygame.draw.line(screen , (0 , 0 , 0 ) , (0 ,0), (width , heigth))
    pygame.display.update()
    # del points
    # print()