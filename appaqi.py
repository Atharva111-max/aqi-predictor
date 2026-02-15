import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AQI Predictor", layout="wide")

st.title("🌍 AQI Predictor")

pm25 = st.slider("PM2.5", 0, 500, 100)
pm10 = st.slider("PM10", 0, 600, 150)
no2 = st.slider("NO2", 0, 300, 50)
so2 = st.slider("SO2", 0, 200, 20)

model = pickle.load(open("model.pkl", "rb"))

input_data = np.array([[pm25, pm10, no2, so2]])
prediction = model.predict(input_data)[0]

st.subheader("Predicted AQI")
st.success(round(prediction,2))

def get_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"

st.write("Category:", get_category(prediction))

fig, ax = plt.subplots()
ax.bar(["PM2.5","PM10","NO2","SO2"], [pm25,pm10,no2,so2])
st.pyplot(fig)
