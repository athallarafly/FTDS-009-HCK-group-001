import pandas as pd
from .db import engine

# loading DAG
def data_load():
    file = 'm12y2023'
    data = pd.read_sql_table(file, engine)
    data.to_csv('/opt/airflow/data/' + file + '.csv', index=False) # saving raw data