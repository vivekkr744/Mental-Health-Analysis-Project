import streamlit as st
import joblib
import numpy as np
import pandas as pd


st.set_page_config(
   page_title="GreatMind",
   page_icon="👩🏻‍⚕️",
   layout="wide",
   initial_sidebar_state="expanded",
)

# Load trained model
model = joblib.load("model.pkl")

st.header("Hii There... 🙋‍♂️")
st.title(':red[Welc]:blue[ome to -]')
st.title("Smart Mental Health Analysis at Your Fingertips 🧠📊🔍")

# Define all input fields
age = st.number_input("Age", min_value=10, max_value=100, value=None, placeholder=' enter age')
gender = st.selectbox("Gender", ["Male", "Female", "Prefer not to say", "Non-binary"], index=None, placeholder="Choose any one")
employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed", "Self-employed", "Student"], index=None, placeholder="Choose any one")
work_environment = st.selectbox("Work Environment", ["On-site", "Remote", "Hybrid"], index=None, placeholder="Choose any one")
mental_health_history = st.selectbox("Mental Health History", ["Yes", "No"],index=None, placeholder="Choose any one")
seeks_treatment = st.selectbox("Seeks Treatment", ["Yes", "No"],index=None, placeholder="Choose any one")
stress_level = st.slider("Stress Level", 0, 15, 6)
sleep_hours = st.slider("Sleep Hours", 0, 15, 6)
physical_activity_days = st.number_input("Physical Activity Days", min_value=0, max_value=10, value=None, placeholder='Enter physical activity')
depression_score = st.slider("Depression Score", 0.0, 30.0, 15.0)
anxiety_score = st.slider("Anxiety Score", 0.0, 25.0, 10.56)
social_support_score = st.slider("Social Support Score", 0.0, 100.0, 50.0)
productivity_score = st.slider("Productivity Score", 0.0, 100.0, 77.0)

# Create input DataFrame

# Predict on button click
if st.button(label="Predict"):
    if None in (age, gender, employment_status, work_environment, mental_health_history, seeks_treatment,
                stress_level, sleep_hours, physical_activity_days, depression_score,
                anxiety_score, social_support_score, productivity_score):
        st.error("⚠ Please fill all fields before prediction.")
    else:
        input_data = pd.DataFrame([[
            age, gender, employment_status, work_environment, mental_health_history, seeks_treatment,
            stress_level, sleep_hours, physical_activity_days, depression_score,
            anxiety_score, social_support_score, productivity_score
        ]], columns=[
            'age', 'gender', 'employment_status', 'work_environment', 'mental_health_history', 'seeks_treatment',
            'stress_level', 'sleep_hours', 'physical_activity_days', 'depression_score',
            'anxiety_score', 'social_support_score', 'productivity_score'
        ])

        prediction = model.predict(input_data)
        
        st.success(f"✅🩺 Your Mental Health Status is : **{prediction[0]}**")
