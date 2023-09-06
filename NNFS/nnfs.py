import sys
import numpy as np
import matplotlib

class architechture:
    def __init__(self, weights):
        self.weights = weights

    def generate(self):
        #Based on a 3D array of weights it should generate the amount of layers needed as well as the number of nodes in each layer
        layers = len(self.weights)


class neuron:
    def __init__(self, curve):
        self.bias = 0
        self.curve = curve
    
    def compute(self, input, weight):
        y = input * weight + self.bias
        return y

    def output(self, inputs, weights):
        total = 0
        for i in range(len(inputs)):
            total += self.compute(inputs[i],weights[i])
        
        if self.curve == "ReLU": #So that depending on the curve after the output is calculated it is placed on the function appropriately.
            if total < 0:
                total = 0
            
            else:
                pass
        
        elif self.curve == "Sigmoid":
            total = 1/(1+np.exp(total))

        elif self.curve == "Linear":
            pass
        
        else:
            return "Sorry we don't have that curve available currently"
        
        return total # Strictly linear function can be turned into ReLU later

inputs = [3, 5, 7] # Each input is a node
firstLayerWeights = [[1,2,1],[1,1,2],[2,1,1], [0.1,0.1,0.1], [1,0.5,2]] # Each node is fully connected

# node1 = neuron()
# node2 = neuron()

firstLayer = []
firstLayerSize = len(firstLayerWeights)

firstLayerOutputs = []
for i in range(firstLayerSize): # Thus 5 nodes are created
    firstLayer.append(neuron("ReLU"))
    firstLayerOutputs.append(firstLayer[i].output(inputs, firstLayerWeights[i]))

print(firstLayerOutputs)

# print(firstLayer[0].output(inputs, weights[0]))
# print(firstLayer[1].output(inputs, weights[1]))
secondLayer = []

secondLayerWeights = [[0.1,0.1,0.1,1,0.1], [0.1,0.5,0.5,0.5, 1], [0.15,0.1,0.5,1,0.1], [0.15,0.1,0.1,1,0.15]]
secondLayerSize = len(secondLayerWeights)

secondLayerOutputs = []
for i in range(secondLayerSize): #4 nodes
    secondLayer.append(neuron("Sigmoid"))
    secondLayerOutputs.append(secondLayer[i].output(firstLayerOutputs, secondLayerWeights[i]))

print(secondLayerOutputs)

outputLayer = []

outputLayerWeights = [[1,2,0,1]] # 1 output node
outputLayerSize = len(outputLayerWeights)

output = []
for i in range(outputLayerSize):
    outputLayer.append(neuron("Linear"))
    output.append(outputLayer[i].output(secondLayerOutputs, outputLayerWeights[i]))

print(output)

if sum(output) > 100:
    print("Greater than 100!")

else:
    print("Less than a 100 :(.")