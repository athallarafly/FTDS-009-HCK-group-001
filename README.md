# Analisis Sentimen dari Review Produk di Tokopedia 📊

[Hugging Face Deployment](https://huggingface.co/spaces/habibib/FTDS-009-HCK-group-001)

## Latar Belakang Proyek 🌟

Pengalaman pelanggan dapat diukur dan dipahami melalui berbagai cara, salah satunya melalui review yang diberikan oleh pelanggan (Jain et. al., 2017). Review yang ditinggalkan pelanggan dapat mempengaruhi keputusan pelanggan lain, sehingga review ini perlu diperhatikan (Patil & Rane, 2023). Salah satu cara efektif untuk menganalisis review ini adalah melalui analisis sentimen, yang dapat memberikan wawasan tentang aspek-aspek yang perlu ditingkatkan, baik dari segi produk maupun layanan. Analisis ini bertujuan untuk meningkatkan pengalaman pelanggan, yang pada gilirannya akan meningkatkan kepuasan pelanggan dan reputasi brand (Debutify, 2023).

## ETL 🔄

### Alat: Docker, Airflow, Great Expectations
### Objektif:
Data perlu diproses dan dibersihkan untuk digunakan oleh pihak lain seperti analis data atau ilmuwan data. ETL (Extract, Transform, Load) membantu menyediakan data yang bersih secara efisien. Otomatisasi akan dilakukan setiap bulan, memberikan data yang bersih kepada analis/ilmuwan data untuk dikerjakan.

### Kesimpulan:
Nama kolom data mentah perlu dinormalisasi meskipun tidak ada nilai yang hilang. Fungsi yang dibuat untuk transformasi terdiri dari normalisasi nama kolom, menghapus duplikat dan nilai yang hilang jika ada di masa depan, tokenisasi, dan memastikan kolom numerik memiliki tipe data yang benar. Mengimpor dan mengekspor data menggunakan sqlalchemy untuk menghubungkan sql dalam kontainer. Saran untuk masa depan adalah memiliki otomatisasi untuk penamaan file.

## EDA (Exploratory Data Analysis) 🔍

### Alat: NLTK, Matplotlib, Seaborn, nlp-id, TableU
### Objektif:
EDA akan mengeksplorasi hubungan antara review/ulasan produk di Tokopedia dengan sentimen dari review tersebut, rating dari produk, serta emotional tone dari review. EDA ini tidak hanya memberikan wawasan bagi penjual, jasa ekspedisi, dan Tokopedia sebagai pemilik platform untuk meningkatkan pengalaman berbelanja pembeli, tetapi juga dapat menjadi dasar pembuatan model NLP yang dapat memprediksi sentimen dari review produk di Tokopedia.

### Kesimpulan:
Review yang mengekspresikan emosi bahagia dan cinta cenderung memiliki sentimen positif, sementara review dengan emosi ketakutan, sedih, dan marah cenderung negatif. Produk dengan review positif umumnya memiliki rating lebih tinggi dan sedikit lebih mahal dibandingkan produk dengan review negatif. Review negatif dan produk dengan rating rendah cenderung memiliki review yang lebih panjang. Kata-kata yang sering muncul pada review positif adalah "mantap", "cepat", "sesuai", dan "terima kasih", sedangkan pada review negatif adalah "tidak sesuai", "kurang", "kecewa", "jelek", dan "rusak".

## Machine Learning 🤖

### Alat: Tensorflow, Scikit-learn, Sastrawi
### Objektif:
Tujuan utamanya adalah membangun sebuah model NLP untuk mengkategorikan ulasan produk ke dalam sentimen positif atau negatif. Model ini akan dievaluasi menggunakan metrik akurasi sebagai tolok ukur utama.

### Kesimpulan:
Model RNN berhasil mencapai tingkat akurasi sebesar 88% dalam mengklasifikasikan sentimen ulasan produk, sesuai dengan tujuan penggunaan metrik akurasi sebagai tolok ukur performa model. Keberhasilan ini menunjukkan efektivitas pendekatan yang diambil dalam membangun model RNN untuk mengklasifikasikan sentimen ulasan produk secara akurat.

---
### Dataset

[PRDECT-ID: Indonesian Emotion Classification](https://www.kaggle.com/datasets/jocelyndumlao/prdect-id-indonesian-emotion-classification)
