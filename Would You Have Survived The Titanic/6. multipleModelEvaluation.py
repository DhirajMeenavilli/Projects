import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Titanic_train = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

Titanic_train = Titanic_train.dropna(axis=0) # Always deal with nan and weird values prior to passing to model

features = ['PassengerId','Pclass','Age','SibSp','Parch','Fare']

X = Titanic_train[features]
y = Titanic_train.Survived

max_leaf_nodes = [5,50,500,5000]

for i in range(len(max_leaf_nodes)):
    #1. Split your data

    train_X, test_X, train_y, test_y = train_test_split(X,y, random_state=42)

    #2. Define the Model

    titanic_model = DecisionTreeClassifier(max_leaf_nodes=max_leaf_nodes[i],random_state = 2035)

    #3. Fit on the training data
    titanic_model.fit(train_X, train_y)

    #4. Predict on the test data
    predictions = titanic_model.predict(test_X)

    #5. Evaluate by eye
    print(predictions[:5]) # It seems to be the case that at 50 nodes and beyond the exact same predictions are occuring.
    print(test_y.head()) 

    #6. Validate by metric
    print("Max Level:",max_leaf_nodes[i]," Accuracy:",accuracy_score(test_y,predictions)) # 47% accuracy now moved up to 60% just as a function of having a bit deeper of a tree.

titanic_model = DecisionTreeClassifier(max_leaf_nodes = 50,random_state = 2035)

titanic_model.fit(X,y) # Because we've found the best depth level, we don't really need a hold out set so we can just train on the full dataset.