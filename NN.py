from cv2 import Mat
from matirix import Matrix
import numpy as np 


class NeuralNetwork:

    def __init__(self , numI , numH , numO):
        self.input_nodes = numI
        self.hidden_nodes = numH
        self.output_nodes = numO

        self.lr = 0.1
 
        self.weight_ih = Matrix(self.hidden_nodes , self.input_nodes)
        self.weight_ho = Matrix(self.output_nodes , self.hidden_nodes)

        # self.bais_h    = Matrix(self.hidden_nodes , 1)
        self.bais_h    = Matrix(2 , 1)
        # self.bais_o    = Matrix(self.hidden_nodes , 1)
        self.bais_o    = Matrix(2, 1)
        
        self.sigmoid = lambda x : 1 / (1 + np.exp(-x))
        self.dsigmoid = lambda y : y * (1 - y)

    def feedforward(self , input):
        
        #INPUT TO HIDDEN FUNCTION 
        input_node = Matrix.arrayFrom(input)
        hidden = Matrix.multiply(self.weight_ih , input_node)
        hidden.add(self.bais_h)


        #ACTIVATION FUNTION 
        hidden.map(self.sigmoid)

        #HIDDEN TO OUTPUT FUNCTION
        output = Matrix.multiply(self.weight_ho , hidden)
        output.add(self.bais_o)
        output.map(self.sigmoid)

        return output.toArray()

    def train(self , inputs , targets):
   
        #INPUT TO HIDDEN FUNCTION 
        input_node = Matrix.arrayFrom(inputs)
        hidden = Matrix.multiply(self.weight_ih , input_node)
        hidden.add(self.bais_h)


        #ACTIVATION FUNTION 
        hidden.map(self.sigmoid)

        #HIDDEN TO OUTPUT FUNCTION
        outputs = Matrix.multiply(self.weight_ho , hidden)
        outputs.add(self.bais_o)
        outputs.map(self.sigmoid)
        

        outputs.display()
        target = Matrix.arrayFrom(targets)

        output_errors = Matrix.subract(target , outputs)
        print("1")
        gradient = Matrix.mapOutput(outputs , self.dsigmoid)
        print("2")
        gradient.multiplyScalar(output_errors)
        print("3")
        gradient.multiplyScalar(self.lr)
        print("4")
        hidden_t = Matrix.transpose(hidden)
        print("5")  

        weight_ho_delta = Matrix.multiply(gradient , hidden_t)
        print("6")

        self.weight_ho.add(weight_ho_delta)
        print("7")

        self.bais_o.add(gradient) 
        print("8")

        who_t = Matrix.transpose(self.weight_ho)
        # who_t = self.weight_ho
        print("9")

        print(who_t.row , who_t.col , output_errors.row , output_errors.col)
        print("10")

        hidden_errors = Matrix.multiply(who_t , output_errors)  
        print("11")

        hidden_gradient =  Matrix.mapOutput(hidden , self.dsigmoid)
        print("12")

        hidden_gradient.multiplyScalar(hidden_errors)
        print("13")

        hidden_gradient.multiplyScalar(self.lr)

        print("14")
        input_t = Matrix.transpose(input_node)
        print("15")

        weight_ih_delta = Matrix.multiply(hidden_gradient , input_t)
        print("16")

        self.weight_ih.add(weight_ih_delta)
        print("17")

        self.bais_o.add(hidden_gradient) 
        
        

        # self.bais_h.add(hidden_gradient)
# from NN import NeuralNetwork
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

    nn = NeuralNetwork(2 , 2 , 2)

    for _ in range(1):
        # for i in training:
        i = random.choice(training)
        nn.train(i['input'] , i['targets'])
        # print(nn.feedforward(input))

    print(nn.feedforward([0 , 1]))
    print(nn.feedforward([1 , 0]))
    print(nn.feedforward([0 , 0]))
    print(nn.feedforward([1 , 1]))