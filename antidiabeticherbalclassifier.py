import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="Klasifikasi Tanaman Herbal", layout="centered")

# ======================
# Bagian Header
# ======================
st.title("🌿 Sistem Deteksi Tanaman Herbal Antidiabetes")
st.write("Unggah gambar daun herbal untuk diidentifikasi jenisnya menggunakan model AI khusus.")

# ======================
# Fungsi Load & Prediksi
# ======================
@st.cache_resource
def load_tflite_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

def predict_tflite(interpreter, image):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Preprocessing gambar sesuai ukuran model
    img = image.resize((224, 224))  # ubah jika ukuran input berbeda
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0).astype(np.float32)

    # Set input dan jalankan inferensi
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])[0]
    return predictions

# ======================
# Load Model
# ======================
MODEL_PATH = "leafnet_model.tflite"
interpreter = load_tflite_model(MODEL_PATH)

# ======================
# Upload Gambar
# ======================
uploaded_file = st.file_uploader("📸 Unggah gambar daun (format .jpg/.png)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_container_width=True)

    if st.button("🔍 Identifikasi"):
        with st.spinner("Sedang menganalisis gambar..."):
            preds = predict_tflite(interpreter, image)

            # Misalnya ada 20 kelas daun herbal
            classes = [
                "Daun Salam", "Daun Sambiloto", "Daun Kelor", "Daun Sirih", "Daun Pegagan",
                "Daun Katuk", "Daun Jambu Biji", "Daun Afrika", "Daun Insulin", "Daun Tempuyung",
                "Daun Mengkudu", "Daun Pandan", "Daun Serai", "Daun Kemangi", "Daun Lidah Buaya",
                "Daun Binahong", "Daun Beluntas", "Daun Pepaya", "Daun Pare", "Daun Mengkudu"
            ]

            pred_idx = np.argmax(preds)
            confidence = preds[pred_idx] * 100

            st.success(f"🌱 Jenis daun terdeteksi: **{classes[pred_idx]}** ({confidence:.2f}%)")

# ======================
# Footer
# ======================
st.markdown("---")
st.caption("© 2025 Sistem Klasifikasi Tanaman Herbal Antidiabetes | Dibangun dengan Streamlit")
