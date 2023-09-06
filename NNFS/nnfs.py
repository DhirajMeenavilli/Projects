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

inputs = [3, 5, 7] # Each input is a node
firstLayerWeights = [[1,2,1],[1,1,2],[2,1,1], [0.1,0.1,0.1], [1,0.5,2]] # Each node is fully connected

# node1 = neuron()
# node2 = neuron()

firstLayer = []
firstLayerSize = len(firstLayerWeights)

firstLayerOutputs = []
for i in range(firstLayerSize):
    firstLayer.append(neuron())
    firstLayerOutputs.append(firstLayer[i].output(inputs, firstLayerWeights[i]))

# print(firstLayer[0].output(inputs, weights[0]))
# print(firstLayer[1].output(inputs, weights[1]))
secondLayer = []

secondLayerWeights = [[0.1,0.1,0.1,1,0.1], [0.1,0.5,0.5,0.5, 1], [0.15,0.1,0.5,1,0.1], [0.15,0.1,0.1,1,0.15]]
secondLayerSize = len(secondLayerWeights)

secondLayerOutputs = []
for i in range(secondLayerSize):
    secondLayer.append(neuron())
    secondLayerOutputs.append(secondLayer[i].output(firstLayerOutputs, secondLayerWeights[i]))

print(secondLayerOutputs)
