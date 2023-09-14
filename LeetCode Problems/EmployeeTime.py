import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['emp_id', 'event_day'])['total_time'].sum().reset_index()
    employees[['day']] = employees[['event_day']]
    employees = employees.drop(columns=['event_day'])
    employees = employees[['day','emp_id','total_time']]
    
    return employees
