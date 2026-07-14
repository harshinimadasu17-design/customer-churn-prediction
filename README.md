# Customer Churn Prediction Using Machine Learning

## Project Overview
This project predicts whether a telecom customer is likely to **churn (leave the service)** or **stay** using a Machine Learning model. It helps telecom companies identify customers who are at risk of leaving so they can take appropriate retention measures.

## Features
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Feature encoding using LabelEncoder
- Random Forest Classifier for prediction
- Model accuracy evaluation
- Streamlit web application for user interaction
- Predicts whether a customer is likely to churn or stay

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

## Dataset
- Dataset: IBM Telco Customer Churn Dataset
- Records:7043 customers
- Input Features:19
- Target Variable:Churn (Yes/No)

## Machine Learning Model
- Random Forest Classifier

## Model Performance
-Accuracy:79.55%

## Project Structure

customer-churn-prediction/
│── dataset/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── screenshots/
│   ├── homepage.png
│   ├── stay_prediction.png
│   └── churn_prediction.png
│
├── Customer_Churn_Prediction.py
├── app.py
├── churn_model.pkl
├── requirements.txt
└── README.md

## How to Run the Project

### 1. Clone the repository

git clone https://github.com/<your-github-username>/customer-churn-prediction.git

### 2. Navigate to the project folder

cd customer-churn-prediction

### 3. Install the required packages

pip install -r requirements.txt

### 4. Run the Streamlit application

streamlit run app.py

### 5. Open the application

Open your browser and visit:
http://localhost:8501

## Screenshots

### Home Page

<img width="1912" height="997" alt="Streamlit coverpage" src="https://github.com/user-attachments/assets/078b4f19-c28e-4f09-a34d-5400477b4171" />


### Prediction Result

<img width="1908" height="1013" alt="Streamlit stay" src="https://github.com/user-attachments/assets/86935973-7836-4878-82dc-29fdf53fbd9f" />
<img width="1918" height="1008" alt="streamlit Chrun" src="https://github.com/user-attachments/assets/7f8a88c6-68d2-4d85-bb86-a862ae8e4e36" />



## Future Enhancements
- Improve prediction accuracy using advanced algorithms such as XGBoost.
- Deploy the application to the cloud.
- Add prediction probability.
- Improve the user interface.
