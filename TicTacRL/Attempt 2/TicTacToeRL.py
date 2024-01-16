import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

class Game():
    def __init__(self) -> None:
        self.board = torch.FloatTensor([0,0,0,0,0,0,0,0,0])
    
    def play_move(self, symbol, position):
        self.board[position] = symbol

# Define the neural network model
class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.model = nn.Sequential(nn.Linear(9, 256),
                                   nn.ReLU(),
                                   nn.Linear(256, 256),
                                   nn.ReLU(),
                                   nn.Linear(256, 9))
        self.optimizer = optim.Adam(self.parameters(), lr=0.01)
        self.loss = nn.MSELoss # Because a Q-Network is effectively trying to minimize the loss between the predicted Q-values and actual Q-values according to the policy network.

    def forward(self, x): # Backprop is automatically handled by the PyTorch library.
        out = self.model(x)
        return out

class Player():
    def __init__(self, gamma=0.99, epsilon=1, epsilon_min=0.01, epsion_decrement=0.0005, batch_size=32, max_mem_size=100000):
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decrement = epsion_decrement
        self.batch_size = batch_size
        self.max_mem_size = max_mem_size
        
        self.action_space = [0,1,2,3,4,5,6,7,8]
        self.memory_counter = 0

        self.policy_network = DQN()
        self.target_network = DQN()
        
        self.state_memory = np.zeros((self.max_mem_size, 9), dtype=np.float32)        
        self.new_state_memory = np.zeros((self.max_mem_size, 9), dtype=np.float32)
        self.action_memory = np.zeros(self.max_mem_size, dtype=np.int32)
        self.reward_memory = np.zeros(self.max_mem_size, dtype=np.float32)
        self.terminal_memory = np.zeros(self.max_mem_size, dtype=np.bool)
    
    def store_transition(self, state, new_state, action, reward, terminal):
        index = self.memory_counter % self.max_mem_size
        self.state_memory[index] = state
        self.new_state_memory[index] = new_state
        self.reward_memory[index] = reward
        self.action_memory[index] = action
        self.terminal_memory[index] = terminal

        self.memory_counter += 1

    def choose_action(self, state):
        if np.random.random() > self.epsilon: #np.random.random returns a value between [0.0, 1.0)
            actions = self.policy_network.forward(state)
            greedy_action = torch.argmax(actions).item() # Just because torch.argmax returns the value and index
            return greedy_action
        
        else:
            random_action = np.random.randint(0,9)
            return random_action

torch.manual_seed(0)

game = Game()
# X_agent = DQN() # Pure greedy single DQN, no menmory buffer/expierence replay, no policy and target network, and no backprop to update weights
# O_agent = DQN()
X_player = Player()