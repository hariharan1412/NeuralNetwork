import random

from cv2 import Mat

class Matrix:

    def __init__(self , rows , cols):
        
        self.row = rows 
        self.col = cols
        self.data = []

        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append(random.uniform(-1 , 1))
            self.data.append(row)
            
    @staticmethod
    def arrayFrom(input):
        new = Matrix(len(input) , 1)
        
        for i in range(len(input)):
            new.data[i][0] = input[i]

        return new

    def toArray(self):
        out_arr = []
        for i in range(self.row):
            for j in range(self.col):
                out_arr.append(self.data[i][j])
        return out_arr

    def display(self):
        
        print()
        for i in range(self.row):
            for j in range(self.col):
                print(self.data[i][j] , end= ' ')
            print()

    def generate_matrix(self):
        
        return self.display(self.data)

    @staticmethod
    def subract(a , b):

        result = Matrix(a.row , a.col)
        
        for i in range(result.row):
            for j in range(result.col):
                result.data[i][j] = a.data[i][j] - b.data[i][j]

        return result

    def add(self , n):

        if isinstance(n , Matrix):
            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j] += n.data[i][j]   

        else:
            
            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j] += n                

        # return self.display(self.data)
    @staticmethod
    def transpose(a):
        
        resultTranspose = Matrix(a.col , a.row)
        for i in range(resultTranspose.col):
            for j in range(resultTranspose.row):
                resultTranspose.data[j][i] = a.data[i][j]

        return resultTranspose

    @staticmethod
    def multiply(a , b):
        if a.col != b.row:
            print("col" , a.col , "row" , b.row)
            print(" DIMENTION ERROR ")
            return None

        else:
            a.result = Matrix(a.row , b.col)
            
            for i in range(a.result.row):
                for j in range(a.result.col):
                    s = 0 
                    for k in range(a.col):
                        s += a.data[i][k] * b.data[k][j]

                    a.result.data[i][j] = s

            return a.result
    
    def multiplyScalar(self , n):
        
        if isinstance(n , Matrix):
            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j] *= n.data[i][j]   

        else:
            
            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j] *= n                
    
    @staticmethod
    def mapOutput(a , func):
        
        result = Matrix(a.row , a.col)
        for i in range(result.row):
            for j in range(result.col):
                val = result.data[i][j] 
                result.data[i][j] = func(val)             
        
        return result

    def map(self , func):

        for i in range(self.row):
            for j in range(self.col):
                val = self.data[i][j] 
                self.data[i][j] = func(val)             

        # return self.display(self.data)
if __name__ == "__main__":
    m = Matrix(2 , 1)
    n = Matrix.transpose(m)
    print(n.display())  