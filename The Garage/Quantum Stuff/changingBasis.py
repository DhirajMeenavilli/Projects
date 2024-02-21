# First have a qubit which is in some binomial distribution between ground and excited, then have the second qubit assume the firsts position, and collapse it under a different measurement basis.

import random
import math

"""
wins = 0.0

# Game

for i in range(1000000):
    x,y = random.randint(0,1),random.randint(0,1) #So Alice and Bob recieve either 0 or 1 as thir input.
    a,b=0,0 # Alica and Bobs bits, without Qubits this is the optimal strategy and after 1,000,000 trials it appears to be roughly coherent with a win rate of 75% 
    if x*y == 1:
        if a != b: # (a+b)%2 Basically just asking a and b not to be equal
            wins += 1.0

    else:
        if a == b:
            wins += 1.0

print(wins/1000000.0)
"""

wins = 0.0

for i in range(1000000):
    x,y = random.randint(0,1),random.randint(0,1) #So Alice and Bob recieve either 0 or 1 as thir input.
    a,b=0,0 # Alica and Bobs bits, without Qubits this is the optimal strategy and after 1,000,000 trials it appears to be roughly coherent with a win rate of 75% 
    if x*y == 1:
        if a != b: # (a+b)%2 Basically just asking a and b not to be equal
            wins += 1.0

    else:
        if a == b:
            wins += 1.0

print(wins/1000000.0)