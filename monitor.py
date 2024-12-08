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