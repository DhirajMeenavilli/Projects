import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales = daily_sales.sort_values('make_name')
    daily_sales = daily_sales.sort_values('date_id')

    dates = daily_sales['date_id'].unique()
    
    uniques = {'unique_leads':[],'unique_partners':[]}
    
    for i in range(len(dates)):
        makes = []
        makes.append(daily_sales.loc[daily_sales['date_id'] == dates[i]]['make_name'].unique())
        
        for j in range(len(makes[0])):
            uniques['unique_leads'].append(int(daily_sales.loc[(daily_sales['date_id'] == dates[i]) & (daily_sales['make_name'] == makes[0][j])]['lead_id'].nunique()))
            uniques['unique_partners'].append(int(daily_sales.loc[(daily_sales['date_id'] == dates[i]) & (daily_sales['make_name'] == makes[0][j])]['partner_id'].nunique()))

    daily_sales.drop(columns=['lead_id','partner_id'],inplace=True)
    daily_sales.drop_duplicates(inplace=True)
    daily_sales['unique_leads'] = uniques['unique_leads']
    daily_sales['unique_partners'] = uniques['unique_partners']
    uniques = pd.DataFrame(uniques)
    return daily_sales