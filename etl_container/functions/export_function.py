import pandas as pd
from .db import engine

def data_export():
    file = 'm12y2023'
    data= pd.read_csv('/opt/airflow/data/' + file + '_cleaned.csv')
    data.to_sql(name= file + '_cleaned', con= engine)
