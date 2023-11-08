"""
Cross-validation gives a more accurate measure of model quality, which is especially important if you are making a lot of modeling decisions. However, it can take longer to run, because it estimates multiple models (one for each fold).

So, given these tradeoffs, when should you use each approach?

For small datasets, where extra computational burden isn't a big deal, you should run cross-validation.
For larger datasets, a single validation set is sufficient. Your code will run faster, and you may have enough data that there's little need to re-use some of it for holdout.
There's no simple threshold for what constitutes a large vs. small dataset. But if your model takes a couple minutes or less to run, it's probably worth switching to cross-validation.

Alternatively, you can run cross-validation and see if the scores for each experiment seem close. If each experiment yields the same results, a single validation set is probably sufficient.
"""

import pandas as pd

Titanic_train = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

cols_to_use = ['Pclass', 'Age', 'Fare']

X = Titanic_train[cols_to_use]
y = Titanic_train.Survived

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline([('imputer', SimpleImputer()),('model', RandomForestClassifier(n_estimators=100,random_state=42))])

from sklearn.model_selection import cross_val_score

score = -1 * cross_val_score(my_pipeline, X, y, cv=3, scoring='neg_mean_absolute_error')

print(score)