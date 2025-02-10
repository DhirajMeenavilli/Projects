import pandas as pd
import numpy as np
from sklearn import metrics

truthdf = pd.read_csv("CMPUT 469\Finetune\Sepearating Questions\Q1LabelerLabels.csv", index_col=0)
preddf = pd.read_csv("CMPUT 469\Baseline\BaselinePredictions.csv", index_col=0)

candidateLabels = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes', 'Other']
truthdf = truthdf[candidateLabels]

randomF1 = 0.0

for i in range(truthdf.shape[0]):

    randomArr = np.random.randint(2, size=len(candidateLabels))
    
    if not np.any(truthdf.iloc[i].to_numpy()):
    
        if not np.any(randomArr):
            randomF1 += 1.0
        
        else:
            randomF1 += 0.0
    
    else:
        randomF1 += metrics.f1_score(truthdf.iloc[i].to_numpy(), preddf.iloc[i].to_numpy(), zero_division=0)

print("The F1 score of the random baseline is:", randomF1/truthdf.shape[0])


modelF1 = 0.0

for i in range(truthdf.shape[0]):
    if not np.any(truthdf.iloc[i].to_numpy()):
        if not np.any(preddf.iloc[i].to_numpy()):
            modelF1 += 1.0
        
        else:
            modelF1 += 0.0
    else:
        modelF1 += metrics.f1_score(truthdf.iloc[i].to_numpy(), preddf.iloc[i].to_numpy(), zero_division=0)

print("The F1 score of the model is:",modelF1/truthdf.shape[0])