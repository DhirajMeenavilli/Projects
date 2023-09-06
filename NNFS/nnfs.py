import sys
import numpy as np
import matplotlib

class neuron:
    def __init__(self) -> None:
        self.bias = 0
    
    def compute(self, input, weight):
        y = input * weight + self.bias
        return y

    def output(self, inputs, weights):
        total = 0
        for i in range(len(inputs)):
            total += self.compute(inputs[i],weights[i])
        return total # Strictly linear function can be turned into ReLU later

inputs = [3, 5, 7]
weights = [[1,2,1],[1,1,2]]

# node1 = neuron()
# node2 = neuron()

firstLayer = []
firstLayerSize = 2

for i in range(firstLayerSize):
    firstLayer.append(neuron())
    print(firstLayer[i].output(inputs, weights[i]))

# print(firstLayer[0].output(inputs, weights[0]))
# print(firstLayer[1].output(inputs, weights[1]))