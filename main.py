import streamlit as st
import joblib
import numpy as np

# Load model dan encoder
model = joblib.load('ML_AirQualityClassifier.pkl')
encoder = joblib.load('encoder.pkl')  # Pastikan encoder juga disimpan

st.title("Prediksi Polusi Udara")

"""
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
"""

def self_prediction():
    try:
        # Input dari pengguna
        Temperature = float(input(''))
        Humidity = float(input(''))
        PM25 = float(input(''))
        PM10 = float(input(''))
        NO2 = float(input(''))
        SO2 = float(input(''))
        CO = float(input(''))
        Proximity_to_Industrial_Areas = float(input(''))
        Population_Density = int(input(''))

        # Data harus berbentuk array 2D
        data = [[Temperature, Humidity, PM25, PM10, NO2, SO2, CO, Proximity_to_Industrial_Areas, Population_Density]]

        # Prediksi dan hasil
        print('\nPrediction')
        pred_label = model.predict(data)[0]
        pred_quality = encoder.inverse_transform([pred_label])[0]
        print('Air Quality', pred_quality)

    except Exception as e:
        print('Error:', e)

# Memanggil fungsi
self_prediction()