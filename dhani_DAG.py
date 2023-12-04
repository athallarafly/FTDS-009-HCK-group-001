# import libraries
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from functions.clean_function import cleaning_data
from functions.load_function import loading_data
from functions.export_function import export_data
from airflow.models import Variable

# settting a global variable
Variable.set('file_name', "m12y2023")

default_args = {
    'owner': 'dhani',
    'start_date': dt.datetime(2023, 12, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}

with DAG('ETL',
         default_args=default_args,
         schedule_interval='0 0 1 * *', # schedule for the 1st the of the month
         ) as dag:
    
    data_load = PythonOperator(
        task_id='Fetch from SQL Database',
        python_callable=loading_data
    )

    data_clean = PythonOperator(
        task_id='Preprocessing',
        python_callable=cleaning_data
    )

    data_export = PythonOperator(
        task_id='Export to SQL Database',
        python_callable=export_data
    )

    # order of execution
    data_load >> data_clean >> data_export
