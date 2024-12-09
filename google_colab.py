# -*- coding: utf-8 -*-
"""ini last.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MZrgsb3cxhc0hMneY5n_L92KXmiP3HbC
"""

# Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat Data Menjadi Dataframe
dataku = pd.read_csv('pollution.csv')

# Menampilkan 5 Baris Pertama Dari Dataframe
dataku.head()

dataku.info()

# Melakukan Import LabelEncoder dari Modul Sklearn
from sklearn.preprocessing import LabelEncoder

# Menyalin Dataframe Awal Supaya Tetap Utuh
dataku_int = dataku.copy()

# Membuat Object atau Instance dengan Nama Encoder
encoder = LabelEncoder()

# Membuat List Dari Nama kolom Data Kategori
categorical_data = ['Temperature', 'Humidity', 'PM25', 'PM10' ,'NO2', 'SO2', 'CO', 'Proximity_to_Industrial_Areas', 'Population_Density', 'Air Quality']

# Mengubah Setiap Kolom Kategori Menjadi Numerik
for kolom in categorical_data:
  dataku_int[kolom] = encoder.fit_transform(dataku[kolom])

# Berhasil!
dataku_int.head()

import joblib

joblib.dump(encoder, 'encoder.pkl')

for kolom in categorical_data:
  print(kolom, dataku_int[kolom].unique())

for kolom in categorical_data:
  print(kolom, dataku[kolom].unique())

# Menampilkan Matrix Kolerasi Antar Kolom
dataku_int.corr()

plt.figure(figsize=(10,8))
plt.title('Matriks Kolerasi Data')
sns.heatmap(dataku_int.corr(), annot=True, linewidths=3)
plt.show()

# Distribusi Data

def distribusi():
  fig,axes= plt.subplots(nrows=2, ncols=3, figsize=(12,8))
  plt.suptitle('Distribusi', fontsize=24)

  def kolom_generator():
    for kolom in dataku_int:
      yield kolom
  kolom = kolom_generator()

  for i in range(0, 2):
    for j in range(0, 3):
      k = next(kolom)
      dataku_int[k].plot(kind='hist', ax = axes[i, j])
      axes[i, j].set_title(k)

plt.show()
distribusi()

# Memisahkan Data

data = dataku_int.drop('Air Quality', axis=1)
label = dataku_int['Air Quality']

# Memisahkan Data untuk Latihan dan Tes
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2)

# Print untuk Mengetahui Bentuk Dataframe
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

# Mari Kita Gunakan linear SVC
# Import Linear SVC Model Dari Sklearn
from sklearn.svm import SVC

# Buat Objek dengan Nama Model dengan Memanggil SVC()
model = SVC(gamma='scale')

# Melatih model dengan data pelatihan (x_train dan y_train)
model.fit(x_train, y_train)

# Membuat prediksi dengan data uji (x_test)
prediction = model.predict(x_test)

# Import confusion matrix dari sklearn
from sklearn.metrics import confusion_matrix

# Membuat funsi untuk menampilkan confusion matrix dengan seaborn dan matplotlib
def display_conf(y_test,prediction):
    sns.heatmap(confusion_matrix(y_test,prediction),annot=True,linewidths=3,cbar=False)
    plt.title('Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Prediction')
    plt.show()

# Memanggil fungsi untuk menampilkan visualisasi confusion matrix
display_conf(y_test,prediction)

from sklearn.metrics import r2_score, classification_report

print(f'R2 Score : {r2_score(y_test,prediction)}')
print('Classification Report :')
print(classification_report(y_test, prediction, zero_division=0))

# Meningkatkan Model
# Menggunakan GridSearchCV untuk menemukan model dengan parameter terbaik

from sklearn.model_selection import GridSearchCV

# SVC Model Hyperparameter
param_grid = {'C':[0.01,0.1,1,10,100],
              'gamma':[100,10,1,0,1,0.01]}

# Membuat model terbaik dari semua kemungkinan kombinasi param_grid
best_model = GridSearchCV(SVC(),param_grid,cv=5,refit=True)

# Melatih model terbaik
best_model.fit(x_train,y_train)

# Model dengan parameter terbaik
best_model.best_estimator_

# Membuat prediksi dengan model yang telah ditingkatkan
prediction = best_model.predict(x_test)
# Menampilkan confusion matrix pada prediksi yang baru
display_conf(y_test,prediction)

print(f'R2 Score : {r2_score(y_test,prediction)}')
print('Classification Report :')
print(classification_report(y_test,prediction))

import pickle
# Menyimpan model menjadi file .pkl
with open('ML_AirQualityClassifier.pkl','wb') as file:
    pickle.dump(best_model,file)

# Memuat model dalam file .pkl
with open('ML_AirQualityClassifier.pkl','rb') as file:
    model = pickle.load(file)

# Model dengan parameter terbaik
best_model.best_estimator_

# Yuk, lakukan prediksi

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