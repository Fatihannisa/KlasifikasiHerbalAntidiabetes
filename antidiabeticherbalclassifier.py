import streamlit as st

# ==============================
# KONFIGURASI DASAR HALAMAN
# ==============================
st.set_page_config(
    page_title="Klasifikasi Tanaman Herbal Antidiabetes",
    layout="wide",
    page_icon="🌿"
)

# ==============================
# HEADER / JUDUL WEBSITE
# ==============================
st.markdown("<h1 style='text-align:center;'>🌿 Sistem Klasifikasi Tanaman Herbal Antidiabetes 🌿</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Mengidentifikasi jenis tanaman herbal berdasarkan citra daun menggunakan teknologi kecerdasan buatan.</p>", unsafe_allow_html=True)

st.markdown("---")

# ==============================
# NAVIGASI TAB
# ==============================
tab1, tab2, tab3 = st.tabs(["📘 Deskripsi", "🪴 Petunjuk", "📷 Unggah Gambar"])

# ==============================
# TAB 1: DESKRIPSI
# ==============================
with tab1:
    st.subheader("Deskripsi Sistem")
    st.write("""
    Sistem ini dikembangkan untuk membantu pengguna mengenali tanaman herbal antidiabetes melalui citra daun.
    Dengan memanfaatkan model *Transfer Learning* dan arsitektur *LeafNet*, sistem dapat mengklasifikasikan
    citra daun dan menampilkan informasi tambahan mengenai tanaman yang terdeteksi.
    """)

    st.markdown("### Tujuan")
    st.write("- Mempermudah identifikasi tanaman herbal antidiabetes secara cepat dan akurat.")
    st.write("- Menyediakan informasi ilmiah dan edukatif bagi pengguna.")

    st.markdown("### Manfaat")
    st.write("- Mendukung penelitian dan konservasi tanaman herbal lokal.")
    st.write("- Memberikan panduan pengenalan herbal untuk masyarakat umum dan praktisi kesehatan alami.")

# ==============================
# TAB 2: PETUNJUK
# ==============================
with tab2:
    st.subheader("Petunjuk Penggunaan")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/685/685655.png", width=80)
        st.caption("1️⃣ Unggah gambar daun tanaman")

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/992/992651.png", width=80)
        st.caption("2️⃣ Tekan tombol **Identifikasi**")

    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/3131/3131636.png", width=80)
        st.caption("3️⃣ Lihat hasil klasifikasi dan informasi tanaman")

# ==============================
# TAB 3: UNGGAH GAMBAR & HASIL
# ==============================
with tab3:
    st.subheader("Unggah Gambar Daun Anda")

    col1, col2 = st.columns([1.5, 1])
    with col1:
        uploaded_file = st.file_uploader("Unggah gambar daun (JPG/PNG)", type=["jpg", "png"])
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Citra daun yang diunggah", use_column_width=True)

        # Tombol Identifikasi
        if st.button("🔍 Identifikasi", use_container_width=True):
            st.info("Model sedang memproses gambar...")

            # === Proses klasifikasi model di sini ===
            # contoh dummy output:
            st.success("✅ Tanaman teridentifikasi: *Orthosiphon aristatus* (Kumis Kucing)")
            st.write("**Status:** Herbal Antidiabetes")
            st.write("**Tingkat kepercayaan sistem:** 94.3%")

            with st.expander("Informasi Tambahan"):
                st.markdown("""
                - Tanaman ini dikenal sebagai *Kumis Kucing*.
                - Memiliki senyawa aktif seperti sinensetin yang berpotensi menurunkan kadar gula darah.
                """)
                st.markdown("[🔗 Baca artikel ilmiah](https://scholar.google.com)")
                st.markdown("[📖 Panduan pengolahan herbal](https://id.wikipedia.org/wiki/Kumis_kucing)")

    with col2:
        st.markdown("#### Tips Pengambilan Gambar")
        st.write("""
        - Gunakan pencahayaan alami.
        - Pastikan daun tampak utuh.
        - Hindari bayangan atau latar belakang gelap.
        - Gunakan resolusi tinggi agar fitur daun terlihat jelas.
        """)

        st.markdown("#### Contoh Gambar yang Disarankan")
        st.image([
            "https://upload.wikimedia.org/wikipedia/commons/6/6f/Kumis_kucing_leaf.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/3/3d/Curcuma_xanthorrhiza_leaf.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/7/7f/Centella_asiatica_leaves.jpg"
        ], caption=["Kumis Kucing", "Temulawak", "Pegagan"], width=100)

# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.markdown("<p style='text-align:center; font-size:14px;'>© 2025 Sistem Klasifikasi Tanaman Herbal Antidiabetes | Dibangun dengan Streamlit</p>", unsafe_allow_html=True)
