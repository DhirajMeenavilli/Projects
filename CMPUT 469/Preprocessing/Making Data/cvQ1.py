import pandas as pd

df = pd.read_csv("CMPUT 469\Finetune\Sepearating Questions\Q1LabelerLabels.csv",index_col=0)

fold1 = df[:150]
fold2 = df[150:300]
fold3 = df[300:450]
fold4 = df[450:600]
fold5 = df[600:750]

folds = [fold1, fold2, fold3, fold4, fold5]

candidateLabels = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes', 'Other']

for i in range(len(candidateLabels)):
    for j in range(len(folds)):
        try:
            print("Fold", j , candidateLabels[i],folds[j][candidateLabels[i]].value_counts()[1])
        
        except:
            print("Fold", j , candidateLabels[i],"0")
    