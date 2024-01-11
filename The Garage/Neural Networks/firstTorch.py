import torch
from torch import nn

in_tensor = torch.tensor([3.0])

print(in_tensor)

model = nn.Sequential(nn.Linear(1,1),
                      nn.ReLU(),
                      nn.Linear(1,5))

output = model(in_tensor)

print(output)