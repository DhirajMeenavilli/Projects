# Create an RL system and see if it is able with simple reward to pick up which dice to play against me with.
import random
import numpy as np
import matplotlib.pyplot as plt

dice = [[2,2,4,4,9,9],[1,1,6,6,8,8],[3,3,5,5,7,7]]

class Q_Agent():
    def __init__(self) -> None:
        self.q_table = [[1,1,1],[1,1,1],[1,1,1]]
        self.alpha = 0.01
        self.epsilon = 0.9
        self.epsilon_decrement = 0.001
        self.epsilon_min = 0.1
    
    def choose_action(self, state):
        if random.random() > self.epsilon:

            if self.epsilon > self.epsilon_min:
                self.epsilon -= self.epsilon_decrement
                
            return self.q_table[state].index(max(self.q_table[state]))
        else:

            if self.epsilon > self.epsilon_min:
                self.epsilon -= self.epsilon_decrement

            return self.q_table[0].index(random.choice(self.q_table[0]))
    
    def learn(self, state, action, reward):
        self.q_table[state][action] = (1 - self.alpha) * self.q_table[state][action] + self.alpha * reward

q_learner = Q_Agent()

total_reward = 0

iterations = 10000
rewards = np.zeros(iterations)

for i in range(iterations):
    player_die = random.randint(0,2)
    learner_die = q_learner.choose_action(player_die)

    player_roll = random.choice(dice[player_die])
    learner_roll = random.choice(dice[learner_die])

    if learner_roll > player_roll:
        reward = 1
    
    else:
        reward = -1
    
    total_reward += reward
    rewards[i] = total_reward
    q_learner.learn(player_die, learner_die, reward)

plt.plot(rewards)
plt.ylabel("Reward (Units)")
plt.xlabel("Iterations (Units)")
plt.title("Q Learner Wins over Time")
plt.show()