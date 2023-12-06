import streamlit as st
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from tensorflow.keras.models import load_model
from nlp_id.lemmatizer import Lemmatizer
import re
import json
from joblib import load

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

# Load the sentiment analysis model
model = load_model('model_rnn')

# Streamlit app
def run():
    st.title('NLP Sentiment Analysis')

    # User input text area
    user_input = st.text_area('Enter your text here: after that press Ctrl+Enter', '')

    if st.button('Analyze'):
        # Preprocess user input
        processed_input = text_preprocessing(user_input)

        # Perform inference using the loaded model
        result = model.predict(np.array([processed_input]))  # Assuming the model takes input as a numpy array
        
        # Display prediction
        if result[0] > 0.5:  # Example threshold for binary classification
            st.write('Sentiment: Positive')
        else:
            st.write('Sentiment: Negative')
