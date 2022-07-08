import random


training = [
    {
        'input' : [0 , 1],
        'targets' : [1]
    },

    {
        'input' : [1 , 0],
        'targets' : [1]
    },

    {
        'input' : [0 , 0],
        'targets' : [0]
    },

    {
        'input' : [1 , 1],
        'targets' : [0]
    },

]



i = random.choice(training)
# for i in training:
print(i['input'] , i['targets'])