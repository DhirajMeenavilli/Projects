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
        return total

inputs = [3, 5, 7]
weights = [1,2,1]

node1 = neuron()

print(node1.output(inputs, weights))