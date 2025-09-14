# 🌸 Iris Flower Classifier Web App

This is a Streamlit-based web application that predicts the species of an Iris flower 
based on its features (sepal length, sepal width, petal length, petal width).  
The model is trained using the famous Iris dataset (3 classes: Setosa, Versicolor, Virginica).

-----------------------------------------
✨ Features
-----------------------------------------
- 🎚️ Interactive sliders to input flower measurements  
- 🤖 Machine learning model to predict species  
- 🖼️ Displays an image of the predicted flower species  
- 🎨 Simple and user-friendly interface using Streamlit  

-----------------------------------------
📂 Project Structure
-----------------------------------------
iris_classifier_project/  
│── app.py                # 🚀 Streamlit app  
│── iris_model.pkl        # 💾 Trained ML model  
│── Iris_Prediction.ipynb # 📒 Jupyter notebook (training + EDA)  
│── requirements.txt      # 📦 Python dependencies  
│── README.md             # 📘 Documentation  
│── .gitignore            # 🙈 Ignore unnecessary files  

-----------------------------------------
⚙️ Installation & Setup
-----------------------------------------
1️⃣ Clone the repository  
   git clone https://github.com/your-username/iris_classifier_project.git  
   cd iris_classifier_project  

2️⃣ Create a virtual environment (recommended)  
   python -m venv venv  
   source venv/bin/activate   # For Linux/Mac  
   venv\Scripts\activate      # For Windows  

3️⃣ Install dependencies  
   pip install -r requirements.txt  

4️⃣ Run the Streamlit app  
   streamlit run app.py  

5️⃣ Open the link shown in terminal (usually 👉 http://localhost:8501/) in your browser  

-----------------------------------------
📊 Dataset
-----------------------------------------
The app uses the **Iris dataset** from scikit-learn, which contains:  
- 🌿 Sepal length  
- 🌿 Sepal width  
- 🌸 Petal length  
- 🌸 Petal width  
- 🏷️ Target species (Setosa, Versicolor, Virginica)  

-----------------------------------------
🙏 Acknowledgements
-----------------------------------------
- ⚡ Scikit-learn  
- 🌐 Streamlit  
- 📖 Iris Dataset (Fisher, 1936)  
