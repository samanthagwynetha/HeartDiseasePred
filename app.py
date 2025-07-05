import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('heart_disease_model.joblib')

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")
st.title("❤️ Heart Disease Risk Predictor")
st.write("Enter patient information below to check heart disease risk.")

# Input form
with st.form("risk_form"):
    bmi = st.number_input("BMI (Body Mass Index)", 10.0, 60.0, step=0.1)
    physical_health = st.slider("Physical Health (Bad Days in past 30)", 0, 30)
    mental_health = st.slider("Mental Health (Bad Days in past 30)", 0, 30)
    sleep_time = st.slider("Average Sleep Hours per Day", 0, 24)

    smoking = st.selectbox("Does the patient smoke?", ["Yes", "No"])
    alcohol = st.selectbox("Does the patient drink alcohol?", ["Yes", "No"])
    stroke = st.selectbox("Has the patient had a stroke?", ["Yes", "No"])
    diff_walking = st.selectbox("Difficulty walking?", ["Yes", "No"])
    sex = st.selectbox("Sex", ["Male", "Female"])
    age = st.selectbox("Age Category", [
        "18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59",
        "60-64", "65-69", "70-74", "75-79", "80 or older"
    ])
    race = st.selectbox("Race", [
        "White", "Black", "Asian", "American Indian/Alaskan Native", "Other", "Hispanic"
    ])
    diabetic = st.selectbox("Is the patient diabetic?", ["No", "Yes"])
    physical_activity = st.selectbox("Does the patient do physical activity?", ["Yes", "No"])
    gen_health = st.selectbox("General Health", ["Poor", "Fair", "Good", "Very good", "Excellent"])
    asthma = st.selectbox("Asthma?", ["Yes", "No"])
    kidney_disease = st.selectbox("Kidney Disease?", ["Yes", "No"])
    skin_cancer = st.selectbox("Skin Cancer?", ["Yes", "No"])

    submitted = st.form_submit_button("Predict")

# Predict when submitted
if submitted:
    total_bad_days = physical_health + mental_health

    input_df = pd.DataFrame({
        'BMI': [bmi],
        'PhysicalHealth': [physical_health],
        'MentalHealth': [mental_health],
        'SleepTime': [sleep_time],
        'Smoking': [smoking],
        'AlcoholDrinking': [alcohol],
        'Stroke': [stroke],
        'DiffWalking': [diff_walking],
        'Sex': [sex],
        'AgeCategory': [age],
        'Race': [race],
        'Diabetic': [diabetic],
        'PhysicalActivity': [physical_activity],
        'GenHealth': [gen_health],
        'Asthma': [asthma],
        'KidneyDisease': [kidney_disease],
        'SkinCancer': [skin_cancer],
        'TotalBadDays': [total_bad_days]
    })

    prediction = model.predict(input_df)[0]
    confidence = model.predict_proba(input_df)[0][1]  # probability of class 1

    if prediction == 1:
        st.error(f"⚠️ Patient is **at risk** of heart disease.")
    else:
        st.success(f"✅ Patient is **not at risk** of heart disease.")

    st.info(f"🔍 Confidence Score: {confidence:.2%}")
