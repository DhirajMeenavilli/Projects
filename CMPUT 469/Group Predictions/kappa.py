from sklearn.metrics import cohen_kappa_score
import pandas as pd
rater = ['Anu', 'Aqib', 'Ayush', 'Dhiraj', 'Model','Edmonton']
paths = {'Anu': 'CMPUT 469\Group Predictions\Q1LabelsAnu.csv',
         'Aqib':'CMPUT 469\Group Predictions\Q1LabelsAqib.csv',
         'Ayush':'CMPUT 469\Group Predictions\Q1LabelsAyush.csv',
         'Dhiraj':'CMPUT 469\Group Predictions\Q1LabelsDhiraj.csv',
         'Model':'CMPUT 469\Group Predictions\Q1LabelsModel.csv',
         'Edmonton':'CMPUT 469\Group Predictions\Q1Labelz2Compare.csv'}

for i in range(len(paths)-1):
    for j in range(i+1, len(paths)):
        y1 = pd.read_csv(paths[rater[i]])
        y2 = pd.read_csv(paths[rater[j]])

        # Extract the ratings from the DataFrames
        ratings1 = y1.iloc[:, 2:].values
        ratings2 = y2.iloc[:, 2:].values

        # Flatten the ratings arrays
        flat_ratings1 = ratings1.flatten()
        flat_ratings2 = ratings2.flatten()


        print(f'Agreement between {rater[i]} and {rater[j]} was: {cohen_kappa_score(flat_ratings1, flat_ratings2)}')