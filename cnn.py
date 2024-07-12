import numpy as np

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.wieghts=np.random.randn(n_inputs, n_neurons)
        self.biases=np.zeroes(1, n_neurons)
      #  np.zeros((5,5))
    def forward(self,inputs):
        self.output=np.dot(inputs,self.wieghts)+self.biases
        #return self.output
        X = [[1, 2, 3, 2.5],
             [2.0, 5.0, -1.0, 2.0],
             [-1.5, 2.7, 3.3, -0.8]]
        layer1=Layer_Dense(4,5)
        layer1.forward(X)
        Layer_Dense(4,5).forward(X)
    