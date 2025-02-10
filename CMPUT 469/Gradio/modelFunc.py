from transformers import pipeline
import numpy as np

def modelClassify(sequenceToClassify):
    labels = np.zeros(30)
    classifier = pipeline("zero-shot-classification",
                        model="Narsil/deberta-large-mnli-zero-cls")

    candidateLabels = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime',
                    'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces',
                    'Transit', 'Walkability', 'Safety', 'Downtown',
                    'Social services and supports', 'Traffic', 'Programs for children',
                    'Programs for seniors', 'Programs for persons with disabilities',
                    'People and sense of community', 'Condition of roads and sidewalks',
                    'Recreational facilities and programs', 'Events and attractions',
                    'Health care', 'Schools and education', 'Child care', 'City governance',
                    'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes']

        
    for i in range(len(candidateLabels)):
        hypothesis = f"This text is about {candidateLabels[i]}."
        out = classifier(sequenceToClassify, hypothesis, multi_label=False)

        if out['scores'][0] > 0.75:
            labels[i] = 1

    if not np.any(labels):
        labels[29] = 1
        themes = "Other."

    else:
        themes = ""

        for i in range(len(candidateLabels)):
            if labels[i] == 1:
                themes = themes + candidateLabels[i] + ", "
    
        themes = themes[:-2] + "."

    return "The text passed relates to the themes of " + themes

print(modelClassify("It's a decent place to live with lots of my family and friends. There's lots of fun things to do and I believe it pretty safe city."))