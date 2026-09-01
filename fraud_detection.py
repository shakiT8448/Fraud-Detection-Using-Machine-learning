import streamlit
import pandas
import joblib
model = joblib.load("fraud_detection_pipeline.pkl")