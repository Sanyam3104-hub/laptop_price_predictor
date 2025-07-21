import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("Laptop Price Predictor")

# Collect input from user
company = st.selectbox('Brand', ['Dell', 'Apple', 'HP', 'Lenovo', 'Asus', 'Acer', 'MSI', 'Other'])
type = st.selectbox('Type', ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible', 'Workstation', 'Netbook'])
ram = st.selectbox('RAM (in GB)', [4, 8, 16, 32, 64])
weight = st.number_input('Weight of the Laptop')
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.selectbox('IPS Display', ['No', 'Yes'])
ppi = st.number_input('PPI (Pixels Per Inch)', step=1.0)
cpu = st.selectbox('CPU Brand', ['Intel Core i5', 'Intel Core i7', 'Intel Core i3', 'AMD Ryzen', 'Other'])
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 128, 256, 512, 1024])
gpu = st.selectbox('GPU Brand', ['Nvidia', 'AMD', 'Intel'])
os = st.selectbox('Operating System', ['Windows', 'Mac', 'Linux', 'Others'])

# Button to trigger prediction
if st.button('Predict Price'):

    # Convert 'Yes'/'No' to binary 1/0
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Create DataFrame with correct columns
    query_df = pd.DataFrame([[
        company, type, ram, weight, touchscreen, ips, ppi,
        cpu, hdd, ssd, gpu, os
    ]], columns=[
        'Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen',
        'Ips', 'ppi', 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'
    ])

    # Predict and show result
    try:
        predicted_price = int(np.exp(pipe.predict(query_df)[0]))
        st.success(f"Estimated Laptop Price: ₹ {predicted_price}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
