import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.preprocessing import StandardScaler

# === Set device for GPU or CPU ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# === Load and Preprocess Data ===
features_df = pd.read_csv("/home/ntwist/Documents/Retain/Code + Data 3/Ntwist/Data/Temporary/features_df_no_NA.csv", index_col=0)
features_df = features_df.sort_values("Date")

split_idx = int(len(features_df) * 0.75)
X_train = features_df.iloc[:split_idx].drop(columns=["target"])
X_test = features_df.iloc[split_idx:].drop(columns=["target"])
y_train = features_df.iloc[:split_idx]["target"]
y_test = features_df.iloc[split_idx:]["target"]
X_all, y_all = pd.concat([X_train, X_test]), pd.concat([y_train, y_test])

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_all)

# Convert to torch tensors (on CPU for now; batches will be moved to device)
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
y_tensor = torch.tensor(y_all.values, dtype=torch.float32).view(-1, 1)

# Time-based train/test split
split_idx = int(len(X_tensor) * 0.75)
X_train_nn, X_test_nn = X_tensor[:split_idx], X_tensor[split_idx:]
y_train_nn, y_test_nn = y_tensor[:split_idx], y_tensor[split_idx:]

# Create DataLoaders
train_dataset = TensorDataset(X_train_nn, y_train_nn)
test_dataset = TensorDataset(X_test_nn, y_test_nn)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64)

# Define deep neural network
class DeepRegressor(nn.Module):
    def __init__(self, input_dim):
        super(DeepRegressor, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 4096),
            nn.ReLU(),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Linear(4096, 1)
        )

    def forward(self, x):
        return self.model(x)

# Instantiate model and move to device
input_dim = X_tensor.shape[1]
model = DeepRegressor(input_dim).to(device)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-5)
#weight_decay=5e-2

# Initialize lists to track losses
train_losses = []
test_losses = []

epochs = 10000000
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    for X_batch, y_batch in train_loader:
        X_batch = X_batch.to(device)
        y_batch = y_batch.to(device)
        optimizer.zero_grad()
        predictions = model(X_batch)
        loss = criterion(predictions, y_batch)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    avg_train_loss = running_loss / len(train_loader)
    train_losses.append(avg_train_loss)

    # Evaluate on test set
    model.eval()
    with torch.no_grad():
        X_test_nn_device = X_test_nn.to(device)
        y_test_nn_device = y_test_nn.to(device)
        test_predictions = model(X_test_nn_device)
        test_loss = criterion(test_predictions, y_test_nn_device).item()
        test_losses.append(test_loss)
        r2 = 1 - (test_loss / torch.var(y_test_nn_device))

    print(f"Epoch [{epoch+1}/{epochs}] - Train Loss: {avg_train_loss:.4f} - Test Loss: {test_loss:.4f} - R²: {r2.item():.4f}")

# === Plotting Train vs Test Loss ===
plt.figure(figsize=(10, 6))
plt.plot(range(1, epochs + 1), train_losses, label='Train Loss')
plt.plot(range(1, epochs + 1), test_losses, label='Test Loss')
plt.xlabel('Epoch')
plt.ylabel('MSE Loss')
plt.title('Training vs Test Loss Over Epochs')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

