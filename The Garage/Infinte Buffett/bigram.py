"""
Author: Dhiraj Meenavilli
Date: 12/02/2023
Title: Bigram Language Model (All credit to Andrej Karpathy, I'm just replicating his work for my own knowledge)
"""
# Imports
import torch
import torch.nn as nn
from torch.nn import functional as F
### --------------------------------------- Functions -----------------------------------------------------------------------------------------
def get_batch(data, batch_size, block_size): # Should always write all your imports and functions at the top of the file not randomly like this.
    # generate a small batch of data of inputs x and targets y
    ix = torch.randint(len(data) - block_size, (batch_size,)) # Not sure why I leave just a comma with nothing after it in place of high
    # Picks the random locations
    x_tuple, y_tuple = [], []

    for i in ix:
      x_tuple.append(data[i:i+block_size])
      y_tuple.append(data[i+1:i+block_size+1])
    
    x_tuple = tuple(x_tuple) # Weird why I couldn't add tensors to a tuple or why the code he was using wouldn't work for me but honestly better that way becasue I get to make it my own in some sense.
    y_tuple = tuple(y_tuple)
    
    x = torch.stack(x_tuple) # Stacks them as rows
    y = torch.stack(y_tuple)

    x,y = x.to(device), y.to(device)

    return x,y
###----------------------------------------- Classes ------------------------------------------------------------------------------------------
class Head(nn.Module):
  # One head of self-attention

  def __init__(self, head_size) -> None:
    super().__init__()
    self.key = nn.Linear(n_embed, head_size, bias = False)
    self.query = nn.Linear(n_embed, head_size, bias = False)
    self.value = nn.Linear(n_embed, head_size, bias = False)
    self.register_buffer('tril', torch.tril(torch.ones(block_size, block_size)))
# The self.register allows you to assign it to the module so it can be called.

  def forward(self, x):
    B,T,C = x.shape[0], x.shape[1], x.shape[2]
    k = self.key(x)
    q = self.query(x)
    weights = q @ k.transpose(-2,-1) * C **(-1/2)
    weights = weights.masked_fill(self.tril[:T,T:] == 0, float('-inf')) # We go and make sure that only the past is able to be communicated with via the weights
    weights = F.softmax(weights, dim=1)
    v = self.value(x)
    output = weights @ v
    return output

class bigramLanguageModel(nn.Module): # For the bigram model position doesn't matter but as we go from bigram to ngram to GPT it will.
  def __init__(self) -> None:
    super().__init__()

    self.token_embedding_table = nn.Embedding(vocab_size, n_embed) # Because you don't want to emebed the entire vocab size I guess?
    # The embedding table is a table of size vocab size x vocab size in this case 65 x 65
    # nn.embedding is a thin wrapper around the table
    self.position_embedding_table = nn.Embedding(block_size, n_embed)
    #Because we're not just emebedding the charachters but also their position we need a second embedding table
    self.self_attention_head = Head(n_embed) # We make the headsize = number of embeddings
    self.lm_head = nn.Linear(n_embed, vocab_size)
  
  def forward(self, idx, targets):
    token_emb = self.token_embedding_table(idx)
    position_emb = self.position_embedding_table(torch.arange(T ,device=device))
    
    x = token_emb + position_emb
    x = self.self_attention_head(x)
    
    logits = self.lm_head(x) # The nn is coming about
    
    # When we pass idx here, every interger is going to refer to the table and pluck out the row associated with it's interger value. So 23 takes the 23rd row, etc.
    # PyTorch will then arrange this into (Batch, Time, Channel) tensors. Channel is = vocab size
    # This will then be interperted as logits which is a set of scores for the charachteres stating what is likely next.

    # loss = F.cross_entropy(logits, targets)
    # This wont work however as F.cross entropy requires a BxT,C tensor so we need to reshape
    if targets == None:
      loss = None

    else:
      B,T,C = logits.shape
      logits = logits.view(B*T, C)
      targets = targets.view(B*T) # Could also do -1, which PyTorch will fill in well.
      loss = F.cross_entropy(logits, targets)

    return logits, loss

    # Now that we can evaluate the loss of the model we'd also like to be able to generate from the model.

  def generate(self, idx, max_new_tokens):
    # idx is (Batch, Time) array of indicies in the current context window
    for i in range(max_new_tokens):
      # We have to make sure the index never goes outside the range of the blaock size available so we crop it (?)
      idx = idx[:, -block_size:]
      # Taking the current indicies and getting the predictions
      logits, loss = self.forward(idx, None) # We ignore the loss, cus we have no ground truth to compare against becasue we are geenrating
      # Focus on last time step, we pluck out the last moment because that's the one predicting what comes next.
      logits = logits[:, -1 , :] # Batch, Time, Channel becomes Batch, Channel
      # Softmax for Probabilities
      probs = F.softmax(logits, dim = -1) # Batch, Channel Format
      # Sample the distribution
      idx_next = torch.multinomial(probs, num_samples=1) #Batch, 1
      # Append sampled index to the running sequence and then return
      idx = torch.cat((idx, idx_next), dim = 1) # Batch, Time + 1
    return idx

###----------------------------------------------------------------- Code --------------------------------------------------------------

# Inputs

with open('The Garage/Infinte Buffett/input.txt','r',encoding='utf-8') as fil:
  text = fil.read()

# Variables

chars = sorted(list(set(text)))
vocab_size = len(chars)
encode_dict = { ch:i for i,ch in enumerate(chars) } # A dictionary of all the charachteres in the vocab so the entire file can be encoded as numbers for the machine to process
decode_dict = { i:ch for i,ch in enumerate(chars) } # A dictionary to decode
encode = lambda s: [encode_dict[c] for c in s] # Takes in a string and outputs a list of ints
decode = lambda l: ''.join(decode_dict[i] for i in l) # Takes a list of ints and returns a concatanted string
data = torch.tensor(encode(text), dtype=torch.long)


training_size = int(0.9*len(data))
block_size = 8 # What the context length we want up to is
batch_size = 32
learning_rate = 1e-3
device = 'cuda' if torch.cuda.is_available() else 'cpu'
n_embed = 32
# eval_iters = 200 If you want an average of losses after a certain number of iterations, useful if different layers have different behaviours dependant on the mode it's in

train_data = data[:training_size]
val_data = data[training_size:]

m = bigramLanguageModel()
model = m.to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate) # For smaller models a bigger learning rate is fine because of less complexity in some sense.
torch.manual_seed(42)

# Outputs
# torch.no_grad() Useful for validation time.
for i in range(10000):
  # Sample the data
  xb, yb = get_batch(train_data, batch_size, block_size)

  # Evaluate the loss
  logits, loss = model(xb, yb)
  optimizer.zero_grad(set_to_none=True) # Zeroing out gradients of previous steps to avoid contiminating the gradient.
  loss.backward()
  optimizer.step()

print(loss.item()) # 2.5 is about as low as it's gonna go and it gets there in about 20000 iterations

print(decode(model.generate(idx=torch.zeros((1,1), dtype=torch.long, device=device),max_new_tokens=100)[0].tolist())) # it actually looks kind of like an english sentence now with spacing and even some real words and caps in reasonable places