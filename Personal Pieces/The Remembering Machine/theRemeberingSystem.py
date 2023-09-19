# The idea is just to have an algorithim which uses a k means alogorithim on a "training set", i.e. putting them in that n dimensional space, and then on the predicting bit it just finds the observation nearest in the k means space.
# And we then search for those observations closest in the k means space and then find the output of those cases were and weight them by distance and if the weighted normalised value is greater than the threshold value than we say 
# that's the likely outcome. So in the case of titanic dataset it doens't need to remember survival column but the dictonary does have to have it as the value to the key (Stored as a string of the coordinates in n-D space) of it's other attricutes.
# I've spotted two problems with this situation, 1) all dimensions are not equal thus if age is largely different it gains a proposterous weight and there may not be enough values to take in the dimensions to create sufficient space for unique observations.
# Think of like a cube in n-dimensions with each length dictated by the range in values so 1,2,or 3 means one side of the cube is 3 long, and so next one 2, next 3, next 3 you'll have 54 unique points and that's all so diversity cannot be expressed.

import pandas as pd
from scipy.spatial import cKDTree

# dict = {"0,1,2,1": "Survived",
#         "0,5,5,2": "Died"}

# print(dict["0,1,2,1"])
    

train = pd.read_csv("Projects/Personal Pieces/The Remembering Machine/train.csv")
test = pd.read_csv("Projects/Personal Pieces/The Remembering Machine/test.csv")

survived = train["Survived"]

train = train.drop(["Name", "Ticket", "Fare", "Cabin", "PassengerId", "Embarked", "Survived"],axis = 1) #We'll see how we do w/o Age, being as that's likely a huge factor in survivorship, if no good we infill. It was in fact no good.

train = train.replace({'female': 1}, regex=True)
train = train.replace({'male': 0}, regex=True)

print(train)
# Create a cKDTree from the DataFrame
kdtree = cKDTree(train.values)

# Query for nearest neighbors
target = [3, 0, 34.5, 0, 0]  # Replace with your target point
nearest_distances, nearest_indices = kdtree.query(target, k=5)  # Find the 5 nearest neighbors

# Get the nearest neighbor rows from the DataFrame
nearest_neighbor_ids = train.index[nearest_indices].to_numpy()

print("Unique IDs of Nearest 5 Neighbors:")

for i in nearest_neighbor_ids:
    print(i)


# nearest_neighbor = train.iloc[nearest_idx]
# print("Nearest Neighbor:", nearest_neighbor)
# for i in train.columns:
#     print(i, sum(train[i].isna())) #Immedeatly I've run into a choice do I leave out all observations where there are nan values in a primarily non nan value column, or do I reduce the feature set s.t all observations have a coordinate point on the n-D map.
#                                    #Also I've realised I could in fill the data, also by k-means possibly as an advanced technique 
#                                    (the obvious benifit being that the infills will not create crazy deviation from where the observation would have been placed anyway in n-D space, especially the more features there are.)