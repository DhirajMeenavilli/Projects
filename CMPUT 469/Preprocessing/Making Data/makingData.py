import pandas as pd

data = pd.read_csv('CMPUT 469\Preprocessing\Intial\Service Satisfaction Survey 2023 coded data - Online Panel Sample (800) - Data.csv')

data = data.drop(['id','weight','a1','b1',], axis=1)

titlesForQ1 = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes', 'Other']

for i in range(1,31):
    data[titlesForQ1[i-1]] = data['a2_coded_'+str(i*2-1)] | data['a2_coded_'+str(i*2)]

titlesForQ2Part1 = ['Housing', 'Transit', 'Recreation facilities', 'Parks and trails']

for i in range(1,5):
    data[titlesForQ2Part1[i-1]] = data['b2_coded_'+str(i*8-7)] | data['b2_coded_'+str(i*8-6)] | data['b2_coded_'+str(i*8-5)] | data['b2_coded_'+str(i*8-4)] | data['b2_coded_'+str(i*8-3)] | data['b2_coded_'+str(i*8-2)] | data['b2_coded_'+str(i*8-1)] | data['b2_coded_'+str(i*8)]


titlesForQ2Part2 = ['Crime and policing','Roads and sidewalks']

for i in range(1,3):
    data[titlesForQ2Part2[i-1]] = data['b2_coded_'+str(32 + i*5-4)] | data['b2_coded_'+str(32 + i*5-3)] |  data['b2_coded_'+str(32 + i*5-2)] | data['b2_coded_'+str(32 + i*5-1)] | data['b2_coded_'+str(32 + i*5)]

data['Social services'] = data['b2_coded_43'] | data['b2_coded_44'] | data['b2_coded_45'] | data['b2_coded_46'] | data['b2_coded_47'] | data['b2_coded_48'] | data['b2_coded_49'] | data['b2_coded_50']

data['Information services'] = data['b2_coded_51'] | data['b2_coded_52'] | data['b2_coded_53'] | data['b2_coded_54'] | data['b2_coded_55']

data['Waste removal and garbage collection'] = data['b2_coded_56'] | data['b2_coded_57'] | data['b2_coded_58'] | data['b2_coded_59'] | data['b2_coded_60'] | data['b2_coded_61']

data['Recycling and eco stations'] =  data['b2_coded_62'] | data['b2_coded_63'] | data['b2_coded_64'] | data['b2_coded_65'] | data['b2_coded_66'] | data['b2_coded_67'] | data['b2_coded_68']

data['Fire services'] = data['b2_coded_69'] | data['b2_coded_70'] | data['b2_coded_71'] | data['b2_coded_72'] | data['b2_coded_73'] | data['b2_coded_74']

data['City communications and customer service'] = data['b2_coded_75'] | data['b2_coded_76'] | data['b2_coded_77'] | data['b2_coded_78'] | data['b2_coded_79']

titlesForQ2Part3 = ['Seniors programs','Childrens programs', 'Community programs']

for i in range(1,4):
    data[titlesForQ2Part3[i-1]] = data['b2_coded_'+str(79 + i*7-6)] | data['b2_coded_'+str(79 + i*7-5)] |  data['b2_coded_'+str(79 + i*7-4)] | data['b2_coded_'+str(79 + i*7-3)] | data['b2_coded_'+str(79 + i*7-2)] | data['b2_coded_'+str(79 + i*7-1)] | data['b2_coded_'+str(79 + i*7)]

data['Bylaw and traffic enforcement'] = data['b2_coded_101'] | data['b2_coded_102'] | data['b2_coded_103'] | data['b2_coded_104'] | data['b2_coded_105'] | data['b2_coded_106']

data['Taxes, licensing, and permits'] = data['b2_coded_107'] | data['b2_coded_108'] | data['b2_coded_109'] | data['b2_coded_110'] | data['b2_coded_111'] | data['b2_coded_112']

data['Downtown'] = data['b2_coded_113'] | data['b2_coded_114'] | data['b2_coded_115'] | data['b2_coded_116'] | data['b2_coded_117'] 

data['Entertainment, events, and attractions'] = data['b2_coded_118'] | data['b2_coded_119'] | data['b2_coded_120'] | data['b2_coded_121'] | data['b2_coded_122'] | data['b2_coded_123'] | data['b2_coded_124'] | data['b2_coded_125']

data['Communications and public engagement'] = data['b2_coded_126'] | data['b2_coded_127'] | data['b2_coded_128'] | data['b2_coded_129']

data['City governance'] = data['b2_coded_130']

titlesForQ3 = ['Cost of living', 'Housing cost', 'Housing', 'Homelessness', 'Crime', 'Drugs and addiction', 'Jobs and employment', 'Parks and green spaces', 'Transit', 'Walkability', 'Safety', 'Downtown', 'Social services and supports', 'Traffic', 'Programs for children', 'Programs for seniors', 'Programs for persons with disabilities', 'People and sense of community', 'Condition of roads and sidewalks', 'Recreational facilities and programs', 'Events and attractions', 'Health care', 'Schools and education', 'Child care', 'City governance', 'Local businesses', 'Entertainment/amenities', 'Weather', 'Taxes']

for i in range(1,30):
    data[titlesForQ3[i-1]+" 2"] = data['c1_coded_'+str(i*2-1)] | data['c1_coded_'+str(i*2)]

data.to_csv('CMPUT 469\Preprocessing\Making Data\Data.csv')