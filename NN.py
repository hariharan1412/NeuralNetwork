from cv2 import Mat
from matirix import Matrix
import numpy as np 


class NeuralNetwork:

    def __init__(self , numI , numH , numO):
        self.input_nodes = numI
        self.hidden_nodes = numH
        self.output_nodes = numO
 
        self.weight_ih = Matrix(self.hidden_nodes , self.input_nodes)
        self.weight_ho = Matrix(self.output_nodes , self.hidden_nodes)

        self.bais_h    = Matrix(self.hidden_nodes , 1)
        self.bais_o    = Matrix(self.hidden_nodes , 1)
        
        self.sigmoid = lambda x : 1 / (1 + np.exp(-x))

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


if __name__ == "__main__":
    input = [1 , 0]
    nn = NeuralNetwork(len(input) , 2 , 2)

    print(nn.feedforward(input))
