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
    #MainMenu, footer, header {visibility: hidden;}
    body {
        background-color: #f8fcf8;
        color: #1b3d1b;
        font-family: 'Poppins', sans-serif;
    }
    .main-container {
        max-width: 800px;
        margin: 0 auto;
        background: #ffffff;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.05);
    }
    .title {
        text-align: center;
        color: #1B5E20;
        font-size: 2em;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #4CAF50;
        font-size: 1.1em;
        margin-bottom: 2rem;
    }
    .upload-box {
        border: 2px dashed #A5D6A7;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        color: #388E3C;
        background-color: #f1faf1;
        transition: all 0.3s ease-in-out;
    }
    .upload-box:hover {
        background-color: #e8f5e9
    }
    .result-card {
        background: #f9fff9;
        border-left: 6px solid #66BB6A;
        padding: 1.2rem 1.5rem;
        margin-top: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .footer {
        text-align: center;
        color: #777;
        font-size: 0.9em;
        margin-top: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="title">🌿 Klasifikasi Tanaman Herbal Antidiabetes</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload citra daun untuk mengidentifikasi jenis tanaman herbal</div>', unsafe_allow_html=True)

# ==============================
# Upload Gambar
# ==============================
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Gambar yang diunggah", use_container_width=True)
    st.write("🔍 Sedang menganalisis gambar...")

    # --- Simulasi hasil sementara ---
    st.markdown("""
        <div class="result-card">
            <h4>🌱 Hasil Prediksi</h4>
            <b>Tanaman:</b> Orthosiphon aristatus (Kumis Kucing)<br>
            <b>Status:</b> Herbal antidiabetes ✅<br>
            <b>Tingkat kepercayaan model:</b> 92%<br><br>
            <b>Informasi:</b> Mengandung senyawa sinensetin dan orthosiphol yang berpotensi menurunkan kadar gula darah.<br><br>
            🔗 <a href="https://www.sciencedirect.com/science/article/pii/S2213453020300470" target="_blank">Lihat referensi jurnal</a><br>
            🫖 <b>Cara pengolahan:</b> Daun direbus dalam air 200 ml selama 10 menit, diminum 2x sehari.
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">Dibuat oleh <b>Listy Zulmi</b> • Proyek Skripsi Data Science 🌿</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
