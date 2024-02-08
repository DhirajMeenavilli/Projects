import torch
import torch.nn as nn
from torch import optim
import numpy as np

class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.model = nn.Sequential(nn.Linear(6, 256), #Paddle 1 y position, Paddle 2 y position, ball x position, ball y position, ball x velocity, ball y velocity
                                   nn.ReLU(),
                                   nn.Linear(256, 256),
                                   nn.ReLU(),
                                   nn.Linear(256, 1024),
                                   nn.ReLU(),
                                   nn.Linear(1024, 3)) # Pressing up, down, or none.
        self.optimizer = optim.Adam(self.parameters(), lr=0.01)
        self.loss = nn.MSELoss() # Because a Q-Network is effectively trying to minimize the loss between the predicted Q-values and actual Q-values according to the policy network.

    def forward(self, x): # Backprop is automatically handled by the PyTorch library.
        out = self.model(x)
        return out

class Player():
    def __init__(self, gamma=0.75, epsilon=1, epsilon_min=0.01, epsion_decrement=0.0000025, batch_size=32, max_mem_size=50000000):
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decrement = epsion_decrement
        self.batch_size = batch_size
        self.max_mem_size = max_mem_size
        
        self.action_space = [0,1]
        self.memory_counter = 0

        self.policy_network = DQN()
        # self.target_network = DQN()
        
        self.state_memory = np.zeros((self.max_mem_size, 6), dtype=np.float32)        
        self.new_state_memory = np.zeros((self.max_mem_size, 6), dtype=np.float32)
        self.action_memory = np.zeros(self.max_mem_size, dtype=np.int32)
        self.reward_memory = np.zeros(self.max_mem_size, dtype=np.float32)
    
    def store_transition(self, state, new_state, action, reward):
        index = self.memory_counter % self.max_mem_size
        
        self.state_memory[index] = state
        self.new_state_memory[index] = new_state
        self.reward_memory[index] = reward
        self.action_memory[index] = action

        self.memory_counter += 1

    def choose_action(self, state):
        if np.random.random() > self.epsilon: #np.random.random returns a value between [0.0, 1.0)
            actions = self.policy_network.forward(state)
            greedy_action = torch.argmax(actions).item() # Just because torch.argmax returns the value and index
            return greedy_action
        
        else:
            random_action = np.random.randint(0,3)
            return random_action
    
    def learn(self):
        if self.memory_counter < self.batch_size:
            return

        else:
            self.policy_network.optimizer.zero_grad() # Zeroing out the gradient
            max_mem = min(self.memory_counter, self.max_mem_size) # To make sure we're taking the lesser of how many memories do and can exist

            batch = np.random.choice(max_mem, self.batch_size, replace=False)
            batch_index = np.arange(self.batch_size, dtype=np.int32)

            state_batch = torch.Tensor(self.state_memory[batch])
            new_state_batch = torch.Tensor(self.new_state_memory[batch])
            reward_batch = torch.Tensor(self.reward_memory[batch])
            action_batch = self.action_memory[batch]
            q_of_state = self.policy_network.forward(state_batch)[batch_index, action_batch] # Gives the values only of the actions we actually took
            q_of_next_state = self.policy_network.forward(new_state_batch) # This is where we'd use the target network to get an unmoving Q' for say 100 steps and then we'd copy the weights from the policy network so that it could have updated Q' values
            # q_of_next_state[terminal_batch] = 0.0 # Used to set the q_value of all terminal states to 0

            q_target = reward_batch + self.gamma * torch.max(q_of_next_state, dim=1)[0]

            loss = self.policy_network.loss(q_target, q_of_state)
            loss.backward()
            self.policy_network.optimizer.step()

            if self.epsilon > self.epsilon_min:
                self.epsilon = self.epsilon - self.epsilon_decrement