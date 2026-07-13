import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("📱 Telecom Customer Churn Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (Months)", 0, 72)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet   service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"]) 
PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0)
TotalCharges = st.number_input("Total Charges", 0.0)

gender = 1 if gender == "Male" else 0
Partner = 1 if Partner == "Yes" else 0
Dependents = 1 if Dependents == "Yes" else 0
PhoneService = 1 if PhoneService == "Yes" else 0
MultipleLines = 1 if MultipleLines == "Yes" else 0
InternetService = 1 if InternetService == "DSL" else (2 if InternetService == "Fiber optic" else 0)
OnlineSecurity = 1 if OnlineSecurity == "Yes" else (2 if OnlineSecurity == "No internet service" else 0)
OnlineBackup = 1 if OnlineBackup == "Yes" else (2 if OnlineBackup == "No internet service" else 0)
DeviceProtection = 1 if DeviceProtection == "Yes" else (2 if DeviceProtection == "No internet service" else 0)
TechSupport = 1 if TechSupport == "Yes" else (2 if TechSupport == "No internet service" else 0)
StreamingTV = 1 if StreamingTV == "Yes" else (2 if StreamingTV == "No internet service" else 0)
StreamingMovies = 1 if StreamingMovies == "Yes" else (2 if StreamingMovies == "No internet service" else 0)
Contract = 1 if Contract == "One year" else (2 if Contract == "Two year" else 0)
PaperlessBilling = 1 if PaperlessBilling == "Yes" else 0
PaymentMethod = 1 if PaymentMethod == "Electronic check" else (2 if PaymentMethod == "Mailed check" else (3 if PaymentMethod == "Bank transfer (automatic)" else 4))
data = [[
    gender,
    SeniorCitizen,
    Partner,
    Dependents,
    tenure,
    PhoneService,
    MultipleLines,
    InternetService,
    OnlineSecurity,
    OnlineBackup,
    DeviceProtection,
    TechSupport,
    StreamingTV,
    StreamingMovies,
    Contract,
    PaperlessBilling,
    PaymentMethod,
    MonthlyCharges,
    TotalCharges
]]

if st.button("Predict"):
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")