import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

Titanic_Dataset = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

# Catergorical Data

# 1. Count Plot # Very useful to show th distribution in the dataset of the representation of a feature in a dataset, so you can modify as needed to be better for training purposes and/or reflect the real world generations of said features or selcect the test set well.
sns.countplot(Titanic_Dataset,x='Survived')
plt.show()

# It's also good for when you have a testset to see that it's not unfavorable or favorable in some way.
"""
Test_data = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Unseen Passangers .csv')

sns.countplot(Test_data,x='Survived')
plt.show() # Normally this would let us ensure that we have the labels well distributed but the Kaggle people didn't give you a way to validate your training which means you get effectively one shot and no feedback which is nonsense, but the point stands and is cool.
"""
# 2. Pie Charting

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
