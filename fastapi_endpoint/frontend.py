import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="Insurance Premium Predictor", page_icon="🛡️")

st.title("🛡️ Insurance Premium Category Prediction")
st.markdown("Enter your details below to predict your insurance premium category.")

# Form for user inputs
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=119, value=30, help="Age of the user (1-119)")
        weight = st.number_input("Weight (kg)", min_value=1.0, max_value=200.0, value=70.0, step=0.1, help="Weight of the user in kilograms")
        height = st.number_input("Height (m)", min_value=0.5, max_value=2.4, value=1.75, step=0.01, help="Height of the user in meters")
    
    with col2:
        income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, max_value=100.0, value=5.0, step=0.1, help="Annual Salary of the User in Lakhs Per Annum")
        smoker = st.selectbox("Smoker", options=[False, True], format_func=lambda x: "Yes" if x else "No")
        city = st.text_input("City", value="Mumbai", help="City of the user")

    occupation = st.selectbox(
        "Occupation", 
        options=['private_job', 'government_job', 'buisness_owner', 'freelancer', 'student', 'retired', 'unemployed'],
        help="Select your primary occupation"
    )

    submit_button = st.form_submit_button("Predict Premium Category")

if submit_button:
    # Prepare the payload
    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        with st.spinner("Calculating..."):
            response = requests.post(API_URL, json=payload)
            
        if response.status_code == 200:
            result = response.json()
            category = result.get("predicted_cotegory", "Unknown")
            
            # Display result with some styling
            st.success(f"### Predicted Category: **{category}**")
            
            # Additional UI feedback
            if category.lower() == "high":
                st.warning("Your profile suggests a high premium category.")
            elif category.lower() == "medium":
                st.info("Your profile suggests a medium premium category.")
            elif category.lower() == "low":
                st.balloons()
                st.info("Your profile suggests a low premium category.")
        else:
            st.error(f"Error: {response.status_code}")
            try:
                st.json(response.json())
            except:
                st.text(response.text)
            
    except Exception as e:
        st.error(f"Failed to connect to the API. Make sure the FastAPI server is running at {API_URL}")
        st.exception(e)

st.markdown("---")
st.caption("Note: This is a prediction based on a machine learning model.")
