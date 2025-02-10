import pandas as pd
import numpy as np

# A visualization of circles where the largeness is how many times a text was labelled as a given topic, and the brightness was how many counts of an explicit term was used type of thing

df = pd.read_csv("CMPUT 469\Finetune\Sepearating Questions\Q1LabelerLabels.csv", index_col=0)

vals = [str(i).lower() for i in df['a2'][:].values]

CoL = ['expensive', 'expense', 'expenses', 'cost', 'prices', 'price', 'payment', 'payments', 'rent', 'rents', 'spend', 'spending', 'living', 'live', 'high', 'housing']
HousingCost = ['housing', 'rent', 'high', 'mortgage']
Housing = ['rate', 'rent', 'rental', 'struggling', 'comfortable', 'house', 'apartment']
Homelessness = ['homeless', 'crime', 'homelessness', 'downtown', 'people', 'drugs', 'dirty', 'lrt', 'cost', 'help']
Crime = ['crime', 'police', 'poor', 'homelessness', 'people', 'safe', 'high', 'cost', 'living', 'rate', 'downtown']
DaA = ['drugs', 'addiction', 'drug']
JaE = ['job', 'work', 'have', 'employment', 'oppurtunities', 'oppurtunity']
PaGS =['river', 'parks', 'park','nice', 'great', 'valley', 'live', 'green']
Transit = ['lrt', 'train', 'bus', 'transit', 'ride']
Walkability = ['easy', 'access']
Safety = ['safe', 'unsafe', 'crime']
Downtown = ['downtown', 'building']
SocSerandSup = ['social', 'homeless', 'help']
Traffic = ['traffic', 'gridlock', 'streets', 'lights', 'slow', 'rush', 'hour']
PfC = ['kids', 'children', 'activities', 'programs', 'program', 'after']
PfS = ['grandkids', 'property', 'seniors', 'pension', 'elders', 'program', 'programs']
PfD = ['disabilities', 'disability', 'program', 'programs', 'accessibility','ramp','ramps']
Community = ['people','sense','community','family','friends','friend','life','living','comfortable','enjoy','lonely']
Roads = ['roads','pothole','potholes','bike','sidewalk','sidewalks','grass','drive','driving','pot','hole']
Recreation = ['facilities','facility','ymca','rec center', 'rec', 'recreation', 'activity', 'activities']
EventsandAttractions = ['event','events','attraction','attractions','things','beautiful','ugly','boring']
Health = ['health','medical','hospital','facility','facilities', 'free', 'access']
Schools = ['education', 'school', 'system', 'schools']
ChildCare = ['child', 'care', 'wage', 'minimum', 'viable']
CityGovernance = ['city', 'government', 'governance', 'council', 'municipal', 'projects']
Business = ['restaurants', 'shopping', 'store', 'stores', 'oppurtunity', 'oppurtunities', 'grocery', 'nightclubs', 'nightclub', 'scene']
Entertainment = ['amenities', 'amenity', 'entertainment', 'entertain']
Weather = ['weather', 'cold', 'sun', 'sunny', 'ice', 'clouds', 'rain', 'hot']
Taxes = ['tax', 'taxes', 'property']

topics = [CoL, HousingCost, Housing, Homelessness, Crime, DaA, JaE, PaGS, Transit, Walkability, Safety, Downtown, SocSerandSup, Traffic, PfC,
          PfS, PfD, Community, Roads, Recreation, EventsandAttractions, Health, Schools, ChildCare, CityGovernance, Business, Entertainment,
          Weather, Taxes]

arrs = np.zeros((df.shape[0], df.shape[1]-1))

candidateLabels = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes', 'Other']
dfToSave = pd.DataFrame(columns=candidateLabels)

for i in range(len(vals)):
    for j in range(len(topics)):
        for k in range(len(topics[j])):
            if topics[j][k] in vals[i]:
                arrs[i][j] = 1
        
    if not np.any(arrs[i]):
        arrs[i][29] = 1

    dfToSave.loc[len(dfToSave.index)] = arrs[i]
    
dfToSave.to_csv("CMPUT 469\Baseline\SimpleBaseline.csv")