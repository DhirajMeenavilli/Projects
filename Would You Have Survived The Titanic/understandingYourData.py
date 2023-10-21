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

# Then comes Sex, which has catergories male, and female, unlikely to have any other groups considering time period. Age is just the age seems to be represented as float and in full years only, not sure though. 

# SibSP seems to be  be intergers of 1 and 0, not sure what it is, Data Dictionary says: # of siblings / spouses aboard the Titanic, so could be pretty much any number >= 0.

# ParCh sems to be just 0's for the first five, but data dictionary says # of parents / children aboard the Titanic, so also any number >= 0.

# Ticket, appears to be some kind of tag, and the dictionary says Ticket Number so maybe we could find if there was super wealthy class, or super poor class from this which could also determine if someone lived or died more accurately.

# Fare, seems to be a float, unbounded range for the number as long as it's > 0, because no one would get on for free I'd assume. 

# Cabin gives the cabin number, which might just be indicitative of the same things as can be gained from ticket names? Although it does have NaN values quite often, so perhaps realtively frequent, 
    # might not be as useful as Ticket but if perhaps there was a reason those values weren't recorded i.e (poverty, sneaking on board, etc.) then we could see if there is some value to extract out of it, but if it's just lost records etc. then it's just noise.

# Embarked seems to have S and C as  choices, not sure what it is, but data dictionary says: Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton.

#3. Postualte intresting and or potentially useful Hypothesis to invalidate

# The passenger class is likely out of the bag the most useful corrolary to survival, but very unflexible, so you can't go much deeper with that as your only predictor.

# The gender is likely the second most useful, but also not very flexible or deep in insight, just knowing from historical standards etc. it is going to be useful though.

# The name, ticket, and cabin are the least likely to be useful however they probably have the most hidden insights if any are to be found.