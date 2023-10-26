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

#4. Dist Plot (Numerical vs. Catergorical):

#5. Heat Map (Catergorical vs. Catergorical):

#6. Cluster Map (Catergorical vs Catergorical):