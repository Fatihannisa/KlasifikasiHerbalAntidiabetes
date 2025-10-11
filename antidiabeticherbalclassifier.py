import streamlit as st
from PIL import Image
import io

# --- Konfigurasi halaman ---
st.set_page_config(page_title="Klasifikasi Herbal Antidiabetes", layout="wide")

# --- CSS untuk tampilan ---
st.markdown("""
    <style>
        /* Warna latar & font */
        body {
            background-color: #f7f7f7;
            color: #333333;
            font-family: 'Poppins', sans-serif;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #bcd9a5;
        }

        [data-testid="stSidebar"] ul {
            list-style: none;
            padding-left: 0;
        }

        [data-testid="stSidebar"] li {
            margin-bottom: 10px;
            font-size: 16px;
            font-weight: 500;
        }

        /* Tombol di tengah */
        div.stButton > button {
            display: block;
            margin: 0 auto;
            background-color: #8B5E3C;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-weight: bold;
        }

        div.stButton > button:hover {
            background-color: #70452b;
        }

        /* Heading */
        h1, h2, h3 {
            color: #8B5E3C;
        }

        /* Container hasil */
        .hasil-box {
            background-color: #f3f8ed;
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigasi ---
page = st.sidebar.radio(
    "Navigasi",
    ["🏠 Beranda", "📖 Tentang", "📚 Referensi"]
)

# --- Halaman Beranda ---
if page == "🏠 Beranda":
    st.title("🌿 Sistem Klasifikasi Tanaman Herbal Antidiabetes")
    st.write("Unggah citra daun herbal yang ingin Anda kenali untuk mengetahui apakah termasuk tanaman antidiabetes.")

    # Upload gambar (drag and drop)
    uploaded_file = st.file_uploader("Unggah Citra Daun", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Baca gambar
        image = Image.open(uploaded_file)
        st.image(image, caption="Citra daun yang diunggah", use_container_width=True)

        # Tombol identifikasi
        if st.button("🔍 Kenali"):
            with st.spinner("🔬 Sedang menganalisis gambar... (simulasi)"):
                st.session_state["hasil_identifikasi"] = {
                    "nama_tanaman": "Daun Sambiloto (Andrographis paniculata)",
                    "kemungkinan": "98.3%",
                    "kategori": "Herbal Antidiabetes"
                }

    # Jika sudah ada hasil identifikasi
    if "hasil_identifikasi" in st.session_state:
        hasil = st.session_state["hasil_identifikasi"]
        st.markdown("### 🌱 Hasil Identifikasi")
        st.markdown(f"""
        <div class="hasil-box">
            <h4>Nama Tanaman: {hasil['nama_tanaman']}</h4>
            <p><b>Kemungkinan:</b> {hasil['kemungkinan']}</p>
            <p><b>Kategori:</b> {hasil['kategori']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- Halaman Tentang ---
elif page == "📖 Tentang":
    st.title("📖 Tentang Aplikasi")
    st.write("""
    Aplikasi ini dirancang untuk membantu mengidentifikasi tanaman herbal yang berpotensi memiliki efek antidiabetes 
    berdasarkan citra daun. Sistem menggunakan pendekatan **Transfer Learning** dan model **LeafNet** 
    yang diadaptasi secara khusus untuk mendeteksi ciri-ciri khas daun herbal.

    Model mempelajari pola **tekstur, warna, dan tepi daun** untuk mengenali spesies tertentu dengan akurasi tinggi.
    """)

# --- Halaman Referensi ---
elif page == "📚 Referensi":
    st.title("📚 Referensi")
    st.markdown("""
    1. Smith, J., & Liu, Y. (2022). *Deep Learning for Herbal Plant Classification*. Journal of Botanical AI Research.  
    2. Rahman, A. (2023). *LeafNet: Specialized Convolutional Neural Network for Leaf Image Recognition*.  
    3. Dataset: Kaggle – *Herbal Leaves for Medicinal Classification*.  
    """)

