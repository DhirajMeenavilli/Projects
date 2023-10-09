# Gonna try and code along and actually do what I can

# First thing that happens is it gets set as a markdown, just my kind of luck, I love it. Here's to a better next.

# import pytorch

# Realised I can do it on jupyter instead which is way better, and also I can then copy the code over if needed.

# Then realised a platform like google colab is even better, also discovered Spyder vaery cool

"""
from sklearn.datasets import make_circles
import pandas as pd
import matplotlib.pyplot as plt
import torch
from sklearn.model_selection import train_test_split
import requests
from pathlib import Path

def accuracy_fn(y_true, y_pred):
    correct = torch.eq(y_true, y_pred).sum().item() # torch.eq() calculates where two tensors are equal
    acc = (correct / len(y_pred)) * 100
    return acc

n_samples = 2000

X, y = make_circles(n_samples, # Toy question from sklearn, of which there are many many more to play with.
                    noise=0.08, # Lots of noise I want to see what happens to the scattering, how does this require a different model? Does it even? Very curious.
                    random_state=2047) #Cool year perhpas 100 years after the great second war. Scary

circles = pd.DataFrame({"X1": X[:, 0], "X2": X[:, 1], "label": y})

plt.scatter(x = X[:, 0], y = X[:, 1], c = y, cmap = plt.cm.RdYlBu) # It really helps me to put code back togetehr after it's seperate nicely, so that I can understand what exactly is going in the call, even though it's maybe harder for others toi read it's very much what I like and what I will probably keep doing.

# Ok this is way cooler, than twoi perfectly concentric obvious data, this will be way more intresting to see if it's actually a red or blue dot, because I can't even tell and it's in high uncertainity for human type situations where a bit of asssitance from AI is what we need, not when it's clear as day, and if you gave us the point graphically we could pin it. What if we could?
# No like what if we could at the time the AI puts something somewhere if there was a visual or grpahically way a human with their insight could place it in maybe a few dimensions or something we could just also place and have a discussion with the AI on what the other might be missing to get an actual output. Like if a realtor can see a hose they can mark it pretty well so what if in highly uncertain moments
# The realtor could say I think it's worth 500 K so heputs it in by tapping on digital board or sliding a scale on a website or somehow just doing what the AI effectiovely does as a secondary model in some sense, and then it can say what you might have missed, or overcompensated for, becuase human biases and heuristics, and you could judge the AI, based on what you know it might likley be suffering from
# And ultimately gain insight and be better off even if the model is not perfect. Maybe?

X = torch.from_numpy(X).type(torch.float)
y = torch.from_numpy(y).type(torch.float)

# Split data into train and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=2035) # make the random split reproducible, and also I set the test_size to 30%, I want to make it a bit harder and see if I can still make it work, take it just the limit where it can no longer by a bit, and figure out what I can improve on the margins, and eep doing it until it's a lost cause. So lets see.

# Make device agnostic code
device = "cuda" if torch.cuda.is_available() else "cpu"
device

class ClusteringModel(torch.nn.Module):
    def __init__(self):
        super().__init__() # Inherit the __init__ method of torch.nn.Module except for what you overwrite, and what's deemed uniheritable or whatever.
        self.layer_1 = torch.nn.Linear(in_features=2, out_features=5) # Ok ok I think I got it, it's basically a instance of a class, i.e. an object. And it takes these as intialisations, which ok makes sense, but what about the method how does it access the transform method, with no .after the instance of the class.
        self.layer_2 = torch.nn.Linear(in_features=5, out_features=1)

    def forward(self, x):
        return self.layer_2(self.layer_1(x)) # This is a compositional function, we have x i.e. feature layer, observation, etc. passed into self.layer_1 so it gets computed in that layer, and then the __call__ method which calls the given models forward() automatically, and is inherited from the nn.Module thing gets auto_called, which leads to the resulting weird looking object method call without a method name.

model_0 = ClusteringModel().to(device) # Just so we don't have to know CPU or GPU or whatever.

loss_fn = torch.nn.BCEWithLogitsLoss() # Should defenitley look into and play with other kinds of loss functions.

optimizer = torch.optim.SGD(params = model_0.parameters(), lr = 0.1) # This is defenitley the one I'm least uncomfortable with but I should still look through the docs, and see what's what.

# This is us actually viewing the first 5 outputs of the X values, that we passed to this thing for training, it's litterally my first ever forward pass.

y_logits = model_0(X_test.to(device))[:5] # Since our model hasn't been trained, these outputs are random.

print(y_logits)

y_pred_probs = torch.sigmoid(y_logits) # This is us really mapping the neural networks forward pass to something we can kind of use / understand in the sense we get to really see on a % basis where is this thing actually predicting this item to be. Like the first level of human interpertibility, before this it's just nonsense. Blackbox huh.

print('\n',y_pred_probs)

y_preds = torch.round(y_pred_probs) # We're rounding our probabilities off to like 0.5 and whatever.

# y_pred_labels = torch.round(torch.sigmoid(model_0(X_test.to(device))[:5])) This is how you can do it in one line if you're so inclined

# Check for equality
# print(torch.eq(y_preds.squeeze(), y_pred_labels.squeeze())) Just a show that squeezing this is the same as squeezing the one line which makes sense because it's the exact same.

y_preds.squeeze()  # This creates a copy if you do use a return, but if not then it just updates basically it mutates the memory which is a bit wild, but it works. In effect though I'm not too sure what it's supposed to do other than it says reduces dimensionality by removing all 1 dimensional things?

torch.manual_seed(3075)

# Set the number of epochs
epochs = 100 # Damn it is actually dead even at a 100 epochs it in fact does worse, this is so wild, it does worse than coin toss, so noise is really going crazy on me.

# Put data to target device
X_train, y_train = X_train.to(device), y_train.to(device)
X_test, y_test = X_test.to(device), y_test.to(device)

# Build training and evaluation loop
for epoch in range(epochs):
    ### Training
    model_0.train() # I was getting confused why the accuracy value isn't changing, it's because it's been already trained, and the weights stay the same as the settled into local otimum.

    # 1. Forward pass (model outputs raw logits)
    y_logits = model_0(X_train).squeeze() # squeeze to remove extra `1` dimensions, this won't work unless model and data are on same device
    # y_pred = torch.round(torch.sigmoid(y_logits)) # turn logits -> pred probs -> pred labls
    probs = torch.sigmoid(y_logits)
    y_pred = torch.round(probs)

    # 2. Calculate loss/accuracy

    loss = loss_fn(y_logits, y_train) # Using nn.BCEWithLogitsLoss works with raw logits

    acc = accuracy_fn(y_train, y_pred)

    # 3. Optimizer zero grad
    optimizer.zero_grad()

    # 4. Backpropogation
    loss.backward()

    # 5. Optimizer step
    optimizer.step()

    ### Testing
    model_0.eval()

    with torch.inference_mode():

        # 1. Forward pass

        test_logits = model_0(X_test).squeeze()
        test_pred = torch.round(torch.sigmoid(test_logits))

        # 2. Caculate loss/accuracy

        test_loss = loss_fn(test_logits, y_test) # More mathematically stable, which we can only know if we read the documentation, crazy

        test_acc = accuracy_fn(y_true=y_test, y_pred=test_pred) # There's a whole metrics library in SKLearn.

    # Print out what's happening every 10 epochs
    if epoch % 10 == 0:
        print(f"Epoch: {epoch} | Loss: {loss:.5f}, Accuracy: {acc:.2f}% | Test loss: {test_loss:.5f}, Test acc: {test_acc:.2f}%") # The model is actually degrasing and doing worse than a fair coin toss, shit is crazy, but that was what Daniel was getting too, this is so wild, and surprising like huhhh. Defenitley thought I was doing something wrong.


# Download helper functions from Learn PyTorch repo (if not already downloaded)
if Path("helper_functions.py").is_file():
  print("helper_functions.py already exists, skipping download")
else:
  print("Downloading helper_functions.py")
  request = requests.get("https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/helper_functions.py")
  with open("helper_functions.py", "wb") as f:
    f.write(request.content)

from helper_functions import plot_predictions, plot_decision_boundary # This is one of the craziest coolest shits

# Plot decision boundaries for training and test sets
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Train")
plot_decision_boundary(model_0, X_train, y_train)
plt.subplot(1, 2, 2)
plt.title("Test")
plot_decision_boundary(model_0, X_test, y_test)

class CircleModelV1(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_1 = torch.nn.Linear(in_features=2, out_features=10) # Changed the amount of out_features
        self.layer_2 = torch.nn.Linear(in_features=10, out_features=10) # extra layer
        self.layer_3 = torch.nn.Linear(in_features=10, out_features=1) # We're also training for longer, in a more real setting we would go about testing things in a pairwise way, and then performing like ANOVA and linear combination pair comparison.

    def forward(self, x): # note: always make sure forward is spelt correctly!
        # Creating a model like this is the same as below, though below
        # generally benefits from speedups where possible.
        # z = self.layer_1(x)
        # z = self.layer_2(z)
        # z = self.layer_3(z)
        # return z
        return self.layer_3(self.layer_2(self.layer_1(x)))

model_1 = CircleModelV1().to(device)

torch.manual_seed(3075)

epochs = 1000 # Train for longer

# Put data to target device
X_train, y_train = X_train.to(device), y_train.to(device)
X_test, y_test = X_test.to(device), y_test.to(device)

for epoch in range(epochs):
    ### Training
    # 1. Forward pass
    y_logits = model_1(X_train).squeeze() # Calling the forward method via the __call__ method.

    # proababilities = torch.sigmoid(y_logits)

    # y_pred = torch.round(proababilities) # logits -> predicition probabilities -> prediction labels
    y_pred = torch.round(torch.sigmoid(y_logits))

    # if epoch % 100 == 0:
    #   print(y_pred)
    #   print(torch.round(torch.sigmoid(y_logits)))
    #   print(y_pred == torch.round(torch.sigmoid(y_logits)))

    # 2. Calculate loss/accuracy (Metric Tracking)
    loss = loss_fn(y_logits, y_train)
    acc = accuracy_fn(y_true = y_train, y_pred = y_pred)

    # 3. Optimizer zero grad
    optimizer.zero_grad() # It just sets the gradient to 0 after every batch/epoch because the gradients are stored in an array and probably updated via += method so setting it to 0 lets us not worry about it adding current gradient to previous gradient making larger and larger gradients and stuff or averaging, if gradient in opposite direction. But torch generally sets it to None, better for memory I guess. But theory is the same.

    # 4. Loss backwards
    loss.backward() # Backprop

    # 5. Optimizer step
    optimizer.step()

    ### Testing
    model_1.eval()

    with torch.inference_mode():

        # 1. Forward pass

        test_logits = model_1(X_test).squeeze()

        test_probabilities = torch.sigmoid(test_logits)

        test_pred = torch.round(test_probabilities)

        # 2. Caculate loss/accuracy

        test_loss = loss_fn(test_logits, y_test)

        test_acc = accuracy_fn(y_true = y_test, y_pred = test_pred)

    # Print out what's happening every 10 epochs
    if epoch % 100 == 0:
        print(f"Epoch: {epoch} | Loss: {loss:.5f}, Accuracy: {acc:.2f}% | Test loss: {test_loss:.5f}, Test acc: {test_acc:.2f}%")

# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.title("Train")
# plot_decision_boundary(model_1, X_train, y_train) # I learned something very valuable which is that you can edit the functions directly in library and then just restart the runtime and your runtime vaiables get cleared, but the function is modified to your fit. Collab is continuing to impress.
# plt.subplot(1, 2, 2)
# plt.title("Test")
# plot_decision_boundary(model_0, X_test, y_test) # Extemely curious for some reason it just won't work on model 1 like it keeps showing just a orange background for the plot, instead of an actual descsion boundry, which is extreemly curious because all valriables are the exact same between model 0 and model 1 except the y_pred feature, but even those when made comprable don't change what's happening.
# Whatever is causing it tho is very likely associated with the fact that there's a string at the top of the plots, stating the code used to produce this. Really weird cus I can see it working for model 0 but not model 1
# But yea defenitley weird, and wonky, but that's kinda the nature of matplotlib
"""