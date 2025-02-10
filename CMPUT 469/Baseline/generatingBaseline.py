from transformers import pipeline
import pandas as pd
import numpy as np


classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

candidateLabels = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes', 'Other']
dfToSave = pd.DataFrame(columns=candidateLabels)

df = pd.read_csv('CMPUT 469\Data.csv')

for i in range(800):
    outputArray = np.zeros(len(candidateLabels), dtype=int)

    sequenceToClassify = df.loc[i, 'a2']

    if type(sequenceToClassify) == float:
        outputArray = np.zeros(len(candidateLabels))
    
    else:
        out = classifier(sequenceToClassify, candidateLabels, multi_label=True)

        confident = 0

        while out['scores'][confident] > 0.7:
            confident += 1

        confidentLabels = out['labels'][0:confident]

        for j in range(len(confidentLabels)):
            for k in range(len(candidateLabels)):
                if confidentLabels[j] == candidateLabels[k]:
                    outputArray[k] = 1

    dfToSave.loc[len(dfToSave.index)] = outputArray

    print(i)

dfToSave.to_csv('CMPUT 469\BaselinePredictions.csv')
