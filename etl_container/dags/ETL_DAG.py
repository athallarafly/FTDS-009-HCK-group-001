# import libraries
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from functions.clean_function import data_preprocess
from functions.load_function import data_load
from functions.export_function import data_export

default_args = {
    'owner': 'dhani',
    'start_date': dt.datetime(2023, 12, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('ETL',
         default_args=default_args,
         schedule_interval='0 0 1 * *', # schedule for the 1st the of the month
         ) as dag:
    
    data_loading = PythonOperator(
        task_id='Fetch-from-SQL-Database',
        python_callable=data_load
    )

    data_processing = PythonOperator(
        task_id='Preprocessing',
        python_callable=data_preprocess
    )

    data_exporting = PythonOperator(
        task_id='Export-to-SQL-Database',
        python_callable=data_export
    )

    # order of execution
    data_loading >> data_processing >> data_exporting
