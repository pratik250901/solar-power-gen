import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("deploy.pkl", "rb"))

st.title("☀️ Solar Power Prediction App")
st.sidebar.header("Enter Input Features")

# Only the 2 features your model was trained on:
dist_to_solar_noon = st.sidebar.number_input("Distance to Solar Noon")
humidity = st.sidebar.number_input("Humidity (%)")

input_df = pd.DataFrame({
    'distance-to-solar-noon': [dist_to_solar_noon],
    'humidity': [humidity]
})

if st.sidebar.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Solar Power Output: ⚡ {prediction[0]:.2f} kW")
