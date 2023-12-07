import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Membuat function untuk dipanggil pada app.py
def run():
    st.title('Exploratory Data Analysis')
    with st.expander('Objektif'):
        st.caption('Mengeksplorasi hubungan review/ulasan produk yang ada di platform Tokopedia dengan sentimen dari review tersebut, rating dari produk yang diulas, serta emotional tone dari review tersebut.')

# Jumlah review dari masing-masing sentimen
    st.header('Review Berdasarkan Sentimen')
    sentiment_count = Image.open('sentiment_count.png')
    st.image(sentiment_count, caption='Review Berdasarkan Sentimen')
    with st.expander('Penjelasan'):
        st.caption('Persebaran review yang bersifat positif dan negatif cukup seimbang dengan 48% review positif dan 52% review yang negatif.')
        
# Pembagian emosi review berdasarkan sentimen
    st.header('Emosi Review Berdasarkan Sentimen')
    sentiment_emotion = Image.open('sentiment_emotion.png')
    st.image(sentiment_emotion, caption='Emosi Review Berdasarkan Sentimen')
    with st.expander('Penjelasan'):
        st.caption('Review dengan emosi bahagia (happy) dan suka/cinta (love) juga merupakan review dengan sentimen positif, sementara review dengan emosi marah (anger), ketakutan (fear), dan sedih (sadness) merupakan review dengan sentimen yang negatif.')

# Persebaran rating produk berdasarkan sentimen dari review produk
    st.header('Rating Produk Berdasarkan Sentimen Review')
    rating_sentiment = Image.open('rating_sentiment.png')
    st.image(rating_sentiment, caption='Rating Produk Berdasarkan Sentimen Review')
    with st.expander('Penjelasan'):
        st.caption('Rating dari produk yang memiliki review positif lebih tinggi dibandingkan dengan produk yang memiliki review negatif.')

# Persebaran harga produk berdasarkan sentimen dari review produk
    st.header('Harga Produk Berdasarkan Sentimen Review')
    price_sentiment = Image.open('price_sentiment.png')
    st.image(price_sentiment, caption='Harga Produk Berdasarkan Sentimen Review')
    with st.expander('Penjelasan'):
        st.caption('Harga produk yang memiliki review positif sedikit lebih mahal dibandingkan dengan produk yang memiliki review negatif.')

# Persebaran panjang review produk berdasarkan sentimennya
    st.header('Panjang Review (dalam Jumlah Karakter) Berdasarkan Sentimen')
    len_sentiment = Image.open('len_sentiment.png')
    st.image(len_sentiment, caption='Panjang Review Berdasarkan Sentimen')
    with st.expander('Penjelasan'):
        st.caption('Produk dengan review yang negatif memiliki review yang lebih panjang (menurut jumlah karakter) daripada produk dengan review yang positif.')

# Word cloud dari review positif
    st.header('Kata yang Sering Muncul pada Review Positif')
    positive_wordcloud = Image.open('positive_wordcloud.png')
    st.image(positive_wordcloud, caption='Kata yang Sering Muncul pada Review Positif')
    with st.expander('Penjelasan'):
        st.caption('Pada review positif, pembeli memuji kecepatan pengiriman, keamanan pengemasan barang, kualitas barang yang mantap, original, dan sesuai deskripsi, serta berterima kasih kepada penjual terhadap barang yang dibeli.')

# Word cloud dari review negatif
    st.header('Kata yang Sering Muncul pada Review Negatif')
    negative_wordcloud = Image.open('negative_wordcloud.png')
    st.image(negative_wordcloud, caption='Kata yang Sering Muncul pada Review Negatif')
    with st.expander('Penjelasan'):
        st.caption('Pada review negatif, pembeli menggambarkan kekecewaannya dengan kata-kata kecewa, tidak sesuai, menggambarkan kualitas barang yang rusak, salah, dan jelek, serta komplain mengenai lamanya pengiriman barang yang dibeli.')
