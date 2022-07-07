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

        self.bais_h    = Matrix(self.hidden_nodes , 1)
        self.bais_o    = Matrix(self.hidden_nodes , 1)
        
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

    def train(self , input , target):
   
        #INPUT TO HIDDEN FUNCTION 
        input_node = Matrix.arrayFrom(input)
        hidden = Matrix.multiply(self.weight_ih , input_node)
        hidden.add(self.bais_h)


        #ACTIVATION FUNTION 
        hidden.map(self.sigmoid)

        #HIDDEN TO OUTPUT FUNCTION
        outputs = Matrix.multiply(self.weight_ho , hidden)
        outputs.add(self.bais_o)
        outputs.map(self.sigmoid)
        
        target = Matrix.arrayFrom(target)

        output_errors = Matrix.subract(target , outputs)

        # outputs.map(self.dsigmoid)
        gradient = Matrix.mapOutput(outputs , self.dsigmoid)
        gradient.multiplyScalar(output_errors)
        gradient.multiplyScalar(self.lr)

        hidden_t = Matrix.transpose(hidden)
        weight_ho_delta = Matrix.multiply(gradient , hidden_t)

        self.weight_ho.add(weight_ho_delta)

        self.bais_o.add(gradient)

        who_t = Matrix.transpose(self.weight_ho)
        hidden_errors = Matrix.multiply(who_t , output_errors)

        hidden_gradient =  Matrix.mapOutput(hidden , self.dsigmoid)
        hidden_gradient.multiplyScalar(hidden_errors)
        hidden_gradient.multiplyScalar(self.lr)

        input_t = Matrix.transpose(input_node)
        weight_ih_delta = Matrix.multiply(hidden_gradient , input_t)
        
        self.weight_ih.add(weight_ih_delta)
        self.bais_h.add(hidden_gradient)

if __name__ == "__main__":
    input = [1 , 0]
    target = [1 , 0]
    nn = NeuralNetwork(len(input) , 2 , 2)
    nn.train(input , target)
    # print(nn.feedforward(input))
