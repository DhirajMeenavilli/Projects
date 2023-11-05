import pandas as pd

Titanic_train = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

features = ['PassengerId','Pclass','Age','SibSp','Parch','Fare','Cabin','Sex']

X = Titanic_train[features]
y = Titanic_train.Survived

# 1. Drop Catergorical Variables: The Issue with this is obvious in that it drops possibly very useful information without good reason

# 2. Ordinal Encoding (Assigning each unique value a unique interger): This can be useful but simmilar catergorical values get transformed to very different values and information is possibly lost, so can be tuned for better encoding. 

# 3. One Hot Encoding: Creating n columns one for each of the n unique values in a catergorical column and binarying each observation to each with either 1 or 0 for ids this unique value or not this unique value/ 