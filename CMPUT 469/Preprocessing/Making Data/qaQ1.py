import pandas as pd

df = pd.read_csv('CMPUT 469\Preprocessing\Making Data\Data.csv',index_col=0)['a2']

topics = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes']

questions = []

for i in range(df.shape[0]):
    for topic in topics:
        questions.append(f"Is the text: '{df.iloc[i]}'about the topic of {topic}? Please answer only Yes or No.")

df2Save = pd.DataFrame({"Questions": questions})

df2Save.to_csv('CMPUT 469\QA\qaQ1.csv',index = False)

