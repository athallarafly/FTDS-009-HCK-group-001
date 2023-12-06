import streamlit as st
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from tensorflow.keras.models import load_model
from nlp_id.lemmatizer import Lemmatizer
from nltk.corpus import stopwords
import re

nltk.download('punkt')
nltk.download('stopwords')

# Define Stopwords
stopwords_id = set(stopwords.words('indonesian'))
sw_1 = set(StopWordRemoverFactory().get_stop_words())
sw_2 = set(stopwords.words('indonesian'))
stopwords_id.update(sw_1)
stopwords_id.update(sw_2)
add_sw = {'tp', 'jg', 'tgl', 'utk', 'nya', 'yg', 'sih', 'aja', 'lg', 'barang', 'tokopedia', 'tokped', 'toped', 'tokopeda',
          'an', 'aaaa', 'hehe', 'laaah', 'yaa', 'krn', 'sy', 'dgn', 'dg', 'sdh', 'jd', 'brg', 'dapet', 'dah', 'sen',
          'gan', 'ny', 'kak', 'dpt', 'deh', 'udh', 'dr', 'dg', 'da', 'uda', 'nih', 'gw', 'gin', 'pdhl', 'duh', 'yah', 'loh',
          'lo', 'jual', 'seller', 'toko', 'sesuai', 'produk', 'pakai', 'pake', 'dtg', 'jgn', 'rb', 'eh',
          'sya', 'tuh', 'klo', 'bs', 'wa', 'gr', 'spt', 'ps', 'lbh', 'pcs', 'pc', 'blm', 'dlm', 'cpt', 'hr', 'eh', 'knp','pd',
          'sm', 'jdi', 'bbrp', 'sma', 'sprti', 'kyk', 'ad'}
remove_sw = {'tidak', 'kurang', 'akurat', 'seenaknya', 'masalahnya', 'segitu', 'sepihak', 'lama', 'pihak', 'alhamdulillah',
             'percuma', 'makasih', 'kelamaan', 'keterlaluan', 'tepat', 'berkali', 'sekali', 'macam', 'kesekian', 'baik',
             'waktu', 'cukup', 'bisa', 'banyak', 'biasa', 'baru', 'jelas', 'sesuai', 'sampai', 'tapi', 'betul', 'datang',
             'masalah', 'banget', 'apa', 'kali', 'kesekian'}
stopwords_id.update(add_sw)
stopwords_id.difference_update(remove_sw)

# Define lemmatizer
lemmatizer = Lemmatizer()


# Definisikan fungsi untuk memproses teks

def text_preprocessing(text, stop_words, lemmatizer):

    # Case folding
    text = text.lower()

    # Menghapus special character
    text = re.sub(r"[^a-zA-Z\s\']", " ", text)

    # Tokenization
    tokens = word_tokenize(text)

    # Mengganti kata 'ga', 'gak', 'ngga', 'gk', dan 'tdk' menjadi 'tidak'
    tokens = [word if word.lower() not in {'ga', 'gak', 'ngga', 'gk', 'tdk'} else 'tidak' for word in tokens]

    # Mengganti variasi dari kata mantap
    tokens = [word if word.lower() not in {'manstapu', 'mantappp', 'mantabbb', 'mantappss', 'mantaaaap', 'mantappppp', 'mantab'} else 'mantap' for word in tokens]

    # Mengganti variasi kata banget
    tokens = [word if word.lower() not in {'bangett', 'bangettt', 'bgt'} else 'banget' for word in tokens]

    # Mengganti variasi kata bagus
    tokens = [word if word.lower() not in {'bagusss', 'baguss', 'bgs'} else 'bagus' for word in tokens]

    tokens = [word if word.lower() not in {'gpp'} else 'tidak apa-apa' for word in tokens]

    tokens = [word if word.lower() not in {'hrg'} else 'harga' for word in tokens]

    tokens = [word if word.lower() not in {'terimakasih'} else 'terima kasih' for word in tokens]

    # Lemmatizer untuk mengembalikan kata menjadi bentuk dasarnya
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Menghapus stopwords
    tokens = [word for word in tokens if word.lower() not in stop_words]

    # Menggabungkan tokens
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
        processed_input = text_preprocessing(user_input, stopwords_id, lemmatizer)

        # Perform inference using the loaded model
        result = model.predict(np.array([processed_input]))  # Assuming the model takes input as a numpy array
        
        # Display prediction
        if result[0] > 0.5:  # Example threshold for binary classification
            st.write('Sentiment: Positive')
        else:
            st.write('Sentiment: Negative')
            
# Run the app
if __name__ == '__main__':
    run()
