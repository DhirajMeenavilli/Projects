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
def show(tensor, ch = 1, size = (28,28), num = 16):
    """
    :function show: Shows a number of images in a grid fashion of a given size with a given number of color channels
    
    :param tensor: Is the tensor from which we show the images?
    :param ch: Describes the number of channels in the images to be shown
    :param size: Describes the size of the images to be shown in this case 28 pixels length by 28 pixels width
    :param num: Describes the number of images to be shown on output in this case a 4x4 grid resulting in 16 images being displayed
    
    :return: None 
    """
    data = tensor.detach().cpu().view(-1, ch, *size)
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

infoStep = 23450 # After how may steps we want information about the training etc. to be displayed
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
        """
        :function forward: The auto forward call for the class

        :param noise: The noise vector

        :return: a forward call on the noise vector passed in
        """
        return self.genarator(noise) # I'm not sure to what the noise vector we're passing in is getting mapped I suppose it's taken as the litteral input vector
    
def generateNoise(number, noiseVectorDimension):
    """
    :function generateNoise: Generates a noise vector

    :param number: A random number
    :param noiseVectorDimension: The size of the noise vector

    :return: A random vector of size noiseVectorDimension
    """
    return torch.randn(number, noiseVectorDimension).to(device)

def discBlock(inp, out):
    """
    :function discBlock: Creates a Discriminator Block

    :param inp: The number of nodes for input layer
    :param out: The number of nodes for output layer

    :return: The architecture for a discrimanator block
    """
    return nn.Sequential(
        nn.Linear(inp, out),
        nn.LeakyReLU(0.2) # So that the vanishing gradients problem may be avoided by allowing a smal boundry around 0 in the negative region not to be snapped to 0 but smoothly curved in.
    )

class Discriminator(nn.Module):
    def __init__(self, i_dim = 784, h_dim = 256) -> None:
        super().__init__()
        self.discriminator = nn.Sequential(
            discBlock(i_dim,  h_dim*4), # We start big and get small
            discBlock(h_dim*4, h_dim*2),
            discBlock(h_dim*2, h_dim),
            nn.Linear(h_dim, 1),
            
        )
    
    def forward(self, image):
        """
        :function forward: The auto forward call for the class

        :param image: The vector of the image to be classified

        :return: a forward call on the image to be classified
        """
        return self.discriminator(image)

gen = Generator(noiseVectorDimension).to(device)
genaratorOptimizer = torch.optim.Adam(gen.parameters(), lr=alpha) 
disc = Discriminator().to(device)
discriminatorOptimizer = torch.optim.Adam(disc.parameters(), lr=alpha)

x,y = next(iter(dataLoader)) # Likely replace by a dataset class

# Calculating the Loss

# Generator Loss
def calcGeneratorLoss(lossFunc, gen, disc, number, noiseVectorDimension):
    """
    :function calcGeneratorLoss:
    
    :param lossFunc:
    :param gen:
    :param disc:
    :param number:
    :param noiseVectorDimension:

    :return:
    """
    noise = generateNoise(number, noiseVectorDimension)
    fake = gen(noise)
    pred = disc(fake)
    targets = torch.ones_like(pred) # Means all of the ones the discrimanator said are real
    genLoss = lossFunc(pred, targets)

    return genLoss

def calcDiscLoss(lossFunc, gen, disc, number, realImages, noiseVectorDimension):
    """
    
    """
    noise = generateNoise(number, noiseVectorDimension)
    fake = gen(noise)
    discFake = disc(fake.detach()) # We datch so that we don't accidentally touch the generator
    
    discFakeTargets = torch.zeros_like(discFake)
    discFakeLoss = lossFunc(discFake, discFakeTargets)

    discReal = disc(realImages)
    discRealTargets = torch.ones_like(discReal)
    discRealLoss = lossFunc(discReal, discRealTargets)

    discLoss = (discFakeLoss + discRealLoss) / 2 # Afloat is valid I suppose

    return discLoss

for epcoch in range(epochs):
    for real, _ in tqdm(dataLoader): # For each value returned we store the real values/images and the labels but we discard the labels as they're unneeded for the generator portion of GAN.
        # It should be noted additionally the tqdm gives us an easy way to have progress bars of our training loop.
        
        ### Discriminator
        if currentStep % 8 == 0:
            discriminatorOptimizer.zero_grad()

            currentBatchSize = len(real)
            real = real.view(currentBatchSize, -1)
            real = real.to(device)

            discLoss = calcDiscLoss(lossFunction, gen, disc, currentBatchSize, real, noiseVectorDimension)

            discLoss.backward(retain_graph=False) # Frees the graph in memory
            discriminatorOptimizer.step()

        ### Generator

        genaratorOptimizer.zero_grad()
        generatorLoss = calcGeneratorLoss(lossFunction, gen, disc, currentBatchSize, noiseVectorDimension)
        generatorLoss.backward(retain_graph = False)
        genaratorOptimizer.step()

        ### Visualisation and Steps
        meanDiscriminatorLoss += discLoss.item()/infoStep
        meanGeneratorLoss += generatorLoss.item()/infoStep

        if currentStep % infoStep == 0 and currentStep != 0:
            fakeNosie = generateNoise(currentBatchSize, noiseVectorDimension)
            fake = gen(fakeNosie)
            show(fake)
            show(real)
            print(f"{epcoch}: step {currentStep}, Gen Loss: {meanGeneratorLoss}, Disc Loss: {meanDiscriminatorLoss}")
            meanGeneratorLoss, meanDiscriminatorLoss = 0, 0
        
        currentStep += 1