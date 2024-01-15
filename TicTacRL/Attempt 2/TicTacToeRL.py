import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

class Game():
    def __init__(self) -> None:
        self.board = torch.FloatTensor([[0,0,0],[0,0,0],[0,0,0]])
    
    def play_move(self, symbol, position):
        self.board[position//3][position%3] = symbol

# Define the neural network model
class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.model = nn.Sequential(nn.Linear(3, 24),
                                   nn.ReLU(),
                                   nn.Linear(24, 24),
                                   nn.ReLU(),
                                   nn.Linear(24, 9))

    def forward(self, x):
        out = self.model(x)
        return out[0]

torch.manual_seed(0)

game = Game()
X_agent = DQN() # Pure greedy single DQN, no menmory buffer/expierence replay, no policy and target network, and no backprop to update weights
O_agent = DQN()
game.play_move(1,torch.argmax(X_agent(game.board)))
print(game.board)
game.play_move(2,torch.argmax(O_agent(game.board)))
print(game.board)
