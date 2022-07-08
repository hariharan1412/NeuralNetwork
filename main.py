from NN import NeuralNetwork
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

if __name__ == "__main__":

    nn = NeuralNetwork(2 , 2 , 1)

    for _ in range(1):
        # for i in training:
        i = random.choice(training)
        nn.train(i['input'] , i['targets'])
        # print(nn.feedforward(input))

    print(nn.feedforward([0 , 1]))
    print(nn.feedforward([1 , 0]))
    print(nn.feedforward([0 , 0]))
    print(nn.feedforward([1 , 1]))