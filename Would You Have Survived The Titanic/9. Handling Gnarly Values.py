# This is the start of the intermediate ML course on Kaggle, so we'll see how it goes.

import pandas as pd

Titanic_train = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

features = ['PassengerId','Pclass','Age','SibSp','Parch','Fare']

X = Titanic_train[features]
y = Titanic_train.Survived

from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X,y, random_state=42)

#1. Drop Rows Containing NaN: The logic being if we just get rid of them we don't have to think about them, this can go for columns as well, but that can lead to situations where we drop like a whole very useful feature because of one recording error. 

cols_with_missing = [col for col in train_X.columns if train_X[col].isnull().any()] # Normally we would use it with the drop but I want to test an alternate method instead.

dropRowTrain = train_X.drop(cols_with_missing, axis=1) # This causes us to drop over 600 rows of the training data just because they are missing the Cabin Fare column value which likley was not that important and even if it was likley didn't justify so many observations being dropped out.
dropRowVal = val_X.drop(cols_with_missing, axis=1) # This also doesn't even work because when you dro the rpws with nulls you can't predict on them so it fails. I didn't even realise when I used ffill I'd have to do something like that for validation as well.

# 2. Imputation: If we just generate the mean or mode value we're most likley to get it right obviously there can be very custom tailored imputation based on the data, so it can get very deep, but in general simple imputation is a good baseline to start with/

from sklearn.impute import SimpleImputer

imputer = SimpleImputer()

imputationTrain = pd.DataFrame(imputer.fit_transform(train_X))
imputationVal = pd.DataFrame(imputer.transform(val_X))

# Imputation removes column names so we have to put them back.

imputationTrain.columns = train_X.columns
imputationVal.columns = val_X.columns

# 3. Extended Imputation: Instead of just passing an imputed value if we pass along with it an indicator variable of if this was reorded or imputed the model may learn some very significant relation to predict with. Not likel but it probably doesn't hurt.

X_train_plus = train_X.copy()
X_valid_plus = val_X.copy()

# Make new columns indicating what will be imputed
for col in cols_with_missing:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_valid_plus[col + '_was_missing'] = X_valid_plus[col].isnull()

# Imputation
my_imputer = SimpleImputer()
imputed_X_train_plus = pd.DataFrame(my_imputer.fit_transform(X_train_plus))
imputed_X_valid_plus = pd.DataFrame(my_imputer.transform(X_valid_plus))

imputed_X_train_plus.columns = X_train_plus.columns
imputed_X_valid_plus.columns = X_valid_plus.columns


# Testing the various styles of imputation

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

titanic_model = RandomForestClassifier(random_state = 2035)
splits = [[dropRowTrain, dropRowVal],[imputationTrain,imputationVal],[imputed_X_train_plus,imputed_X_valid_plus]]

for i in range(len(splits)):
    titanic_model.fit(splits[i][0], train_y)

    predictions = titanic_model.predict(splits[i][1])

    print(accuracy_score(val_y,predictions)) # The second is the best closely tailed by the third which tells us that imputation is defenitley a better method of dealing with missing values than simply dropping columns, and far better than just dropping the row.
    # It should be noted that if there was basically just one column and it was all NaN values dropping that column and imputation will likley perform the same or imputation may even be slightly better.