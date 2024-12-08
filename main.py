import streamlit as st
import joblib
import numpy as np

# Load model dan encoder
model = joblib.load('ML_AirQualityClassifier.pkl')
encoder = joblib.load('encoder.pkl')  # Pastikan encoder juga disimpan

st.title("Prediksi Polusi Udara")

# Input dari pengguna
pm25 = st.number_input("PM25", min_value=0.0, format="%.2f")
pm10 = st.selectbox("PM10", min_value=00.0, format="%.3f")
no2 = st.selectbox("NO2", min_value=00.0, format="%.3f")
so2 = st.selectbox("SO2", min_value=0.0, format="%.2f")
co = st.number_input("CO", min_value=0.00, format="%.3f")

if st.button("Prediksi"):
    # Data input berbentuk array 2D
    data = np.array([[pm25, pm10, no2, so2, co]])
    try:
        pred_label = model.predict(data)[0]
        pred_drug = encoder.inverse_transform([pred_label])[0]
        st.success(f"Pasien mengonsumsi: {pred_quality}")
    except Exception as e:
        st.error(f"Error: {e}")
