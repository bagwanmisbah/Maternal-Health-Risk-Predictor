# 🤰 Maternal Health Risk Predictor

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A machine learning project to predict maternal health risk levels during pregnancy using patient data. This project includes a Jupyter Notebook for model training and a Streamlit web app for interactive predictions.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Demo](#-demo)
- [License](#-license)

---

## 📖 Overview

This project addresses the critical issue of maternal health by providing a tool to predict potential health risks for expectant mothers. It uses the [Maternal Health Risk Dataset from UCI](https://archive.ics.uci.edu/dataset/863/maternal+health+risk) which contains biometric data such as age, blood pressure, and heart rate.

The core of the project is a **Random Forest Classifier** trained to categorize risk into three levels: **Low Risk**, **Mid Risk**, and **High Risk**.

---

## 📁 Project Structure
      
      Maternal-Health-Risk-Predictor/
      │
      ├── app.py # The Streamlit web application
      |
      ├── maternal_health_prediction.ipynb # Jupyter Notebook for data analysis and model training
      │
      ├── maternal_risk_model.joblib # Saved trained model
      |
      ├── scaler.joblib # Saved scaler object
      |
      ├── label_encoder.joblib # Saved label encoder object
      │
      ├── requirements.txt # Project dependencies
      |
      └── README.md # Project explanation

## ⚙️ Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   

         git clone (this repo link)
         cd Maternal-Health-Risk-Predictor

# For Windows

         python -m venv venv
         venv\Scripts\activate

# For macOS/Linux
      
      python3 -m venv venv
      source venv/bin/activate
      
Install the required dependencies:

    pip install -r requirements.txt

## Usage

There are two main components to this project:

1.Jupyter Notebook:
Explore the Maternal Health Risk Predictor.ipynb notebook to see the full workflow, including data exploration, preprocessing, model training, and evaluation.

### Distribution of Maternal Health Risk Levels

<img width="940" height="817" alt="image" src="https://github.com/user-attachments/assets/c4124686-8b48-43d4-9eea-b088f1117239" />



2. Streamlit Web App:
To launch the interactive prediction app, run the following command in your terminal:

      streamlit run app.py
      
Your web browser will open with the application running.

## Demo 


<img width="940" height="423" alt="image" src="https://github.com/user-attachments/assets/c92e478d-9f5d-4011-ab18-cdd1a837e8c8" />


<img width="940" height="428" alt="image" src="https://github.com/user-attachments/assets/fa9b680e-776e-447b-a8ac-5f645e198c58" />


<img width="940" height="429" alt="image" src="https://github.com/user-attachments/assets/9632ae91-31c2-4a5c-9199-583365bf259e" />



### Model Performance

The final Random Forest model achieved an overall accuracy of 86.21% on the test set.

### Classification Report and Confusion Matrix

<img width="940" height="904" alt="image" src="https://github.com/user-attachments/assets/5de5e8c1-e019-4f9f-8b41-1e35967ab42b" />

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
