from game import play_game
from agent import *

# Initialize the DQN model
model = DQN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.05)

play_game(agent_choice=choose_action())