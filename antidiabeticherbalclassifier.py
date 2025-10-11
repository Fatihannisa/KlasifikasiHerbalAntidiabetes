import streamlit as st
from PIL import Image
import io
import time

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="DiaHerb", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")

# ---------------------------
# Theme colors (user requested)
# ---------------------------
GREEN = "#bcd9a5"
BROWN = "#8B5E3C"
BG = "#FBFAF8"

# ---------------------------
# CSS styling
# ---------------------------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');

    /* global */
    html, body, .stApp {{
        background-color: {BG};
        font-family: 'Poppins', sans-serif;
    }}

    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {GREEN} 0%, #d6e9c6 100%);
        color: {BROWN};
        border-right: 1px solid rgba(0,0,0,0.06);
        padding-top: 18px;
    }}
    [data-testid="stSidebar"] .css-1d391kg {{ padding-left: 18px; padding-right: 18px; }}

    .sidebar .title {{
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        color: {BROWN};
        font-weight: 700;
    }}
    .sidebar .subtitle {{
        font-size:12px;
        color: rgba(0,0,0,0.6);
        margin-bottom: 12px;
    }}

    /* Main header */
    .main-header {{
        display:flex;
        align-items:center;
        gap:14px;
        margin-bottom: 18px;
    }}
    .brand-title {{
        font-family: 'Playfair Display', serif;
        color: {BROWN};
        font-size:28px;
        font-weight:700;
        margin:0;
    }}
    .brand-sub {{
        font-size:13px;
        color: rgba(0,0,0,0.65);
        margin-top: -6px;
    }}

    /* Upload box */
    .upload-box {{
        border-radius: 14px;
        background: linear-gradient(180deg, #f7fbf7 0%, #f2f7f2 100%);
        border: 2px dashed {GREEN};
        padding: 26px;
        text-align: center;
        transition: all 0.2s ease;
    }}
    .upload-box.hover {{
        background: #eef7ea;
        border-color: #9ecb85;
    }}
    .upload-instruction {{
        color: rgba(0,0,0,0.7);
        font-size:16px;
        margin-bottom: 12px;
    }}

    /* style file_uploader box inside */
    .stFileUpload {{}}
    .browse-button {{
        border-radius:10px;
        background: white;
        border: 1px solid rgba(0,0,0,0.08);
        padding:6px 10px;
    }}

    /* Kenali button centered */
    .kenali-wrapper {{
        display:flex;
        justify-content:center;
        margin-top:14px;
    }}
    .kenali-btn {{
        background: linear-gradient(180deg, {BROWN} 0%, #6d3f2a 100%);
        color: white;
        padding:10px 24px;
        border-radius: 10px;
        font-weight:600;
        border: none;
        cursor:pointer;
    }}
    .kenali-btn:active {{ transform: translateY(1px); }}

    /* Result card */
    .result-card {{
        background: white;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    }}

    /* Tips box */
    .tips-box {{
        background: #fff7e6;
        padding: 14px;
        border-radius: 10px;
        border-left: 4px solid #e6b800;
    }}

    /* small helpers */
    .muted {{ color: rgba(0,0,0,0.55); font-size:13px; }}
    .section-title {{ font-family: 'Playfair Display', serif; color: {BROWN}; font-size:20px; margin-bottom:8px; }}

    @media (max-width: 760px) {{
        .brand-title {{ font-size:20px; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Session state keys
# ---------------------------
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None  # bytes
if "result" not in st.session_state:
    st.session_state.result = None  # dict with prediction

# ---------------------------
# Sidebar (navigation)
# ---------------------------
with st.sidebar:
    st.markdown('<div class="sidebar"><div class="title">DiaHerb</div><div class="subtitle">Sistem Klasifikasi Tanaman Herbal Antidiabetes</div></div>', unsafe_allow_html=True)
    page = st.radio("", ["Beranda", "Tentang", "Referensi"], index=0)
    st.markdown("---")
    st.markdown("© 2025 DiaHerb")
    st.markdown("Proyek Skripsi — Listy Zulmi")

# ---------------------------
# Main content
# ---------------------------
# Header / brand area
st.markdown('<div class="main-header"><div style="width:48px;height:48px;border-radius:10px;background:#eef7ea;display:flex;align-items:center;justify-content:center;font-size:22px;">🌿</div><div><div class="brand-title">DiaHerb</div><div class="brand-sub">Sistem Klasifikasi Tanaman Herbal Antidiabetes</div></div></div>', unsafe_allow_html=True)

# Page switch
if page == "Beranda":
    st.markdown('<div class="section-title">Beranda</div>', unsafe_allow_html=True)
    st.write("Unggah citra daun untuk mengidentifikasi apakah tanaman tersebut termasuk herbal antidiabetes.")
    st.write("")  # spacer

    left, right = st.columns([2, 1])

    with left:
        # Upload box area (styled). Place file_uploader inside.
        st.markdown('<div class="upload-box">', unsafe_allow_html=True)
        st.markdown('<div class="upload-instruction">📷 Unggah gambar daun (JPG / PNG) — drag & drop atau klik Browse</div>', unsafe_allow_html=True)

        # file_uploader (it supports drag & drop). Keep it visually minimal by hiding label via label_visibility
        uploaded = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        if uploaded:
            # read bytes and store in session
            bytes_data = uploaded.read()
            st.session_state.uploaded_image = bytes_data
            # show small preview inside upload area
            st.image(Image.open(io.BytesIO(bytes_data)), use_column_width=False, width=420, caption="Preview")
        else:
            # show placeholder (empty)
            st.markdown("<div style='height:140px'></div>", unsafe_allow_html=True)

        # Kenali button centered
        st.markdown('</div>', unsafe_allow_html=True)  # close upload-box
        st.markdown("<div class='kenali-wrapper'>", unsafe_allow_html=True)
        # Use st.button but style via markdown button fallback: simpler to use st.button
        if st.button("🔎 Kenali", key="kenali"):
            if st.session_state.uploaded_image is None:
                st.warning("Silakan unggah gambar daun terlebih dahulu.")
            else:
                # simulate processing (replace with model inference later)
                with st.spinner("Menganalisis gambar..."):
                    time.sleep(1.0)
                    # Dummy prediction results (replace with real model later)
                    st.session_state.result = {
                        "predicted": "Orthosiphon aristatus",
                        "common": "Kumis Kucing",
                        "is_antidiabetes": True,
                        "confidence": 0.92,
                        "info": "Mengandung senyawa sinensetin dan orthosiphol yang berpotensi menurunkan kadar gula darah.",
                        "processing": "Rebus 10-15 gram daun kering dalam 500 ml air hingga tersisa 200 ml. Minum 1 gelas sehari."
                    }
                    # Scroll to results — Streamlit doesn't provide scroll control reliably, but results will render below
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="tips-box"><h4>📸 Tips Pengambilan Gambar</h4><ul style="margin-top:6px;"><li>Fokus pada <b>satu daun</b>.</li><li>Gunakan <b>pencahayaan alami</b> dan hindari bayangan.</li><li>Latar belakang polos (kertas putih/gelap) membantu akurasi.</li><li>Ambil dari sudut tegak lurus ke permukaan daun.</li></ul></div>', unsafe_allow_html=True)

    st.markdown("---")

    # Hasil Identifikasi Section (renders when result exists)
    st.markdown('<div class="section-title">Hasil Identifikasi</div>', unsafe_allow_html=True)

    if st.session_state.result is None:
        st.info("Belum ada hasil. Unggah gambar lalu tekan tombol **Kenali** untuk melihat hasil identifikasi di sini.")
    else:
        res = st.session_state.result
        # layout similar to mockup: image left, name center, status right
        col_img, col_meta, col_status = st.columns([1.2, 1.5, 1])

        with col_img:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.image(Image.open(io.BytesIO(st.session_state.uploaded_image)), use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_meta:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown(f"### **Nama Ilmiah**\n*{res['predicted']}*")
            st.markdown(f"**Nama umum:** {res['common']}")
            st.markdown("</div>", unsafe_allow_html=True)

        with col_status:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            status_text = "Herbal antidiabetes ✅" if res["is_antidiabetes"] else "Bukan herbal antidiabetes"
            st.markdown(f"**Status:** {status_text}")
            st.markdown(f"**Tingkat kepercayaan:** {int(res['confidence']*100)}%")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        # Information box
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### Informasi")
        st.write(res["info"])
        st.markdown("</div>", unsafe_allow_html=True)

        # Links area (placeholders)
        st.markdown('<div style="margin-top:12px"></div>', unsafe_allow_html=True)
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("**Tautan artikel**")
        st.markdown("- (Contoh) Artikel populer tentang Orthosiphon aristatus.")
        st.markdown("**Tautan jurnal penelitian**")
        st.markdown("- (Contoh) Jurnal fitokimia dan uji aktivitas antidiabetes.")
        st.markdown("</div>", unsafe_allow_html=True)

        # Cara pengolahan
        st.markdown('<div style="margin-top:12px"></div>', unsafe_allow_html=True)
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### Cara Mengolah (tradisional)")
        st.markdown("1. Langkah 1\n2. Langkah 2\n3. Langkah 3\n4. dst.")
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "Tentang":
    st.markdown('<div class="section-title">Tentang DiaHerb</div>', unsafe_allow_html=True)
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown("""
    **DiaHerb** adalah sistem cerdas berbasis *deep learning* yang digunakan untuk mengidentifikasi tanaman herbal antidiabetes dari citra daun.

    **Tujuan:** membantu identifikasi cepat tanaman herbal berpotensi antidiabetes dan mendukung penelitian fitofarmasi.

    **Cara kerja (ringkas):**
    1. Preprocessing (resize & normalize).  
    2. Ekstraksi fitur menggunakan CNN (pretrained + transfer learning).  
    3. Klasifikasi & keluaran confidence score serta metadata informatif.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Referensi":
    st.markdown('<div class="section-title">Referensi Ilmiah</div>', unsafe_allow_html=True)
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown("""
    1. Zhang, X., et al. (2022). *LeafNet: A Deep Learning Approach for Plant Identification.*  
    2. Tan, M., & Le, Q. (2021). *EfficientNetV2: Smaller Models and Faster Training.*  
    3. Prasetyo, H., et al. (2020). *Phytochemical study of Orthosiphon aristatus and antidiabetic activity.*  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("<div style='margin-top:24px; text-align:center; color:rgba(0,0,0,0.55); font-size:13px;'>© 2025 DiaHerb — Listy Zulmi</div>", unsafe_allow_html=True)
