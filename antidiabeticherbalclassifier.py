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
        font-size: 26px;
        color: #2E4E1F;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }

    .subtext {
        font-size: 13px;
        color: #3b5323;
        text-align: center;
    }

    /* Tombol navigasi */
    .sidebar-radio label {
        font-size: 16px;
        color: #2E4E1F;
        padding: 8px 12px;
        border-radius: 8px;
        display: block;
    }

    .sidebar-radio label:hover {
        background-color: #dfffba;
        transition: 0.3s;
    }

    /* Header Section */
    .header {
        font-family: 'Playfair Display', serif;
        color: #2E4E1F;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Box konten */
    .upload-box {
        background-color: #F2F8EE;
        border: 2px dashed #8DA77D;
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        transition: 0.3s;
    }

    .upload-box:hover {
        background-color: #E6F2E0;
        border-color: #6b8e23;
    }

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
        background-color: #734b2f;
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

    menu = st.radio("Navigasi", ["Beranda", "Tentang", "Referensi"], label_visibility="collapsed")

    st.markdown("---")
    st.markdown("<small>© 2025 DiaHerb</small>", unsafe_allow_html=True)
    st.markdown("<small>Proyek Skripsi — Listy Zulmi</small>", unsafe_allow_html=True)


# --- Halaman Utama ---
if menu == "Beranda":
    st.markdown("<div class='header'>🌿DiaHerb</div>", unsafe_allow_html=True)
    #st.markdown("<div class='subtext'>Sistem Klasifikasi Tanaman Herbal Antidiabetes</div>", unsafe_allow_html=True)
    st.title("🌿 Sistem Klasifikasi Tanaman Herbal Antidiabetes Beberbasis Deep Learning")
    st.write("Unggah citra daun untuk mengidentifikasi apakah tanaman tersebut termasuk herbal antidiabetes.")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("<div class='upload-box'>📷 Unggah gambar daun (JPG/PNG)</div>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Unggah gambar daun (JPG / PNG) — drag & drop atau klik Browse",
            type=["jpg", "png"],
            label_visibility="collapsed"
        )
        
        st.markdown("""
        <div style="
            border: 2px dashed #bcd9a5;
            border-radius: 10px;
            background-color: #f6f9f3;
            padding: 20px;
            text-align: center;
            ">
            <p style="color:#8B5E3C; font-weight:bold;">Unggah gambar daun (JPG / PNG)</p>
            <p style="color:#666;">Drag & drop atau klik tombol di bawah</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔍 Kenali"):
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.write("🔬 Sedang menganalisis gambar... (simulasi)")
                st.image(image, caption="Hasil gambar yang diunggah", use_column_width=True)
            else:
                st.warning("Silakan unggah gambar terlebih dahulu sebelum mengidentifikasi.")

    with col2:
        st.markdown("<div class='tips-box'><h4>📸 Tips Pengambilan Gambar</h4><ul><li>Ambil satu daun saja, fokus pada objek.</li><li>Gunakan latar belakang polos (putih atau hitam).</li><li>Pencahayaan cukup dan hindari bayangan.</li></ul></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🧪 Hasil Identifikasi (Simulasi)")
    st.info("Nama ilmiah: *Ocimum sanctum* (Kemangi)\n\nStatus: Tanaman herbal antidiabetes\n\nTingkat kepercayaan sistem: **95%**")


elif menu == "Tentang":
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

elif menu == "Referensi":
    st.markdown("<div class='header'>Referensi Ilmiah</div>", unsafe_allow_html=True)
    st.write("""
    1. Hossain, M. A., et al. (2022). *LeafNet: A Deep CNN Model for Plant Identification.*  
    2. Gupta, R. et al. (2023). *Transfer Learning for Medicinal Leaf Classification.*  
    3. Kumar, A. & Singh, R. (2021). *AI-Based Herbal Plant Identification Using ImageNet Pretraining.*  
    4. Listy Zulmi (2025). *Implementasi Model LeafNet untuk Klasifikasi Tanaman Herbal Antidiabetes Berdasarkan Citra Daun.* Skripsi, Universitas Anda.
    """)

st.markdown("<div class='footer'>© 2025 DiaHerb | Sistem Klasifikasi Tanaman Herbal Antidiabetes</div>", unsafe_allow_html=True)
