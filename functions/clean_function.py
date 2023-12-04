import pandas as pd
from airflow.models import Variable

# preprocessing function python file
def data_preprocess():
    dtype_map={
        'price': 'int64', 
        'overall_rating': 'float64',
        'number_sold': 'int64',
        'total_review':'int64',
        'customer_rating':'int64'
    }
    file = Variable.get("file_name") # global variable
    data= pd.read_csv('/opt/airflow/data/' + file + '.csv')
    data.drop_duplicates(inplace=True)
    data.columns= data.columns.map(str.lower)
    data.columns= [col.replace(' ', '_') for col in data.columns]
    data.dropna(inplace=True)
    
    # add function for tokenization
    
    data= data.astype(dtype_map)
    data.to_csv('/opt/airflow/data/' + file + '_cleaned.csv', index=False)