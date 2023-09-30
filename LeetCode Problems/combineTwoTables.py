import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame, colsToDrop: []) -> pd.DataFrame:
    combined = pd.merge(person, address,on='personId', how='left').drop(colsToDrop,axis=1)
    return combined