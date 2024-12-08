import streamlit as st
import joblib
import numpy as np

# Load model dan encoder
model = joblib.load('ML_AirQualityClassifier.pkl')
encoder = joblib.load('encoder.pkl')

# Tambahkan Header
st.markdown(
    """
    <style>
    body {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #F39C12;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.8rem;
        color: #999999;
    }
    </style>
    <div class="title">Prediksi Polusi Udara</div>
    """,
    unsafe_allow_html=True,
)

#Input dari user
col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=00.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=00.0, step=0.1)
    pm25 = st.number_input("PM2.5", min_value=0.0, max_value=500.0, value=00.0, step=0.1)
    pm10 = st.number_input("PM10", min_value=0.0, max_value=500.0, value=00.0, step=0.1)

with col2:
    no2 = st.number_input("NO2", min_value=0.0, max_value=100.0, value=20.0, step=0.1)
    so2 = st.number_input("SO2", min_value=0.0, max_value=100.0, value=10.0, step=0.1)
    co = st.number_input("CO", min_value=0, max_value=50, value=1, step=1)
    proximity_to_industrial_areas = st.number_input("Proximity To Industrial Areas (km)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)

population_density = st.number_input("Population Density (people/km²)", min_value=0.0, value=100.0, step=1.0)

# Cek jika semua nilai 0
if all(value == 0 for value in [temperature, humidity, pm25, pm10, no2, so2, co, proximity_to_industrial_areas, population_density]):
    st.error("Error: Semua nilai tidak boleh 0. Silakan masukkan nilai yang valid!")
else:
    # Tombol Prediksi
    if st.button("Prediksi"):
        # Data input berbentuk array 2D
        data = np.array([[temperature, humidity, pm25, pm10, no2, so2, co, proximity_to_industrial_areas, population_density]])
        try:
            pred_label = model.predict(data)[0]
            pred_quality = encoder.inverse_transform([pred_label])[0]  # Perbaikan nama variabel
            st.success(f"Air Quality: {pred_quality}")
        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown(
    """
    <div class="footer">© 2024, Loyo Tapi Ayo | All Rights Reserved.</div>
    """,
    unsafe_allow_html=True,
)
