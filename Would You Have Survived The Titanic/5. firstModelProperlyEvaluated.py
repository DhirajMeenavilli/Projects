import pandas as pd

Titanic_train = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

Titanic_train = Titanic_train.dropna(axis=0) # Always deal with nan and weird values prior to passing to model

features = ['PassengerId','Pclass','Age','SibSp','Parch','Fare']

X = Titanic_train[features]
y = Titanic_train.Survived

#1. Split your data
from sklearn.model_selection import train_test_split

train_X, test_X, train_y, test_y = train_test_split(X,y, random_state=42) # THe return is done in the form _X, _X, _y, _y

#2. Define the Model
from sklearn.tree import DecisionTreeClassifier

titanic_model = DecisionTreeClassifier(random_state = 2035)

#3. Fit on the training data
titanic_model.fit(train_X, train_y)

#4. Predict on the test data
predictions = titanic_model.predict(test_X)

#5. Evaluate by eye
print(predictions[:5])
print(test_y.head()) # Have to remember that y is split into train_y, and test_y

#6. Validate by metric
from sklearn.metrics import accuracy_score

print(accuracy_score(test_y,predictions)) # 47% accuracy, which is worse than a coin flip.