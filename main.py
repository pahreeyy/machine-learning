import streamlit as st
import joblib
import numpy as np

#Load model dan encoder
model = joblib.load('ML_AirQualityClassifier.pkl')
encoder = joblib.load('encoder.pkl')