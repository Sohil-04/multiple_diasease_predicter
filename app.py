import streamlit as st
import joblib
from streamlit_option_menu import option_menu

# loading the model
model_diabetes= joblib.load("model_diabetes.pkl")
model_heart = joblib.load("model_heart.pkl")

with st.sidebar:
    selected = option_menu("multiple disease prediction system",
                           ["diabetes prediction","heart disease prediction"],
                           default_index = 0)

# diabetes pridicton page
if (selected == "diabetes prediction"):
    # page title
    st.title("diabetes prediction using the given features")

    pregnancies = st.number_input("Number of Pregnancies", min_value=0)
    glucose = st.number_input("Glucose Level", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
    insulin = st.number_input("Insulin Level", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.2f")
    age = st.number_input("Age", min_value=0)
    
    if st.button("Predict Diabetes"):
        input_data = [[pregnancies, glucose, blood_pressure, skin_thickness,
                       insulin, bmi, dpf, age]]
        prediction = model_diabetes.predict(input_data)[0]
        if prediction == 1:
            st.success("The person is likely to have diabetes.")
        else:
            st.success("The person is likely healthy.")


if (selected == "heart disease prediction"):
    # page title
    st.title("heart disease prediction using the given features")

    # Example input fields (replace with all required features)
    age = st.number_input("Age", min_value=0)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    chol = st.number_input("Serum Cholesterol", min_value=0)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG results (0-2)", [0, 1, 2])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, format="%.2f")
    slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (0-3)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (1-3)", [1, 2, 3])
    
    if st.button("Predict Heart Disease"):
        sex_val = 1 if sex == "Male" else 0
        input_data = [[age, sex_val, cp, trestbps, chol, fbs, restecg,
                       thalach, exang, oldpeak, slope, ca, thal]]
        prediction = model_heart.predict(input_data)[0]
        if prediction == 1:
            st.success("The person is likely to have heart disease.")
        else:
            st.success("The person is likely healthy.")
