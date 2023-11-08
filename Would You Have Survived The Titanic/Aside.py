import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

Titanic_train = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

X = Titanic_train[['Age','Pclass', 'Fare']]
y = Titanic_train.Survived

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=42)

from xgboost import XGBRegressor

# Define the model
my_model =  XGBRegressor(random_state=0,n_estimators=1000, learning_rate=0.05) 

# Fit the model
my_model.fit(X_train, y_train,early_stopping_rounds=3,eval_set=[(X_valid, y_valid)])

# Get predictions
predictions_2 = my_model.predict(X_valid)

# Calculate Metric
accuracy = accuracy_score(y_valid, predictions_2) # Doesn't work foir some reason, but I'm sure it can be generalised with some googling.

# Uncomment to print MAE
print("Accuracy:" , accuracy)