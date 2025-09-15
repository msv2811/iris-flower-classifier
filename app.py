%%writefile app.py
import streamlit as st
import numpy as np
import requests
from PIL import Image
from io import BytesIO

# ML libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# -----------------------
# Train model on the fly
# -----------------------
iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Map numeric prediction to species name
species_map = {i: name for i, name in enumerate(iris.target_names)}

# -----------------------
# Streamlit UI
# -----------------------
st.title("🌸 Iris Flower Classifier (No .pkl needed!)")
st.write("Enter the measurements below and I'll predict the flower species!")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(features)[0]
species = species_map[prediction]

st.subheader(f"🌼 Predicted Species: {species.capitalize()}")

# -----------------------
# Fetch online image
# -----------------------
query = f"iris {species} flower"
ACCESS_KEY = st.secrets["UNSPLASH_KEY"]  # stored in Streamlit Cloud secrets

url = f"https://api.unsplash.com/photos/random?query={query}&client_id={ACCESS_KEY}&orientation=squarish"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    img_url = data['urls']['regular']
    img_response = requests.get(img_url)
    img = Image.open(BytesIO(img_response.content))
    st.image(img, caption=species.capitalize(), use_container_width=True)
else:
    st.write("⚠️ Could not fetch image right now.")
