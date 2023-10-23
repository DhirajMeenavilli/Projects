import pandas as pd

Titanic_Dataset = pd.read_csv('Projects/Would You Have Survived The Titanic/Models Training Passengers.csv')

# 1. How Big is the data? (Helpful for us to not write code that breaks)
print(Titanic_Dataset.shape)


# The titanic dataset loaded in is 418 rows x 2 columns. (Would you look at that, writing down the shape let me find out I'd downloaded the wrong dataset, and so I went and got the right datasets and didn't waste a bunch of time waiting to get things done, only for it to ultimately break, because I hadn't seen that my dataset was wrong.)
# This is a perfect example of prevention is worth a tonne of cure, 
# The data is actually 891 rows; also called observations x 12 columns; also called features


#2. How does the data look? (Very good for getting you start to think where is the value, how could we unlock it, where wouldn't we think to look, etc.)
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


#3. Postualte intresting and or potentially useful Hypothesis to invalidate (Just a fun excercise in listing down ideas to go back to if you get stuck.)

# The passenger class is likely out of the bag the most useful corrolary to survival, but very unflexible, so you can't go much deeper with that as your only predictor.

# The gender is likely the second most useful, but also not very flexible or deep in insight, just knowing from historical standards etc. it is going to be useful though.

# The name, ticket, and cabin are the least likely to be useful however they probably have the most hidden insights if any are to be found.



#4, What is the datatype of the columns? (Useful just for whatever functions you end up using so you don't pass any code breaking values to a function. Boring but very important.)

print(Titanic_Dataset.info())

# PassengerId is int64, same with Survived, Pclass, SibSp, and Parch. Name, Sex, Ticket, Cabin and Embarked are objects i.e. strings. Fare and Age are both floats. I'm sure this could be useful, but ehhhh?


#5. Are there / How many Null Values are there in each column? (Very useful to think about what you shouldn't spend much time on, and even what you could possibly drop.)

print(Titanic_Dataset.isnull().sum())

# No missing values excpet age which has about a seventh missing, and cabin which has mostly null. (Defenitley shows we can with the info we had before possibly drop Cabin after exploring it a bit.)

#6. How do the data look mathematically? (Very useful to think about how to encode the data)

print(Titanic_Dataset.describe())

# Doesn't mean much for PassangerId or for Survived, so we can say they're more like ordinal or catergorical, and the encoding likely has little meaning, but maybe if it dictates when a person got on board or something it might help us see correlations?
# Defenitley not helpful with Survived, same with Pclass, cus it's a discrete catergory. For Age we can see that it's min is 0.42000, so we would probably need to make it catergorical with like 8-10 catergories and 1 if yes 0 else.
# The median and mean were about 30, but that's not neccessarily the mode, however with the 25-75% being 20-40 I think it's atleast a safe first hypothesis to assume it's not like a completely bi-modal distribution if if the 25th and 75th percentile give rise to that.
# It also tells us that about 25% of people are below 20 and above 40, so it's kind of split as half 20-40, and half not i.e child,teen / elder. Could be something to think about when encoding the data.
# There was one person with 8 Siblings and Spouses, could be an entry error or it could be something intresting like if you're related to this person you lived, type thing. If this was the case for like 5 of em then we could assume that's just the case and do a check manually.
# Min was 0, and most people had none and like 25% had 1 or more. For parent and child only max 25% had any, with one person having 6, another case of don't need to ask a model we can just check on our own like via names or sumin, see if it was an error or a useful rule.
# Fare is the only one the full description means anything for but also kinda useless because I think it'd be smarter to look at which class is a cut off for what fare encode as such and then just see if there's something to the idea of better suites even in class 2 or 3 and what effect that would have.

#7. Are there Duplicates? (Useful for exploration and for filtering data possibly if needed.)

print(Titanic_Dataset.duplicated().sum())

# No duplicates

#8. What is the correlation looking like between columns? (Defenitley the most sexy question so that we can really feel like data scientists but likely just as helpful as any of the rest.)

print(Titanic_Dataset.corr())

# PassengerID as it is has basically no useful correlations to speak of. 
# Survival as it is has a very high correlation with Pclass and Fare, though more so with Pclass which makes me think it's almost defenitley an encoding thing.
# Pclass had a strong negative correlation with Age and with Fare, most so with Fare, which is logical but I wonder how it would change post encoding switch.
# But this also means age even though it has a strong correlation in some sense with Pclass and Pclass with Survival it's not a very strong indicator by itself of Survival.
# SibSp is strongly correlated with Parch, that could mean maybe it was one family?
