import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

Titanic_Dataset = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

# Catergorical Data

# 1. Count Plot:  Very useful to show the distribution in the dataset of the representation of a feature in a dataset, so you can modify as needed to be better for training purposes and/or reflect the real world generations of said features or selcect the test set well.
sns.countplot(Titanic_Dataset,x='Survived')
plt.show()

# It's also good for when you have a testset to see that it's not unfavorable or favorable in some way.
"""
Test_data = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Unseen Passangers .csv')

sns.countplot(Test_data,x='Survived')
plt.show() # Normally this would let us ensure that we have the labels well distributed but the Kaggle people didn't give you a way to validate your training which means you get effectively one shot and no feedback which is nonsense, but the point stands and is cool.
"""
# 2. Pie Charting: Very useful to get a percentage idea, simmilar to the count plot, but can serve to put things in an easily understandable perspective of percents vs. absolute counts, though one should suffice most of the time.

Titanic_Dataset['Sex'].value_counts().plot(kind='pie',autopct='%.2f')
plt.show()

""" A prettier way of doing it
#colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
#explsion
explode = (0.05,0.05,0.05)

plt.pie(Titanic_Dataset['Pclass'], colors = colors)
#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
plt.tight_layout()
plt.show()
"""

# Numerical Data

#1. Histogram: Really helpful to decide how to bin data, for embedding purposes, or even just what amount of coarsness we can reasonably use.

plt.hist(Titanic_Dataset['Age'], bins = 10)
plt.show()

plt.hist(Titanic_Dataset['Age'], bins = 100)
plt.show()


#2. Dist Plot: Very useful to see what functions you could possibly use toi do things like simmulate synthetic data, and just to tell you waht the proabablities actually look like. And to note the skew of a distribution.

sns.distplot(Titanic_Dataset['Age']) # the distribution has to be generally drawn on by you.
plt.show()

#3. Boxplot: Very useful for both outlier detection and neccessarily for how much information of the Shannon variety / signal a given feature value might represent.
sns.boxplot(Titanic_Dataset['Fare']) #
plt.show()

"""
Xy = X.copy() # This is a code to visualise a kmeans clusterings against some target value to see if there's any clear cluster:target signal.
Xy["Cluster"] = Xy.Cluster.astype("category")
Xy["SalePrice"] = y
sns.relplot(
    x="value", y="SalePrice", hue="Cluster", col="variable",
    height=4, aspect=1, facet_kws={'sharex': False}, col_wrap=3,
    data=Xy.melt(
        value_vars=features, id_vars=["SalePrice", "Cluster"],
    ),
);

# Additionally it should be noted that things like SHAP values and Partial Dependance Plots are also extremely useful for determining the values of features and for granting better insights into disvalidating hypothesis.

"""