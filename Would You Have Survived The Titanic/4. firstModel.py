# There are always a few steps after having analysed the data, to then try to build your first and ever other model that comes after
import pandas as pd

Titanic_train = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

Titanic_train = Titanic_train.dropna(axis=0)

X = Titanic_train[['PassengerId','Pclass','Age','SibSp','Parch','Fare']] # Goes to show how important data cleaning is and encoding is like we can't include anything that's a string, and I've also chosen to include something like PassengerId which is entirely pointless and any observations derrived are likely due to noise. Not neccessarily the case, but likely.
y = Titanic_train.Survived


#1. Define: What Type of Model Will it Be? 
from sklearn.tree import DecisionTreeClassifier # So in this case we could choose something like a Decision Tree Calssifier

titanic_model = DecisionTreeClassifier(random_state = 2035)

#2. Fit: What are the patterns in the data?
titanic_model.fit(X = X, y = y)

#3. Predict: What does the model think the patterns are?
print('The predictions for the foirst 5 in the training data are:')
print(titanic_model.predict(X.head()))

#4. Evaluate: How well did the model actually do on some given data, just by what we see?
print('The true values were:') # It got 100%, which is srprising, but I guess fair enough. It defenitley would be unlikely to generalise well.
print(y.head())

#5. Validation: Numerically, how did it do?
from sklearn.metrics import accuracy_score

predicted_survival = titanic_model.predict(X)
print(accuracy_score(y,predicted_survival)) # 100% accuracy.



