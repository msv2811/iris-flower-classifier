import streamlit as st
import joblib
import numpy as np
import requests
from PIL import Image
from io import BytesIO

# Load trained model
model = joblib.load("iris_model.pkl")

st.title("🌸 Iris Flower Classifier (with Live Images)")
st.write("Enter the measurements below and I'll predict the flower species!")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# Make prediction
features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(features)[0]

# Map numeric prediction to species name
species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
predicted_species = species_map[int(prediction)]

# Show prediction
st.subheader(f"🌼 Predicted Species: {predicted_species.capitalize()}")

# Fetch online image (Unsplash API)
query = f"iris {predicted_species} flower"
ACCESS_KEY = st.secrets["UNSPLASH_KEY"]  # Replace with your real Unsplash API key

url = f"https://api.unsplash.com/photos/random?query={query}&client_id={ACCESS_KEY}&orientation=squarish"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    img_url = data['urls']['regular']
    img_response = requests.get(img_url)
    img = Image.open(BytesIO(img_response.content))
    st.image(img, caption=predicted_species.capitalize(), use_column_width=True)
else:
    st.write("⚠️ Could not fetch image right now.")
