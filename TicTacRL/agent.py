import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

# Define the neural network model
class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(3 * 3, 24)
        self.fc2 = nn.Linear(24, 24)
        self.fc3 = nn.Linear(24, 3 * 3)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Function to preprocess the state for the neural network input
def preprocess_state(state):
    return torch.from_numpy(state.flatten()).float().unsqueeze(0)

# Function to choose an action using epsilon-greedy policy
def choose_action(state, epsilon, model):
    if np.random.rand() <= epsilon:
        return random.randrange(3 * 3)
    q_values = model(preprocess_state(state))
    return torch.argmax(q_values).item()