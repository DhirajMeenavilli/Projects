# When dealing with a new dataset, or even a dataset you've run some preliminary trials on for finding predictivness etc. you may have 100's or thousands of latent combination features or improperly procesed features of the variable in question.

# A good first step is to begin with a feature utility metric. As the name implies it's a metric which we can use to model how valuable a given feature is in helping us predict. 

# Thus comes about Mututal Information, which purportedly is computationally efficient, theoretically well founded, easy to use, and can detect any kind of relationship not just linear.

# Mututal Information describes relationships in terms of uncertainity. The MI is thus interperted as how much is uncertainity about a a given variable y, reduced by knowing inofrmation about a given varaible, x. 

# It must be noted mutual information can only tell you the relationshp of reducing uncertainity from one feature to another not neccessarily how useful a feature is when interacting with another feature, or if encoded differently (Which can both be good things to focus on for feature engineering.)
# This a low MI score is not the death knell for a feature, but other quality metrics like noisyness, availability, and format for the project also play a role in determmining if it's useful or not.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import mutual_info_regression

def make_mi_scores(X, y):
    X = X.copy()
    for colname in X.select_dtypes(["object", "category"]):
        X[colname], _ = X[colname].factorize()
    # All discrete features should now have integer dtypes
    discrete_features = [pd.api.types.is_integer_dtype(t) for t in X.dtypes]
    mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features, random_state=0)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores


def plot_mi_scores(scores):
    scores = scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title("Mutual Information Scores")

# Set Matplotlib defaults
plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc(
    "axes",
    labelweight="bold",
    labelsize="large",
    titleweight="bold",
    titlesize=14,
    titlepad=10,
)

# Load data

Titanic_train = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')
Titanic_train.dropna(axis=1,inplace=True)

features = ["PassengerId", "Sex", "Fare"]
sns.relplot(
    x="value", y="Survived", col="variable", data=Titanic_train.melt(id_vars="Survived", value_vars=features), facet_kws=dict(sharex=False),
)

plt.show()

X = Titanic_train.copy()
y = X.pop('Survived')

mi_scores = make_mi_scores(X, y) # Running into some issue here not sure how to fix the fact that I'm somehow passing an array with 0 samples.

print(mi_scores.head(10))

plt.figure(dpi=100, figsize=(8, 5))
plot_mi_scores(mi_scores.head(10))

### Extra Thoughts:

# Obviously though Celcius and Farenheight may be both be valuable indicators of how predictive a feature is but they give no new information in the Shannon sense to the model about the prediction.

# Mutual information if it's 1 between 2 features is probably a good indicator that you're not getting any new information to predict with when you do your prediction considering both as opposed to just considering one.