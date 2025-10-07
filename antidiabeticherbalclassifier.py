import streamlit as st
from PIL import Image
import numpy as np

# ==============================
# Konfigurasi Halaman
# ==============================
st.set_page_config(
    page_title="Klasifikasi Tanaman Herbal Antidiabetes",
    page_icon="🌿",
    layout="centered"
)

# ==============================
# Tampilan Header
# ==============================
st.markdown("""
    <style>
    body {
        background-color: #f7fdf9;
        color: #003300;
        font-family: 'Poppins', sans-serif;
    }
    .title {
        text-align: center;
        color: #1B5E20;
        font-size: 2.2em;
        font-weight: 700;
        margin-top: 20px;
    }
    .subtitle {
        text-align: center;
        color: #4CAF50;
        font-size: 1.1em;
        margin-bottom: 40px;
    }
    .footer {
        text-align: center;
        color: gray;
        font-size: 0.85em;
        margin-top: 60px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌿 Klasifikasi Tanaman Herbal Antidiabetes</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload citra daun untuk mengidentifikasi jenis tanaman herbal</div>', unsafe_allow_html=True)

# ==============================
# Upload Gambar
# ==============================
uploaded_file = st.file_uploader("Pilih gambar daun herbal...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar yang diunggah', use_column_width=True)

    st.write("🔍 Sedang menganalisis gambar...")

    # TODO: Masukkan model prediksi di sini
    # Contoh dummy prediction
    st.success("🌱 Hasil prediksi: *Daun Kumis Kucing (Orthosiphon aristatus)*")
    st.info("Tanaman ini dikenal berpotensi membantu menurunkan kadar gula darah.")

# ==============================
# Footer
# ==============================
st.markdown("""
    <div class="footer">
        Dibuat oleh <b>Listy Zulmi</b> • Proyek Skripsi Data Science 🌿
    </div>
""", unsafe_allow_html=True)

