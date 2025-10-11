# app.py
import streamlit as st
from PIL import Image
import io
import time

# -------------------------
# Page config
# -------------------------
st.set_page_config(page_title="DiaHerb 🌿", page_icon="🌿", layout="wide", initial_sidebar_state="collapsed")

# -------------------------
# Theme colors (hijau-coklat herbal alami)
# -------------------------
PRIMARY = "#2E5F44"    # hijau tua
ACCENT = "#7EA57A"     # hijau lembut
EARTH = "#8B6B4A"      # coklat lembut
BG = "#FBF9F4"         # cream / natural bg

# -------------------------
# Custom CSS
# -------------------------
st.markdown(
    f"""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');
    .main-title {
        font-family: 'Playfair Display', serif;
        font-weight: 700;
        font-size: 26 px;
        color: #2e7d32;
        letter-spacing: 0.5 px;
    }
    .sub-title {
        font-family: 'Poppins', sans-serif;
        color: #5b5b5b;
        font-size: 15 px;
    }
    </style>
""", unsafe_allow_html=True)


    st.markdown("""
    <div style="display:flex;align-items:center;gap:10px;">
        <div style="width:48px;height:48px;background:#e6f3e6;border-radius:10px;display:flex;align-items:center;justify-content:center;">
            🌿
        </div>
        <div>
            <div class="main-title">DiaHerb</div>
            <div class="sub-title">Sistem Klasifikasi Tanaman Herbal Antidiabetes</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    /* Page background */
    .reportview-container, .main {{
        background-color: {BG};
    }}

    /* Hide default Streamlit header/menu */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* Top navbar */
    .top-nav {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 18px 32px;
        background: linear-gradient(90deg, rgba(255,255,255,0.8), rgba(255,255,255,0.5));
        border-bottom: 1px solid rgba(0,0,0,0.06);
    }}
    .brand {{
        display:flex;
        align-items:center;
        gap:12px;
        font-family: 'Poppins', sans-serif;
    }}
    .brand img {{
        width:44px; height:44px; border-radius:8px;
    }}
    .brand .title {{
        font-size:22px; color: {PRIMARY}; font-weight:700;
    }}
    .brand .subtitle {{
        font-size:12px; color: {EARTH}; margin-top:-4px;
    }}

    .nav-buttons {{
        display:flex;
        gap:10px;
    }}
    .nav-buttons button {{
        background:{ACCENT};
        color:white;
        border: none;
        padding:10px 14px;
        border-radius:8px;
        cursor:pointer;
        font-weight:600;
    }}
    .nav-buttons button:hover {{
        background:{PRIMARY};
    }}

    /* Main container card */
    .main-card {{
        background: white;
        border-radius:16px;
        padding:28px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.06);
        margin-bottom: 24px;
    }}

    /* Upload box */
    .upload-box {{
        border:2px dashed {ACCENT};
        border-radius:12px;
        background: #f6fbf6;
        padding:26px;
        text-align:center;
    }}

    /* Result card */
    .result-card {{
        border-left:6px solid {ACCENT};
        background: #fbfff8;
        padding:18px;
        border-radius:10px;
    }}

    /* Tips card */
    .tips-card {{
        background: #fffaf5;
        padding:18px;
        border-radius:10px;
        border:1px solid rgba(0,0,0,0.03);
    }}

    /* Responsive: stack nav for small widths */
    @media (max-width: 760px) {{
        .nav-buttons {{ display:none; }}
        .brand .title {{ font-size:18px; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Helper: manage page selection
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

def set_page(p):
    st.session_state.page = p

# -------------------------
# Top navbar (visible on desktop)
# -------------------------
logo_html = f"""
<div class="top-nav">
  <div class="brand">
    <div style="width:44px;height:44px;border-radius:8px;background:#f0f6f0;display:flex;align-items:center;justify-content:center;">
      <span style="font-size:20px;color:{PRIMARY};">🌿</span>
    </div>
    <div>
      <div class="title">DiaHerb</div>
      <div class="subtitle">Sistem Klasifikasi Tanaman Herbal Antidiabetes</div>
    </div>
  </div>
  <div class="nav-buttons">
    <form action="">
      <button formaction="#" onclick="window.parent.postMessage({{isNav:true, page:'Beranda'}}, '*')">Beranda</button>
      <button formaction="#" onclick="window.parent.postMessage({{isNav:true, page:'Tentang'}}, '*')">Tentang</button>
      <button formaction="#" onclick="window.parent.postMessage({{isNav:true, page:'Referensi'}}, '*')">Referensi</button>
    </form>
  </div>
</div>
"""

# Render top navbar HTML. It will send a postMessage when clicked.
st.components.v1.html(logo_html, height=90, scrolling=False)

# Listen for JS postMessage and update session_state.page if message received
# (This component returns a dict when message posted — but streamlit's html component doesn't directly capture postMessage.
#  As fallback: we will also provide normal Streamlit controls below for guaranteed navigation.)

# -------------------------
# Sidebar navigation (useful for mobile)
# -------------------------
with st.sidebar:
    st.markdown("<div style='padding:8px 4px;'><b style='color:"+PRIMARY+"; font-size:18px;'>DiaHerb</b></div>", unsafe_allow_html=True)
    page = st.radio("", ["Beranda", "Tentang", "Referensi"], index=["Beranda","Tentang","Referensi"].index(st.session_state.page) if st.session_state.page in ["Beranda","Tentang","Referensi"] else 0)
    if page != st.session_state.page:
        st.session_state.page = page
    st.markdown("---")
    st.markdown("© 2025 DiaHerb")
    st.markdown("Proyek Skripsi — Listy Zulmi")

# Also give top quick-nav fallback (for users who can't use postMessage)
col1, col2, col3 = st.columns([1,1,1])
with col1:
    if st.button("Beranda"):
        set_page("Beranda")
with col2:
    if st.button("Tentang"):
        set_page("Tentang")
with col3:
    if st.button("Referensi"):
        set_page("Referensi")

st.markdown("")  # spacing

# -------------------------
# Page: Beranda (Home) with Upload & Result
# -------------------------
if st.session_state.page == "Beranda":
    # Container card
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("## 🌿 Beranda — DiaHerb")
    st.markdown("Unggah citra daun untuk mengidentifikasi apakah tanaman tersebut termasuk herbal antidiabetes.")
    st.write("")

    # Two-column: upload left, tips right
    left, right = st.columns([2, 1])

    with left:
        st.markdown('<div class="upload-box">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("", type=["jpg","jpeg","png"], label_visibility="collapsed")
        if uploaded_file:
            # show preview
            img = Image.open(uploaded_file).convert("RGB")
            st.image(img, use_column_width=True, caption="Preview gambar")
        else:
            st.markdown("<div style='padding:40px 0; color:#6b786b;'>📷 Unggah gambar daun (JPG/PNG)</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.write("")
        col_a, col_b = st.columns([1,1])
        with col_a:
            if st.button("🌱 Mulai Analisis"):
                if not uploaded_file:
                    st.warning("Silakan unggah gambar daun terlebih dahulu.")
                else:
                    with st.spinner("🔎 Menganalisis citra..."):
                        time.sleep(1.2)
                        # --- Dummy prediction: replace this with model.predict later ---
                        predicted = "Orthosiphon aristatus"
                        common = "Kumis Kucing"
                        is_antidiabetes = True
                        confidence = 0.92
                        info = "Mengandung senyawa sinensetin dan orthosiphol yang berpotensi menurunkan kadar gula darah."
                        processing = "Daun direbus dalam 200 ml air selama 10 menit; diminum 2x sehari."
                        # ----------------------------------------
                        st.success("✅ Analisis selesai")
                        st.markdown(f"""
                        <div class="result-card">
                        <h4>Hasil Identifikasi</h4>
                        <b>Tanaman:</b> <i>{predicted}</i> ({common})<br>
                        <b>Status:</b> {'Herbal antidiabetes ✅' if is_antidiabetes else 'Bukan herbal antidiabetes'}<br>
                        <b>Tingkat Kepercayaan:</b> {int(confidence*100)}%<br><br>
                        <b>Informasi:</b><br>{info}<br><br>
                        <b>Cara Pengolahan (tradisional):</b><br>{processing}
                        </div>
                        """, unsafe_allow_html=True)

        with col_b:
            if st.button("🔁 Unggah ulang"):
                # clearing file uploader is not straightforward; rely on user to re-upload or refresh
                st.experimental_rerun()

    with right:
        st.markdown('<div class="tips-card">', unsafe_allow_html=True)
        st.markdown("### 📸 Tips Pengambilan Gambar")
        st.markdown("""
        - Fokus pada **satu daun** (jangan ambil banyak sekaligus).  
        - Gunakan **pencahayaan alami**, hindari bayangan dan flash.  
        - Gunakan **latar belakang polos** (kertas putih/gelap sesuai kontras).  
        - Ambil dari posisi **tegak lurus** ke permukaan daun.  
        - Pastikan daun tidak robek/terlalu basah.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # end main-card

# -------------------------
# Page: Tentang
# -------------------------
elif st.session_state.page == "Tentang":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("## Tentang DiaHerb 🌿")
    st.markdown("""
    **DiaHerb** adalah sistem cerdas berbasis *deep learning* yang dirancang untuk mengidentifikasi tanaman herbal  
    yang berpotensi sebagai agen antidiabetes dengan menggunakan citra daun.
    """)
    st.markdown("### 🎯 Tujuan")
    st.markdown("- Membantu penelitian dan konservasi tanaman herbal antidiabetes.")
    st.markdown("- Menyediakan alat bantu identifikasi yang mudah untuk masyarakat dan peneliti.")
    st.markdown("### 💡 Manfaat")
    st.markdown("- Edukasi masyarakat tentang tanaman herbal antidiabetes.")
    st.markdown("- Dukungan penelitian fitofarmasi dan dokumentasi etnobotani.")
    st.markdown("### ⚙️ Cara Kerja (ringkas)")
    st.markdown("""
    1. **Preprocessing**: resize & normalisasi citra daun.  
    2. **Feature extraction**: menggunakan arsitektur CNN (pretrained via Transfer Learning).  
    3. **Klasifikasi**: model memprediksi label (nama ilmiah) dan memberikan confidence score.  
    4. **Output**: sistem menampilkan nama ilmiah, status (antidiabetes atau bukan), informasi kandungan, dan referensi.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Page: Referensi
# -------------------------
elif st.session_state.page == "Referensi":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("## Referensi Ilmiah 📚")
    st.markdown("""
    1. S. M. Azam et al., *LeafNet: A Deep CNN Model for Plant Leaf Classification*, Journal of Computational Botany, 2021.  
    2. D. P. Kingma & J. Ba, *Adam: A Method for Stochastic Optimization*, arXiv:1412.6980, 2014.  
    3. A. Wijaya et al., *Detection of Antidiabetic Herbal Plants Using CNN and Transfer Learning*, 2023.  
    4. H. Prasetyo et al., *Phytochemical studies of Orthosiphon aristatus and antidiabetic activity*, 2020.  
    5. -- tambahkan referensi jurnal dan dataset sesuai skripsi --
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Footer (global)
# -------------------------
st.markdown("<div style='margin-top:30px; text-align:center; color: #5a5a5a;'>© 2025 DiaHerb — Listy Zulmi • Proyek Skripsi Data Science</div>", unsafe_allow_html=True)
