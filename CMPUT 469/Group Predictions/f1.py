import pandas as pd
import numpy as np
from sklearn import metrics

truthdf = pd.read_csv("CMPUT 469\Group Predictions\Q1Labelz2Compare.csv", index_col=0)
preddf = pd.read_csv("CMPUT 469\Group Predictions\Q1LabelsModel.csv", index_col=0)

candidateLabels = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes', 'Other']
truthdf = truthdf[candidateLabels]
preddf = preddf[candidateLabels]

modelF1 = 0.0

for i in range(truthdf.shape[0]): # For i in range the number of rows in the truth dataframe
    if not np.any(truthdf.iloc[i].to_numpy()): # This code will execute the block if none of the elements in the ith row of the truth dataframe are true i.e. 1. 
        if not np.any(preddf.iloc[i].to_numpy()): # This code will execute the block if none of the elements in the ith row of the prediction dataframe are true i.e. 1.
            modelF1 += 1.0 # Because they both have none in all areas it's a math hence the f1 should go up by 1 i.e. it's 100% TP
        
        else: # If the truth dataframes row is all 0s and the preds has something which is not 1 then there are 0 true positives hence a 0 for the F1
            modelF1 += 0.0
    else:
        modelF1 += metrics.f1_score(truthdf.iloc[i].to_numpy(), preddf.iloc[i].to_numpy(), zero_division=0) #If there are some things though in the truth dataframe we want to see how well it did. 

print("The F1 score of the model is:",modelF1/truthdf.shape[0])