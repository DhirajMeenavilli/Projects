# Toy Datasets Exist on kaggle, Seaborn, and SKLearn.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

Titanic_Dataset = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

#1. Scatter Plot (Numerical vs. Numerical): Useful for seeing if a relationship exists between 2 different numerical variables, for ex. Tips and Total Bill

sns.scatterplot([Titanic_Dataset['Age'], Titanic_Dataset['Fare']]) # hue = Titanic_Dataset['Sex'], also things like style = , size = , etc. doesn't work with the wide-form data(?), but it can let you see how the relationship works on a catergorical basis for Total Bill and Tip against for ex. Sex, Pclass, Valeted, etc.
plt.show()

#2. Bar Plot(Numerical vs. Catergorical): Not sure what this is exactly useful for but I'm sure it can help answer a question like where exactly are these counts most prounced and thus where are they possibly very revealing / unimportant.

sns.barplot(y=Titanic_Dataset['Age'],x=Titanic_Dataset['Pclass'], hue=Titanic_Dataset['Sex']) # Useful to see the distribution of a numerical variable like Age under various catergorical labels like Passenger Class, and Sex 
plt.show()

#3. Box Plot (Numerical vs. Catergorical) Not sure how exactly I'd go about using this, but this whole section is more of exploring hypotheses you build based on/about encoding, and relationships you believe might be there.

sns.boxplot(x=Titanic_Dataset['Sex'], y=Titanic_Dataset['Age'], hue=Titanic_Dataset['Survived']) # Iluminates if between Men and women there was a large disparity in something like age of survivor/deceased by gender 
plt.show()

#4. Dist Plot (Numerical vs. Catergorical): Very useful to polot conditional distributions, and compare it against other conditional distributions to see how much information you can get out of it. 

sns.distplot(Titanic_Dataset[Titanic_Dataset['Survived']==0]['Age']) # If you type in hist = False you get just the function curve.
sns.distplot(Titanic_Dataset[Titanic_Dataset['Survived']==1]['Age'])
plt.show()

#5. Heat Map (Catergorical vs. Catergorical): Quick and dirty way to get a sense of how the counts are looking against one another, like where is it strongly concentrated, where is it not etc.

sns.heatmap(pd.crosstab(Titanic_Dataset['Pclass'],Titanic_Dataset['Survived'])) # A cross tab is just a set of counts at each meeting point, so in this case 0 against 1, 0 against 2, 0 against 3, and then same 1 against 1 etc. where the first value is survived and the second is Pclass.
plt.show()

#6. Cluster Map (Catergorical vs Catergorical): Looks cool, not sure what it's use is.

sns.clustermap(pd.crosstab(Titanic_Dataset['Pclass'],Titanic_Dataset['Survived']))
plt.show()

#7. Pair Plot: Shows every pairing against one another so it could help with formulation of where encoding may need to change, bar that, possibly where a relationship may just be noise, or where the approach needs to be more precise to get an idea of if the hypothesis is valid or not.

sns.pairplot(Titanic_Dataset, hue = 'Survived')
plt.show()

#8. Line Plot (Numerical vs Numerical): Can help to spot encoding issues or noise in numerical relationships.
sns.lineplot(x = Titanic_Dataset['Age'],y = Titanic_Dataset['Fare'])
plt.show()