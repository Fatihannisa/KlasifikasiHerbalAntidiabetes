import streamlit as st
from PIL import Image
import base64

# --- Konfigurasi halaman ---
st.set_page_config(page_title="DiaHerb", page_icon="🌿", layout="wide")

# --- CSS Kustom ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #d6ffba;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #d6f0ce 0%, #b6d7a8 100%);
        color: #2E4E1F;
        padding-top: 2rem;
        border-right: 2px solid #e0e0e0;
    }

    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        font-family: 'Playfair Display', serif;
        color: #2E4E1F;
        text-align: center;
    }

    /* Logo Judul di Sidebar */
    .logo-text {
        font-family: 'Playfair Display', serif;
        font-size: 30px;
        color: #2E4E1F;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }

    .subtext {
        font-size: 16px;
        color: #3b5323;
        text-align: left;
    }

    /* Tombol navigasi */
    .sidebar-radio label {
        font-size: 16px;
        color: #2E4E1F;
        padding: 8px 12px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .sidebar-radio label:hover {
        background-color: #dfffba;
        transition: 0.3s;
    }

    /* Header Section */
    .header {
        font-family: 'Playfair Display', serif;
        color: #2E4E1F;
        font-size: 60px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Tombol kenali di tengah */
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background-color: #8B5E3C;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        background-color: #bfe8a0;
        transform: scale(1.05);
    }

    .tips-box {
        background-color: #f7f1e1;
        border-left: 4px solid #a18d58;
        border-radius: 10px;
        padding: 15px;
    }

    .footer {
        text-align: center;
        color: #6B705C;
        font-size: 13px;
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)


# --- Sidebar Navigasi ---
with st.sidebar:
    st.markdown("<div class='logo-text'>DiaHerb</div>", unsafe_allow_html=True)
    st.markdown("---")

    menu = st.radio("Navigasi", ["🌿 Beranda", "ℹ️ Tentang", "📚 Referensi"], label_visibility="collapsed")

    st.markdown("---")
    st.markdown("<small>© 2025 DiaHerb</small>", unsafe_allow_html=True)
    st.markdown("<small>Proyek Skripsi — Listy Zulmi</small>", unsafe_allow_html=True)


# --- Halaman Utama ---
if menu == "🌿 Beranda":
    st.markdown("<div class='header'>🌿DiaHerb</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtext'>Sistem Klasifikasi Tanaman Herbal Antidiabetes Berbasis Deep Learning</div>", unsafe_allow_html=True)
    st.write("Unggah citra daun untuk mengidentifikasi apakah tanaman tersebut termasuk herbal antidiabetes.")

    col1, col2 = st.columns([2, 1])

    with col1:
        uploaded_file = st.file_uploader("📷 Unggah gambar daun (JPG / PNG)", type=["jpg", "png", "jpeg"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Gambar yang diunggah", use_container_width=True)
            st.success("✅ Gambar berhasil diunggah!")

        if st.button("🔍 Kenali"):
            if uploaded_file is not None:
                st.write("🔬 Sedang menganalisis gambar... *(simulasi)*")
                st.image(image, caption="Citra hasil identifikasi", use_container_width=True)
                st.info("**Nama ilmiah:** *Ocimum sanctum* (Kemangi)\n\n**Status:** Tanaman herbal antidiabetes\n\n**Tingkat kepercayaan sistem:** 95%")
            else:
                st.warning("⚠️ Silakan unggah gambar terlebih dahulu sebelum mengidentifikasi.")

    with col2:
        st.markdown("""
        <div class='tips-box'>
        <h4>📸 Tips Pengambilan Gambar</h4>
        <ul>
            <li>Ambil satu daun saja, fokus pada objek.</li>
            <li>Gunakan latar belakang polos (putih atau hitam).</li>
            <li>Pencahayaan cukup dan hindari bayangan.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif menu == "ℹ️ Tentang":
    st.markdown("<div class='header'>Tentang — DiaHerb</div>", unsafe_allow_html=True)
    st.write("""
    **DiaHerb** adalah sistem berbasis *Deep Learning* yang dirancang untuk membantu identifikasi tanaman herbal antidiabetes melalui citra daun.  
    Sistem ini bertujuan untuk mendukung masyarakat, peneliti, dan pelaku industri herbal dalam mengenali tanaman berpotensi antidiabetes dengan lebih cepat dan akurat.

    ### 🎯 Tujuan
    - Mengidentifikasi tanaman herbal antidiabetes berdasarkan citra daun.  
    - Meningkatkan kesadaran masyarakat tentang potensi tanaman lokal.  
    - Mendukung penelitian dan pengembangan obat herbal.

    ### 🌿 Manfaat
    - Alternatif identifikasi berbasis AI.  
    - Hemat waktu dalam proses pengenalan tanaman.  
    - Dapat digunakan di lapangan oleh siapa saja.

    ### ⚙️ Cara Kerja Sistem
    - Gambar daun diunggah ke sistem.
    - Model *Transfer Learning* menganalisis ciri morfologi daun.
    - Sistem menampilkan hasil identifikasi, status herbal, dan tingkat kepercayaannya.
    """)

elif menu == "📚 Referensi":
    st.markdown("<div class='header'>Referensi Ilmiah</div>", unsafe_allow_html=True)
    st.write("""
    1. Hossain, M. A., et al. (2022). *LeafNet: A Deep CNN Model for Plant Identification.*  
    2. Gupta, R. et al. (2023). *Transfer Learning for Medicinal Leaf Classification.*  
    3. Kumar, A. & Singh, R. (2021). *AI-Based Herbal Plant Identification Using ImageNet Pretraining.*  
    4. Listy Zulmi (2025). *Implementasi Model LeafNet untuk Klasifikasi Tanaman Herbal Antidiabetes Berdasarkan Citra Daun.* Skripsi, Universitas Anda.
    """)

st.markdown("<div class='footer'>© 2025 DiaHerb | Sistem Klasifikasi Tanaman Herbal Antidiabetes</div>", unsafe_allow_html=True)
