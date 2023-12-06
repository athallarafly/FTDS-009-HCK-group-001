import streamlit as st
import pandas as pd
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')

#menampilakn Perbandingan Credit Card Defaulter
    st.title('gambar setiap class')
    image = Image.open('gambar1.jpg')
    st.image(image, caption='figure 1')
#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('menampilkan gambar di setiap kategori')
        
#menampilakn Perbandingan Credit Card Defaulter
    st.title('dimenssion of image')
    image = Image.open('gambar2.jpg')
    st.image(image, caption='figure 2')
#menampilkan penjelasan    
    with st.expander('Explanation'):
        st.caption('menampilkan dimensi panjang dan lebar setiap class image yang kita punya')
