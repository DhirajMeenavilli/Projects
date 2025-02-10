import numpy as np

def classify(text2classify):
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
    
    candidateLabels = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes', 'Other']

    arrs = np.zeros(len(topics)+1)
    
    for j in range(len(topics)):
        for k in range(len(topics[j])):
            if topics[j][k] in text2classify:
                arrs[j] = 1

    if not np.any(arrs):
        arrs[29] = 1
        themes = "Other."

    
    else:
        themes = ""
    
        for i in range(len(candidateLabels)):
            if arrs[i] == 1:
                themes = themes + candidateLabels[i] + ", "
        
        themes = themes[:-2] + "."

    return "The text passed relates to the themes of " + themes