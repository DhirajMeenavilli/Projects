"""
Author: Dhiraj Meenavilli
Date: 04/04/2024
Title: Basic Generative Adversarial Network
"""

import pdb
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
from torchvision.utils import make_grid
from tqdm.auto import tqdm
import matplotlib.pyplot as plt

# Visualisation Function
def Show(tensor, ch = 1, size = (28,28), num = 16):
    """
    :function Show: Shows a number of images in a grid fashion of a given size with a given number of color channels
    
    :param tensor: Is the tensor from which we show the images?
    :param ch: Describes the number of channels in the images to be shown
    :param size: Describes the size of the images to be shown in this case 28 pixels length by 28 pixels width
    :param num: Describes the number of images to be shown on output in this case a 4x4 grid resulting in 16 images being displayed
    
    :return: None 
    """
    data = tensor.detatch().cpu().view(-1, ch, *size)
    # Detatches the variable from the computation of the gradients, so that we can just do visulaisation without affecting the computations as we visulaise.
    # We also take the tensor to the CPU as opposed to keeping it on GPU for visulaisation purposes.
    # Finally we return a view of the tensor so as to not disturb the tensor, but of the form (128, 1, 28, 28) from the original form of (128, 784) 
    # which is to just say the tensor is a batch of 128 images of 28x 28 size i.e 784
    
    grid = make_grid(data[:num], nrow=4).permute(1,2,0)
    # So we take the first num of the data tensor, which in this case means the first 16 of the 128 images in the tensor.
    # And then we're going to display it of the form 4 x 4
    # Finally we change the order of channels from 1 x 28 x 28 -> 28 x 28 x 1 so that matplotlib can display it.

    plt.imshow(grid)
    plt.show()

# Main Parameters
epochs = 500
currentStep = 0
alpha = 0.00001
lossFunction = nn.BCEWithLogitsLoss() # More numerically stable ecause it uses the logits and normalises first before calculating BCE Loss.
batchSize = 128

infoStep = 100 # After how may steps we want information about the training etc. to be displayed
meanGeneratorLoss = 0
meanDiscriminatorLoss = 0
noiseVectorDimension = 64
device = 'cpu'

dataLoader = DataLoader(MNIST('./The Gallery', download = True, transform = transforms.ToTensor()), shuffle = True, batch_size = batchSize)
# So we decide where to store the data which in this case is being sent to root
# Then we download the data
# After you download and place it in root you transform the data into a multidimensioanl tensor
# Then we shuffle the data every epoch
# Finally we tell the function how many images to take in in a batch, in this case 128, therefore every epoch will have 60,000/128 iterations = ~469

# Generator Function
def genBlock(input, output):
    """
    :function genBlock: Creates a generator block
    
    :param input: The number of input nodes
    :param output: The number of output nodes

    :return: A block which does a fully connected linear mapping, followed by a batchnorming of the output and activates it with a ReLU
    """
    return nn.Sequential(
        nn.Linear(input, output),
        nn.BatchNorm1d(output),
        nn.ReLU(inplace=True)
    )

class Generator(nn.Module):
    def __init__(self, noiseVectorDimension = 64, imageDimension = 784, outputDimension = 128) -> None:
        super().__init__()
        self.genarator = nn.Sequential(
            genBlock(noiseVectorDimension, outputDimension),
            genBlock(outputDimension, outputDimension*2),
            genBlock(outputDimension*2, outputDimension*4),
            genBlock(outputDimension*4, outputDimension*8),
            nn.Linear(outputDimension*8, imageDimension),
            nn.Sigmoid()
        )
    
    def forward(self, noise):
        return self.genarator(noise) # I'm not sure to what the noise vector we're passing in is getting mapped I suppose it's taken as the litteral input vector
    
def generateNoise(number, noiseVectorDimension):
    return torch.randn(number, noiseVectorDimension).to(device)