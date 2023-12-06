import pandas as pd
from joblib import load
import re
import nltk
from nltk.tokenize import word_tokenize
from nlp_id.lemmatizer import Lemmatizer

nltk.download('punkt')

# compiling the regex expression
special_char_removal = re.compile(r"[^a-zA-Z\s\']")

# word mappings
word_variations = {
    'ga': 'tidak', 'gak': 'tidak', 'ngga': 'tidak', 'gk': 'tidak', 'tdk': 'tidak',
    'manstapu': 'mantap', 'mantappp': 'mantap', 'mantabbb': 'mantap', 'mantappss': 'mantap', 
    'mantaaaap': 'mantap', 'mantappppp': 'mantap', 'mantab': 'mantap',
    'bangett': 'banget', 'bangettt': 'banget', 'bgt': 'banget',
    'bagusss': 'bagus', 'baguss': 'bagus', 'bgs': 'bagus',
    'gpp': 'tidak apa-apa', 'hrg': 'harga', 'terimakasih': 'terima kasih'
}

#required libraries for the function
stop_words= load('stopword_list.joblib')
lemmatizer = Lemmatizer()

def text_preprocessing(text):
    text = text.lower()
    text = special_char_removal.sub(" ", text)
    tokens = word_tokenize(text) # tokenization

    tokens = [word_variations.get(word, word) for word in tokens]  # correcting the additional spellings
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Lemmatize to ge the root of the words
    tokens = [word for word in tokens if word not in stop_words]  # removing stop words
    
    processed_text = ' '.join(tokens)

    return processed_text

# preprocessing function python file
def data_preprocess():
    dtype_map={
        'price': 'int64', 
        'overall_rating': 'float64',
        'number_sold': 'int64',
        'total_review':'int64',
        'customer_rating':'int64'
    }
    file = 'm12y2023' # global variable
    data= pd.read_csv('/opt/airflow/data/' + file + '.csv')
    data.drop_duplicates(inplace=True)
    data.columns= data.columns.map(str.lower)
    data.columns= [col.replace(' ', '_') for col in data.columns]
    data.dropna(inplace=True)
    
    #  calling text processing
    data['review_processed'] = data['customer_review'].apply(text_preprocessing)

    data= data.astype(dtype_map)
    data.to_csv('/opt/airflow/data/' + file + '_cleaned.csv', index=False)