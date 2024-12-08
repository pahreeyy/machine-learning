import streamlit as st
import joblib
import numpy as np

# Load model dan encoder
model = joblib.load('ML_AirQualityClassifier.pkl')
encoder = joblib.load('encoder.pkl')  # Pastikan encoder juga disimpan

st.title("Prediksi Polusi Udara")

# Input dari pengguna
temperature = st.number_input("Temperature", min_value=00.0, format="%.2f")
humidity = st.number_input("Humidity", min_value=00.0, format="%.2f")
pm25 = st.number_input("PM25", min_value=0.0, format="%.2f")
pm10 = st.number_input("PM10", min_value=00.0, format="%.2f")
no2 = st.number_input("NO2", min_value=00.0, format="%.2f")
so2 = st.number_input("SO2", min_value=0.0, format="%.2f")
co = st.number_input("CO", min_value=0.0, format="%.2f")
proximity_to_industrial_areas = st.number_input("Proximity To Industrial Areas", min_value=0.0, format="%.2f")
population_density = st.number_input("Population Density", min_value=0)

if st.button("Prediksi"):
    # Data input berbentuk array 2D
    data = np.array([[temperature, humidity, pm25, pm10, no2, so2, co, proximity_to_industrial_areas, population_density]])
    try:
        pred_label = model.predict(data)[0]
        pred_quality = encoder.inverse_transform([pred_label])[0]
        st.success(f"Air Quality: {pred_quality}")
    except Exception as e:
        st.error(f"Error: {e}")
