# FastAPI ML Prediction Service

A FastAPI-based web service that serves an ML model for predicting health insurance categories. This project includes logic for data preprocessing, input validation using Pydantic, and handles inconsistencies between raw user input and model training categories.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10 or higher
- `pip` (Python package manager)

### 2. Setup Instructions

1.  **Clone the Repository**
    ```powershell
    git clone <repository-url>
    cd fastapi_endpoint
    ```

2.  **Create and Activate Virtual Environment**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate
    ```

3.  **Install Dependencies**
    ```powershell
    pip install -r requirements.txt
    ```

4.  **Run the Server**
    ```powershell
    uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

---

## 🛠️ Project Files

### `main.py`
The core application file. It contains:
- **Pydantic Model (`UserInput`):** Validates incoming JSON data and computes derived fields like `bmi`, `age_group`, and `lifestyle_risk`.
- **Pre-processing Logic:** Includes mapping dictionaries to ensure user inputs match the specific categories the model was trained on (e.g., mapping "Goa" to Tier 2 or "young" to "adult").
- **Predict Endpoint:** The `/predict` POST endpoint that converts input data into a DataFrame and returns the model prediction.

---

## 🧪 Testing with PowerShell
If you don't want to use Python scripts, run this in your terminal:
```powershell
$body = @{
    age = 30
    weight = 70.0
    height = 1.75
    income_lpa = 5.0
    smoker = $false
    city = "Mumbai"
    occupation = "private_job"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/predict" -Method Post -Body $body -ContentType "application/json"
```

---

## 🎨 Frontend (Streamlit)

The project includes a user-friendly frontend built with **Streamlit**.

### How to Run the Frontend
1.  **Ensure the Backend is Running**:
    ```powershell
    uvicorn main:app --reload
    ```
2.  **Launch the Frontend**:
    ```powershell
    streamlit run frontend.py
    ```
    The application will open at `http://localhost:8501`.

### Features
-   **Interactive Form:** Enter details like age, height, weight, etc.
-   **Real-time Prediction:** Communicates with the FastAPI backend.
-   **Visual Feedback:** Displays results in categorized, color-coded boxes.

---

## 🔒 Git Best Practices
A `.gitignore` file is included to prevent pushing unnecessary files:
- **Venv:** Local environment files (`venv/`).
- **Models:** Binary files (`*.pkl`) should typically be managed via DVC or LFS, not direct Git commits.
- **Cache:** Python `__pycache__` folders.
