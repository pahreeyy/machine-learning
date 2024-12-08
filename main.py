"""import streamlit as st
import joblib
import numpy as np

#Load model dan encoder
model = joblib.load('ML_AirQualityClassifier.pkl')
encoder = joblib.load('encoder.pkl')

st.title("Prediksi Konsumsi Obat")

#Input dari pengguna
"""

import streamlit as st
import joblib
import numpy as np

# Load model dan encoder
model = joblib.load('ML_AirQualityClassifier.pkl')
encoder = joblib.load('encoder.pkl')  # Pastikan encoder juga disimpan

st.title("Prediksi Konsumsi Obat")

# Input dari pengguna
age = st.number_input("Age", min_value=0, step=1, value=25)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
bp = st.selectbox("BP", options=[0, 1, 2], format_func=lambda x: ["Low", "Normal", "High"][x])
chol = st.selectbox("Cholesterol", options=[0, 1], format_func=lambda x: "Normal" if x == 0 else "High")
natoK = st.number_input("Na_to_K", min_value=0.0, format="%.2f")

if st.button("Prediksi"):
    # Data input berbentuk array 2D
    data = np.array([[age, sex, bp, chol, natoK]])
    try:
        pred_label = model.predict(data)[0]
        pred_drug = encoder.inverse_transform([pred_label])[0]
        st.success(f"Pasien mengonsumsi: {pred_drug}")
    except Exception as e:
        st.error(f"Error: {e}")

