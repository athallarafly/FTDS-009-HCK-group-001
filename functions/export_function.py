import pandas as pd
from db import engine
from airflow.models import Variable

def data_export():
    file = Variable.get("file_name") # global variable
    data= pd.read_csv('/opt/airflow/data/' + file + '_cleaned.csv', index=False)
    data.to_sql(name= file + '_cleaned', con= engine, index=False)
