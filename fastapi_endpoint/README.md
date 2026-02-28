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

### `check_model.py` (Diagnostic Tool)
This utility script was created to inspect the pickled ML model.
- **Why use it?** If the API returns a 500 error related to `ValueError: Found unknown categories`, it means the model is receiving a value it wasn't trained on.
- **How to use it:**
    ```powershell
    python check_model.py
    ```
- **Output:** It prints the model type, feature names, and the exact categories expected for every column (e.g., `city_tier` categories `[1, 2]`).

### `test_predict.py` (Testing Script)
A helper script to quickly verify the endpoint.
- **How to use it:**
    ```powershell
    python test_predict.py
    ```
- **Requirement:** This script requires the `requests` library (`pip install requests`). Alternatively, you can use the built-in FastAPI docs at `/docs` or the PowerShell command provided below.

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

## 🔒 Git Best Practices
A `.gitignore` file is included to prevent pushing unnecessary files:
- **Venv:** Local environment files (`venv/`).
- **Models:** Binary files (`*.pkl`) should typically be managed via DVC or LFS, not direct Git commits.
- **Cache:** Python `__pycache__` folders.
