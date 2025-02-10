import pandas as pd

df1 = pd.read_csv("CMPUT 469\Preprocessing\Making Data\Data.csv")

cols1 = ['a2','Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes', 'Other']

df1 = df1[cols1]
df1 = df1.dropna(subset=['a2'])
df1 = df1.reset_index(drop=True)

df1.to_csv('CMPUT 469\Finetune\Sepearating Questions\Q1LabelerLabels.csv')

df2 = pd.read_csv("CMPUT 469\Preprocessing\Making Data\Data.csv")

cols2 = ['b2','Housing', 'Transit', 'Recreation facilities', 'Parks and trails', 'Crime and policing','Roads and sidewalks', 'Social services', 'Information services', 'Waste removal and garbage collection', 'Recycling and eco stations', 'Fire services', 'City communications and customer service', 'Seniors programs','Childrens programs', 'Community programs', 'Bylaw and traffic enforcement', 'Taxes, licensing, and permits', 'Downtown', 'Entertainment, events, and attractions', 'Communications and public engagement', 'City governance']

df2 = df2[cols2]
df2 = df2.dropna(subset=['b2'])
df2 = df2.reset_index(drop=True)

df2.to_csv('CMPUT 469\Finetune\Sepearating Questions\Q2LabelerLabels.csv')

df3 = pd.read_csv("CMPUT 469\Preprocessing\Making Data\Data.csv")

cols3 = ['c1','Cost of living 2', 'Housing cost 2', 'Housing 2', 'Homelessness 2', 'Crime 2', 'Drugs and addiction 2', 'Jobs and employment 2', 'Parks and green spaces 2', 'Transit 2', 'Walkability 2', 'Safety 2', 'Downtown 2', 'Social services and supports 2', 'Traffic 2', 'Programs for children 2', 'Programs for seniors 2', 'Programs for persons with disabilities 2', 'People and sense of community 2', 'Condition of roads and sidewalks 2', 'Recreational facilities and programs 2', 'Events and attractions 2', 'Health care 2', 'Schools and education 2', 'Child care 2', 'City governance 2', 'Local businesses 2', 'Entertainment/amenities 2', 'Weather 2', 'Taxes 2']

df3 = df3[cols3]

for i in range(1,30):
    df3[cols1[i]] = df3[cols3[i]]

cols1.remove('a2')
cols1.remove('Other')
df3 = df3[['c1'] + cols1]

df3 = df3.dropna(subset=['c1'])
df3 = df3.reset_index(drop=True)

df3.to_csv('CMPUT 469\Finetune\Sepearating Questions\Q3LabelerLabels.csv')