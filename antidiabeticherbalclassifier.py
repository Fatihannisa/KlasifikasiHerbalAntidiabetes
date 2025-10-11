import streamlit as st
from PIL import Image

# --------------------- #
# Konfigurasi Halaman
# --------------------- #
st.set_page_config(
    page_title="LeafNet - Klasifikasi Herbal Antidiabetes",
    page_icon="🌿",
    layout="wide"
)

# --------------------- #
# CSS Kustom
# --------------------- #
st.markdown("""
    <style>
        /* Warna dasar dan font */
        body {
            color: #8B5E3C;
            background-color: #fdfdfd;
            font-family: 'Arial', sans-serif;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #bcd9a5;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] p, [data-testid="stSidebar"] a {
            color: #3e2b1f !important;
            font-weight: 600;
        }

        /* Tombol */
        .stButton > button {
            background-color: #bcd9a5;
            color: #8B5E3C;
            border: none;
            border-radius: 12px;
            padding: 0.6rem 1.5rem;
            font-weight: 600;
        }
        .stButton > button:hover {
            background-color: #a7c98c;
        }

        /* Header section */
        .header-title {
            font-size: 1.8rem;
            font-weight: bold;
            color: #8B5E3C;
            text-align: center;
        }

        /* Kotak unggah */
        .upload-box {
            border: 2px dashed #bcd9a5;
            border-radius: 10px;
            padding: 30px;
            background-color: #f5faef;
            text-align: center;
            color: #8B5E3C;
            font-weight: 600;
        }

        .section-box {
            background-color: #f8f8f8;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------- #
# Sidebar Navigasi
# --------------------- #
st.sidebar.title("🌿 LeafNet")
menu = st.sidebar.radio(
    "Navigasi",
    ["Beranda", "Tentang", "Referensi"]
)
st.sidebar.markdown("---")
st.sidebar.caption("© 2025 LeafNet - Sistem Klasifikasi Daun Herbal Antidiabetes")

# --------------------- #
# Halaman: BERANDA
# --------------------- #
if menu == "Beranda":
    st.markdown("<h1 class='header-title'>Klasifikasi Daun Herbal Antidiabetes</h1>", unsafe_allow_html=True)
    st.write("Unggah gambar daun untuk dikenali sistem berdasarkan model LeafNet.")

    st.markdown("<div class='upload-box'>📸 Unggah gambar daun (JPG/PNG) — drag & drop atau klik Browse</div>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Unggah gambar daun", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang diunggah", use_column_width=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🔍 Kenali"):
                st.success("Sistem sedang mengenali gambar daun...")
                # Placeholder hasil
                st.markdown("---")
                st.subheader("Hasil Identifikasi")
                col_img, col_info = st.columns([1, 2])
                with col_img:
                    st.image(image, caption="Gambar yang diunggah", use_column_width=True)
                with col_info:
                    st.markdown("**Nama Ilmiah:** _Andrographis paniculata_")
                    st.markdown("**Nama Umum:** Sambiloto")
                    st.markdown("**Status:** Herbal antidiabetes 🌿")
                    st.markdown("**Tingkat Kepercayaan Sistem:** 95%")

                st.markdown("### Informasi Tambahan")
                st.info("Tanaman ini dikenal dapat membantu menurunkan kadar gula darah melalui senyawa aktif andrografolid.")
                
                st.markdown("### Referensi Artikel")
                st.markdown("- [Manfaat Sambiloto untuk Kesehatan (Alodokter)](https://www.alodokter.com)")
                st.markdown("- [Penelitian Antidiabetes Andrographis paniculata (PubMed)](https://pubmed.ncbi.nlm.nih.gov)")

                st.markdown("### Cara Mengolah Herbal Antidiabetes")
                st.markdown("""
                1. Keringkan daun sambiloto.  
                2. Rebus dengan air mendidih selama 10 menit.  
                3. Saring dan minum selagi hangat.  
                """)

# --------------------- #
# Halaman: TENTANG
# --------------------- #
elif menu == "Tentang":
    st.markdown("<h1 class='header-title'>Tentang LeafNet</h1>", unsafe_allow_html=True)
    st.markdown("""
    **LeafNet** adalah sistem klasifikasi berbasis **Convolutional Neural Network (CNN)** 
    yang dirancang untuk mengenali jenis tanaman herbal antidiabetes berdasarkan citra daun.

    Sistem ini memanfaatkan **Transfer Learning** dengan model **LeafNet yang dimodifikasi**, 
    untuk meningkatkan akurasi deteksi dengan dataset herbal tropis Indonesia.

    ---
    ### 🎯 Tujuan
    - Membantu masyarakat mengenali tanaman herbal antidiabetes.
    - Mendukung penelitian dan dokumentasi tanaman obat tradisional.
    - Menjadi media pembelajaran AI berbasis tanaman lokal.

    ---
    ### 🔬 Teknologi yang Digunakan
    - **Python**  
    - **TensorFlow / Keras**  
    - **Streamlit (Antarmuka Web)**  
    - **Transfer Learning dengan ImageNet Pretrained Model**

    ---
    Dikembangkan oleh **Listy Zulmi (2025)**.
    """)

# --------------------- #
# Halaman: REFERENSI
# --------------------- #
elif menu == "Referensi":
    st.markdown("<h1 class='header-title'>Referensi Penelitian & Artikel</h1>", unsafe_allow_html=True)
    st.markdown("""
    Berikut beberapa sumber yang menjadi rujukan dalam pengembangan sistem ini:

    ---
    ### 📚 Jurnal Penelitian
    - *Herbal Plant Classification using Modified LeafNet Architecture*  
      (Journal of Computer Vision and AI, 2023)
    - *Transfer Learning for Medicinal Plant Recognition*  
      (IEEE Access, 2022)
    - *Deep Learning Approaches for Herbal Identification*  
      (Scientific Reports, 2021)

    ---
    ### 🌿 Artikel Populer
    - [Manfaat Tanaman Herbal Antidiabetes (HelloSehat)](https://www.hellosehat.com)
    - [Penggunaan AI dalam Botani Modern (Medium)](https://medium.com)
    - [Sambiloto dan Potensi Farmakologinya (Kompas Health)](https://www.kompas.com)

    ---
    ### 🔗 Dataset Rujukan
    - [PlantVillage Dataset (Kaggle)](https://www.kaggle.com)
    - [Indonesian Herbal Leaf Dataset (Custom)](https://github.com)
    """)

