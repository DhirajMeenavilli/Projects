import pandas as pd

Titanic_Dataset = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

# 1. How Big is the data?
print(Titanic_Dataset.shape)


# The titanic dataset loaded in is 418 rows x 2 columns. (Would you look at that, writing down the shape let me find out I'd downloaded the wrong dataset, and so I went and got the right datasets and didn't waste a bunch of time waiting to get things done, only for it to ultimately break, because I hadn't seen that my dataset was wrong.)
# This is a perfect example of prevention is worth a tonne of cure, 
# The data is actually 891 rows; also called observations x 12 columns; also called features


#2. How does the data look?
print(Titanic_Dataset.head())

# The first 4 start with indexes 0-4, so it's 0 indexed, Then onto their PassengerId (Capital P) (1-5), Then Survived with values 0 or 1 for dead: 0, alive: 1 or dead: 1, alive : 1 possibly? 
# Pclass is next, defenitley a refrence to Passenger Class it seems to have values 1 and 3 so 2 is also probably in htere, don't know what it goes up to but 3 is probably the stop.
# Then Name, seems to have format Last Name, can't tell, then assumed gender (Mr. or Mrs.) Then the last name I think like (Harris). This might in fact be the key  no ones seen, because this isn't just a bunch of atomised individuals.
    # It's families and stuff, so there might be hidden interactions in a family, a father saving a child, a wife choosing to die with her husband. Those attributes and features could help distinguish correlations we'd never seen or thought about before.
#