import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# ====================================
# KONFIGURASI AWAL
# ====================================
st.set_page_config(page_title="Klasifikasi Tanaman Herbal Antidiabetes", layout="centered")

# Muat model
@st.cache_resource
def load_herbal_model():
    model = load_model("model_herbal_antidiabetes.h5")  # ganti dengan nama file kamu
    return model

model = load_herbal_model()

# Label kelas
CLASS_NAMES = [
    "Daun Sirsak", "Daun Salam", "Daun Pegagan", "Daun Jati Belanda",
    "Daun Sirih", "Daun Kemangi", "Daun Insulin", "Daun Kelor",
    "Daun Mangga", "Daun Belimbing Wuluh", "Daun Afrika", "Daun Brotowali",
    "Daun Tapak Dara", "Daun Katuk", "Daun Dewa", "Daun Mengkudu",
    "Daun Pandan", "Daun Tempuyung", "Daun Lidah Buaya", "Daun Seledri"
]

# ====================================
# HEADER
# ====================================
st.markdown("## 🌿 Klasifikasi Tanaman Herbal Antidiabetes")
st.markdown("Sistem deteksi tanaman herbal berbasis citra daun menggunakan model **LeafNet dengan Transfer Learning**.")

st.divider()

# ====================================
# TAB NAVIGASI
# ====================================
tab1, tab2, tab3 = st.tabs(["🧾 Deskripsi", "📘 Petunjuk", "📷 Unggah Gambar"])

# =========================
# TAB 1 – DESKRIPSI SISTEM
# =========================
with tab1:
    st.subheader("Deskripsi Sistem")
    st.write("""
    Sistem ini digunakan untuk mengidentifikasi jenis tanaman herbal antidiabetes berdasarkan citra daun.
    Model dilatih menggunakan pendekatan **Transfer Learning** dengan arsitektur khusus **LeafNet**.
    """)

# =========================
# TAB 2 – PETUNJUK
# =========================
with tab2:
    st.subheader("Petunjuk Penggunaan")
    st.write("1️⃣ Unggah gambar daun herbal (format JPG/PNG).")  
    st.write("2️⃣ Tekan tombol **Identifikasi**.")  
    st.write("3️⃣ Hasil klasifikasi dan tingkat kepercayaan sistem akan muncul di bawah.")  

    st.info("""
    **Tips Pengambilan Gambar:**
    - Pastikan daun berada di latar belakang polos.
    - Hindari bayangan atau cahaya berlebih.
    - Fokuskan kamera pada daun secara keseluruhan.
    """)

# =========================
# TAB 3 – UNGGAH & HASIL
# =========================
with tab3:
    st.subheader("Unggah Gambar")
    uploaded_file = st.file_uploader("Unggah gambar daun (JPG/PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image_data = Image.open(uploaded_file).convert("RGB")
        st.image(image_data, caption="Gambar yang diunggah", use_container_width=True)

        if st.button("🔍 Identifikasi"):
            with st.spinner("Sedang menganalisis gambar..."):
                # Preprocessing gambar
                img = image_data.resize((224, 224))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array /= 255.0

                # Prediksi
                predictions = model.predict(img_array)
                class_index = np.argmax(predictions[0])
                confidence = predictions[0][class_index] * 100
                predicted_label = CLASS_NAMES[class_index]

            # =========================
            # HASIL IDENTIFIKASI
            # =========================
            st.success("✅ Hasil Identifikasi")
            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(image_data, width=150)
            with col2:
                st.markdown(f"**Nama Ilmiah:** *{predicted_label}*")
                st.markdown(f"**Tingkat Kepercayaan Sistem:** {confidence:.2f}%")

            # Contoh tambahan informasi (opsional)
            st.subheader("Informasi Tambahan")
            st.write("Jika tanaman ini termasuk herbal antidiabetes, berikut referensi yang relevan:")

            st.markdown("""
            - 🔗 [Artikel Penelitian Terkait](https://scholar.google.com/)
            - 🔗 [Referensi Penggunaan Tradisional](https://id.wikipedia.org/)
            - 🔗 [Panduan Pengolahan Herbal](https://example.com)
            """)

# ====================================
# FOOTER
# ====================================
st.divider()
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2025 Sistem Klasifikasi Tanaman Herbal Antidiabetes | Dibangun dengan Streamlit</p>",
    unsafe_allow_html=True
)
