import streamlit as st

# ======== Konfigurasi Halaman ========
st.set_page_config(
    page_title="DiaHerb | Klasifikasi Herbal Antidiabetes",
    page_icon="🌿",
    layout="wide"
)

# ======== CSS Styling ========
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600&display=swap');

    /* Warna tema */
    :root {
        --primary-green: #2E7D32;
        --brown-natural: #5D4037;
        --soft-bg: #F1F8E9;
    }

    /* Background keseluruhan */
    .stApp {
        background-color: var(--soft-bg);
    }

    /* Judul Utama */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 38px;
        font-weight: 700;
        color: var(--primary-green);
        text-align: center;
        margin-bottom: 0px;
    }

    /* Subjudul */
    .sub-title {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        color: var(--brown-natural);
        text-align: center;
        margin-top: -8px;
        margin-bottom: 40px;
    }

    /* Box konten */
    .content-box {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    }

    /* Heading halaman */
    h2 {
        color: var(--primary-green);
        font-family: 'Inter', sans-serif;
        font-weight: 600;
    }

    /* Footer */
    footer {
        text-align: center;
        color: #666;
        margin-top: 40px;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# ======== Sidebar Navigasi ========
st.sidebar.title("🌿 DiaHerb")
menu = st.sidebar.radio("Navigasi", ["Beranda", "Tentang", "Referensi"])

st.sidebar.markdown("---")
st.sidebar.caption("© 2025 DiaHerb\n\nProyek Skripsi — Listy Zulmi")

# ======== HALAMAN BERANDA ========
if menu == "Beranda":
    st.markdown("<h1 class='main-title'>🌿 DiaHerb</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Sistem Klasifikasi Tanaman Herbal Antidiabetes</p>", unsafe_allow_html=True)

    st.markdown("### 📸 Unggah Citra Daun")
    st.markdown("Unggah gambar daun untuk mengidentifikasi apakah tanaman tersebut termasuk herbal antidiabetes.")

    uploaded_file = st.file_uploader("Pilih gambar daun (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Citra daun yang diunggah", use_column_width=True)
        st.success("✅ Gambar berhasil diunggah! (Integrasikan dengan model di sini nanti)")

    with st.expander("💡 Tips Pengambilan Gambar"):
        st.write("""
        - Gunakan **pencahayaan alami** agar warna daun tampak jelas.  
        - Fokus pada **satu daun** saja (jangan ambil banyak sekaligus).  
        - Pastikan **background polos** agar sistem mudah mengenali pola daun.
        """)

# ======== HALAMAN TENTANG ========
elif menu == "Tentang":
    st.markdown("<h1 class='main-title'>🌿 Tentang DiaHerb</h1>", unsafe_allow_html=True)
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)

    st.markdown("""
    **DiaHerb** adalah sistem klasifikasi berbasis kecerdasan buatan (AI) yang dirancang untuk
    mengidentifikasi tanaman herbal antidiabetes berdasarkan citra daun.

    ### 🎯 Tujuan
    - Membantu peneliti, mahasiswa, dan masyarakat umum mengenali tanaman herbal antidiabetes.  
    - Mendukung digitalisasi pengetahuan herbal Indonesia melalui teknologi AI.

    ### 🌱 Manfaat
    - Meningkatkan efisiensi identifikasi tanaman secara cepat dan akurat.  
    - Mengurangi kesalahan dalam pengenalan tanaman herbal yang mirip secara visual.  
    - Menjadi dasar pengembangan aplikasi edukatif dan riset lebih lanjut.

    ### ⚙️ Cara Kerja Model
    1. **Preprocessing:** Gambar daun diubah menjadi ukuran standar (mis. 224x224 piksel).  
    2. **Ekstraksi Fitur:** Sistem menggunakan model *LeafNet* yang telah diintegrasikan dengan pendekatan *Transfer Learning*.  
    3. **Klasifikasi:** Model mengenali pola bentuk, tepi, dan tekstur daun untuk menentukan apakah tanaman tergolong herbal antidiabetes.  
    4. **Output:** Sistem menampilkan hasil prediksi dengan tingkat kepercayaan (confidence score).

    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ======== HALAMAN REFERENSI ========
elif menu == "Referensi":
    st.markdown("<h1 class='main-title'>📚 Referensi</h1>", unsafe_allow_html=True)
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)

    st.markdown("""
    Berikut beberapa referensi ilmiah yang menjadi dasar pengembangan sistem **DiaHerb**:

    1. Zhang, X., et al. (2022). *LeafNet: A Deep Learning Approach for Plant Species Classification Based on Leaf Images.*  
    2. Tan, M., & Le, Q. (2021). *EfficientNetV2: Smaller Models and Faster Training.*  
    3. He, K., et al. (2016). *Deep Residual Learning for Image Recognition (ResNet).*  
    4. Chollet, F. (2017). *Xception: Deep Learning with Depthwise Separable Convolutions.*  
    5. Dataset tanaman herbal diadaptasi dari hasil kurasi penelitian lokal dan sumber terbuka (Kaggle, PlantVillage, dan HerbDataID).

    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ======== FOOTER ========
st.markdown("<footer>© 2025 DiaHerb | Sistem Klasifikasi Tanaman Herbal Antidiabetes</footer>", unsafe_allow_html=True)
