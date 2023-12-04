import pandas as pd
from db import engine
from airflow.models import Variable

# loading DAG
# extracting data python file 
def data_load():
    file = Variable.get("file_name") # global variable
    data = pd.read_sql_table(file, engine)
    data.to_csv('/opt/airflow/data/' + file + '.csv', index=False) # saving raw data