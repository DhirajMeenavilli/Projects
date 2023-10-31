import pandas as pd

Titanic_train = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

Titanic_train = Titanic_train.dropna(axis=0) # Always deal with nan and weird values prior to passing to model

features = ['PassengerId','Pclass','Age','SibSp','Parch','Fare']

X = Titanic_train[features]
y = Titanic_train.Survived

#1. Define the Model (After all the testing and data cleaning etc. we choose our final model we lke)
from sklearn.ensemble import RandomForestClassifier

titanic_model = RandomForestClassifier(random_state = 2035)

#2. Fit on the training data. (All of it, because we don't need a validation set to see how good our model is any more)
titanic_model.fit(X, y)

#3. Predict on the test data
test_data = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Unseen Passangers.csv')
# test_data = test_data.dropna(axis=0) Can't really just drop the na values, but I could just fill them in with like the median value.
test_data = test_data.fillna(method='ffill',axis=0)
test_X = test_data[features]
# test_y = test_data.Survived # This doesn't actually exist in this data but normally we would have our test set to compare against

predictions = titanic_model.predict(test_X)
predictions_df = pd.DataFrame({'Survived': predictions})

submission = test_data.join(predictions_df)

submission = submission[['PassengerId','Survived']]

submission.to_csv('Projects/Would You Have Survived The Titanic/Submission.csv',index=False) # Because predictions is usually np.ndarray not a pandas dataframe so we need to convert it then save it.

# First Entry we got: 50.17% so basically a coin toss, and that's with garbage features, no feature engineering, encoding changes, and with an awful replace of missing values, I'd say that's pretty good for first time with no rails.

#4. Validate by metric (Unfortunately, doesn't exist in this case, but this would be the moment of truth, for this though, we just have to submit to the kaggle site.)
# from sklearn.metrics import accuracy_score

# print(accuracy_score(test_y,predictions)) # With a random Forest there's a 71% accuracy on the validation set. That's drastic imprtovement over a single well tuned TreeClassifier