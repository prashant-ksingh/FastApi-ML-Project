# 🎨 Insurance Premium Predictor - Frontend Documentation

This document provides a detailed explanation of the Streamlit-based frontend for the Insurance Premium Category Prediction service.

## 📋 Overview
The frontend is built with **Streamlit**, a powerful Python framework for creating data applications. it provides an intuitive, form-based interface that allows users to input their profile details and receive real-time insurance premium category predictions from the FastAPI backend.

## 🚀 How to Run
1.  **Ensure the Backend is Running**:
    The frontend relies on the FastAPI server. Open a separate terminal and run:
    ```powershell
    uvicorn main:app --reload
    ```
2.  **Install Streamlit**:
    If you haven't installed it yet:
    ```powershell
    pip install streamlit requests
    ```
3.  **Launch the Frontend**:
    ```powershell
    streamlit run frontend.py
    ```
    The application will automatically open in your default web browser at `http://localhost:8501`.

## 🛠️ Features & Implementation Details

### 1. User Input Form (`st.form`)
To ensure a smooth user experience, all inputs are wrapped in a `st.form`. This prevents the app from rerunning/refreshing the API call every time a single field is changed, only triggering the prediction when the "Predict" button is clicked.

### 2. Input Widgets
-   **Numerical Inputs**: `age`, `weight`, `height`, and `income_lpa` use `st.number_input` with specific `min_value`, `max_value`, and `step` increments to ensure data integrity before it reaches the API.
-   **Categorical Inputs**:
    -   **Smoker**: A `st.selectbox` that maps "Yes/No" labels to Boolean `True/False`.
    -   **Occupation**: A dropdown menu containing the occupations the model was trained on.
-   **Text Input**: `city` allows users to type their city name, which the backend then maps to the appropriate `city_tier`.

### 3. Dynamic UI Feedback
The app provides visual cues based on the API response:
-   **Spinner**: A `st.spinner` indicates the "Calculating..." state while waiting for the backend.
-   **Success/Warning/Info Boxes**: The result is displayed in colored boxes based on the category:
    -   🟢 **Low**: Displays balloons and a success message.
    -   🔵 **Medium**: Displays an info message.
    -   🟡 **High**: Displays a warning message.

### 4. API Communication
The frontend uses the `requests` library to send a `POST` request to `http://localhost:8000/predict`. It includes:
-   **Payload Construction**: Automatically maps form variables to the JSON structure expected by the FastAPI `UserInput` Pydantic model.
-   **Error Handling**: Catches connection errors (e.g., if the backend is down) and displays a user-friendly error message instead of crashing.

## 🔧 Configuration
The `API_URL` variable at the top of `frontend.py` defines where the frontend looks for the backend. If you deploy the backend to a cloud service, you only need to update this single string.
