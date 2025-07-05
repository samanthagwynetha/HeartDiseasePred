# ❤️ Heart Disease Risk Predictor

A simple machine learning web app that predicts whether a patient is at risk of heart disease based on basic clinical information. Built for Dr. Mendoza’s community health clinic to assist nurses in making early medical decisions.

---

## 📋 Features

- Input patient health details like BMI, sleep hours, activity, and chronic conditions
- Predict if the patient is **at risk** or **not at risk** of heart disease
- View a **confidence score** to support early medical decisions
- User-friendly web interface using **Streamlit**

---

## 🧠 Model Info

- **Algorithm:** RandomForestClassifier
- **Preprocessing:** 
  - `OneHotEncoder` for categorical features
  - `StandardScaler` for numerical features
  - `SimpleImputer` for missing values
- **Training/Test Split:** 80/20 stratified
- **Exported Model:** `heart_disease_model.joblib`

---

## 📁 Dataset

We used the [Heart Disease UCI 2020 (uncleaned)](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease) dataset, which includes:

- Demographic info (age, sex, race)
- Lifestyle info (sleep, exercise, smoking, alcohol)
- Health metrics (BMI, physical/mental health days)
- Medical history (stroke, diabetes, asthma, etc.)

---

## 🚀 Live Demo

👉 https://heartdiseasepredic-rj2zabpjyhdmappartvcanq.streamlit.app/

---

## ⚠️ Disclaimer
This app is built for educational purposes only and not intended for real-world clinical use. For medical decisions, consult with a licensed healthcare professional.

