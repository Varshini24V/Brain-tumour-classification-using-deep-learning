import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('best_model.h5')

class_names = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

st.title("Brain Tumor Classification")

uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # ✅ Load original image for display
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption="Uploaded Image", width=300)

    # ✅ Create a COPY for preprocessing
    img_resized = img.resize((224, 224))

    # Convert to array
    img_array = np.array(img_resized)

    # ✅ Normalize ONLY once
    img_array = img_array.astype(np.float32) / 255.0

    # Expand dims
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    pred = model.predict(img_array, verbose=0)
    class_idx = np.argmax(pred)
    confidence = float(np.max(pred))

    # Output
    st.subheader(f"Prediction: {class_names[class_idx]}")
    st.write(f"Confidence: {confidence*100:.4f}%")