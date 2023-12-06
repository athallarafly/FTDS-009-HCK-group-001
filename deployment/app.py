import streamlit as st
import eda
import model

# navigating pages
page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Classification Model'])

if page == 'Home Page':
    st.header('Home Page') 
    st.write('')
    st.write(
        """
        **Member Tim**:
        
        - Qothrunnadaa Alyaa ( **Data Analyst** )

        - Athalla Rafly Mahardhika Noegroho ( **Data Scientist** )

        - Habibi Bagus Suliano ( **Data Scientist** )

        - Achmad Dhani ( **Data Engineer** )
        """
        )
    st.markdown('Dataset: [PRDECT-ID: Indonesian Emotion Classification](https://www.kaggle.com/datasets/jocelyndumlao/prdect-id-indonesian-emotion-classification)')
    st.write('Objektif :')
    st.write('Tujuan utamanya adalah membangun sebuah model menggunakan pendekatan NLP untuk mengkategorikan ulasan produk ke dalam sentimen positif atau negatif. Model ini akan dievaluasi menggunakan metrik akurasi sebagai tolok ukur utama untuk menilai seberapa tepatnya model dalam memprediksi sentimen dari ulasan produk. Tingkat akurasi yang tinggi akan menjadi indikator keberhasilan, menunjukkan kemampuan model dalam mengklasifikasikan sentimen dengan akurat.')
    st.caption('Please pick the options in the Select Page Box located on the left of the screen to start!')
    st.write('')
    st.write('')
    
#============================= Background Info ==========================
    
    with st.expander("Background Information"):
        st.caption(
            '''
            Pemahaman yang komprehensif terkait tanggapan serta pandangan pelanggan terhadap 
            produk atau layanan memiliki peran penting dalam membangun model NLP (Natural Language Processing) 
            untuk analisis sentimen. Model ini tidak hanya memberikan wawasan mendalam tentang evaluasi pengguna 
            terhadap produk, tetapi juga memungkinkan pemilik produk atau penyedia layanan untuk merespons dengan 
            lebih efektif terhadap kebutuhan serta preferensi konsumen. Oleh karena itu, pengembangan model NLP yang 
            handal menjadi krusial dalam menghadirkan solusi yang responsif dan relevan terhadap umpan balik pelanggan.
            '''
        )
#============================= Work Flow ================================
    
    with st.expander("Work Flow"):
        st.caption(
            '''
            Proses pengembangan model NLP untuk analisis sentimen ulasan pelanggan dimulai dengan mengunduh 
            dataset dari Kaggle, dilanjutkan dengan tahapan EDA untuk mengeksplorasi distribusi sentimen dan 
            statistik deskriptif. Langkah selanjutnya melibatkan pra-pemrosesan data, termasuk pembersihan data, 
            penghapusan stopword, dan penerapan lemmatization. Setelahnya, dataset dibagi menjadi dua bagian: 
            training set dan test set. Kemudian, model NLP, seperti LSTM, RNN, dan GRU, dibangun untuk melakukan 
            analisis sentimen. Evaluasi model dilakukan menggunakan metrik akurasi untuk menilai seberapa tepat 
            model dalam memprediksi sentimen. Model terbaik disimpan untuk penggunaan mendatang, sementara langkah 
            terakhir melibatkan deployment model ke platform Huggingface atau platform lainnya untuk pemanfaatan secara luas.
            '''
        )
        
#============================= Conclusion =================================
    with st.expander("Conclusion"): # conclusion
        st.caption(
            '''
            Dari tujuan awal mengembangkan model NLP untuk mengklasifikasikan sentimen ulasan produk, 
            model RNN muncul sebagai pemenang dengan tingkat akurasi sebesar 88%. Keberhasilan ini sesuai dengan tujuan 
            penggunaan metrik akurasi sebagai tolok ukur utama dalam mengevaluasi performa model. Ini menegaskan bahwa 
            pendekatan yang diambil dalam membangun model RNN memberikan hasil yang sangat baik dalam mengklasifikasikan 
            sentimen ulasan produk secara akurat. Hasil ini memberikan dasar yang kuat untuk memahami pandangan dan perasaan 
            engguna terhadap produk dengan tingkat keakuratan yang tinggi.
            '''
        )

#============================ Other Page ======================================
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model.run()
