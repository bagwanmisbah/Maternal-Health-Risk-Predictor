import streamlit as st
import joblib
import numpy as np

try:
    model = joblib.load('maternal_risk_model.joblib')
    scaler = joblib.load('scaler.joblib')
    label_encoder = joblib.load('label_encoder.joblib')
except FileNotFoundError:
    st.error("Model files not found. Please ensure 'maternal_risk_model.joblib', 'scaler.joblib', and 'label_encoder.joblib' are in the same directory.")
    st.stop()


st.set_page_config(page_title="Maternal Health Risk Predictor", page_icon="🤰")


st.title("🤰 Maternal Health Risk Predictor")
st.write("""
Enter the patient's data to predict the maternal health risk level.
This app uses a Random Forest model to classify the risk as Low, Mid, or High.
""")

st.sidebar.header("Patient Input Features")


def user_input_features():
    age = st.sidebar.number_input("Age (years)", 10, 70, 25)
    systolic_bp = st.sidebar.slider("Systolic Blood Pressure (mmHg)", 70, 180, 120)
    diastolic_bp = st.sidebar.slider("Diastolic Blood Pressure (mmHg)", 40, 120, 80)
    bs = st.sidebar.slider("Blood Sugar (mmol/L)", 6.0, 19.0, 7.0, 0.1)
    body_temp = st.sidebar.slider("Body Temperature (°F)", 96.0, 104.0, 98.6, 0.1)
    heart_rate = st.sidebar.slider("Heart Rate (bpm)", 60, 100, 75)

    data = {
        'Age': age,
        'SystolicBP': systolic_bp,
        'DiastolicBP': diastolic_bp,
        'BS': bs,
        'BodyTemp': body_temp,
        'HeartRate': heart_rate
    }
    features = np.array(list(data.values())).reshape(1, -1)
    return features

input_data = user_input_features()

st.subheader("Patient Data Input:")
st.write(f"- **Age:** {input_data[0, 0]} years")
st.write(f"- **Blood Pressure:** {input_data[0, 1]}/{input_data[0, 2]} mmHg")
st.write(f"- **Blood Sugar:** {input_data[0, 3]} mmol/L")
st.write(f"- **Body Temperature:** {input_data[0, 4]} °F")
st.write(f"- **Heart Rate:** {input_data[0, 5]} bpm")


if st.button("Predict Risk Level"):
    input_data_scaled = scaler.transform(input_data)

    prediction_numeric = model.predict(input_data_scaled)
    prediction_proba = model.predict_proba(input_data_scaled)

    prediction_text = label_encoder.inverse_transform(prediction_numeric)[0]

    st.subheader("Prediction Result")

    if prediction_text == 'low risk':
        st.success(f"Predicted Risk Level: Low Risk")
    elif prediction_text == 'mid risk':
        st.warning(f"Predicted Risk Level: Mid Risk")
    else:
        st.error(f"Predicted Risk Level: High Risk")

    st.write("Prediction Confidence:")
    st.write(f"- **Low Risk:** {prediction_proba[0][1]*100:.2f}%")
    st.write(f"- **Mid Risk:** {prediction_proba[0][2]*100:.2f}%")
    st.write(f"- **High Risk:** {prediction_proba[0][0]*100:.2f}%")