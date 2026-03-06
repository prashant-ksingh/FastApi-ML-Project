# 🛡️ Insurance Premium Prediction - Project Suite

This repository contains a complete end-to-end Machine Learning lifecycle, from model training to production-ready API deployment.

## 📂 Project Structure

The project is divided into three main components, intended to be used in the following order:

1.  **`fastapi_ml_model/`**: The Research & Development phase. Contains the dataset and Jupyter Notebook used to train the Random Forest model.
2.  **`fastapi_endpoint/`**: The Basic Deployment phase. A functional FastAPI service with an integrated Streamlit frontend for user interaction.
3.  **`Insurance_prediction-clean api/`**: The Production phase. A highly structured, modular, and scalable version of the API with advanced features like confidence scores and health checks.

---

## 🚀 Getting Started

### 1. Clone the Repository
```powershell
git clone https://github.com/prashant-ksingh/FastApi-ML-Project.git
cd FastApi-ML-Project
```

### 2. Step 1: Model Training (`fastapi_ml_model`)
Before running any API, you need to understand or generate the model.
- **Purpose:** Load raw data, perform feature engineering, and export the trained `model.pkl`.
- **Setup:**
  ```powershell
  cd fastapi_ml_model
  python -m venv venv
  .\venv\Scripts\Activate
  pip install -r requirements.txt
  ```
- **Execution:** Open `fastapi-ml-model.ipynb` in VS Code or Jupyter and run all cells to generate the model.

### 3. Step 2: Basic API & Frontend (`fastapi_endpoint`)
This project serves the model and provides a visual interface.
- **Purpose:** Quick deployment with a user-friendly Streamlit frontend.
- **Setup:**
  ```powershell
  cd ..\fastapi_endpoint
  python -m venv venv
  .\venv\Scripts\Activate
  pip install -r requirements.txt
  ```
- **Execution:**
  - **Start Backend:** `uvicorn main:app --reload`
  - **Start Frontend:** In a new terminal (with venv active), run `streamlit run frontend.py`

### 4. Step 3: Structured Production API (`Insurance_prediction-clean api`)
This is the most advanced version of the API.
- **Purpose:** Professional-grade API structure with separate folders for logic, schemas, and config.
- **Setup:**
  ```powershell
  cd "..\Insurance_prediction-clean api"
  python -m venv venv
  .\venv\Scripts\Activate
  pip install -r requirements.txt
  ```
- **Execution:** `uvicorn main:app --reload`
- **Features:** Visit `http://127.0.0.1:8000/docs` to see the automated Swagger documentation and test the advanced response model (which includes confidence scores).

---

## 🛠️ Summary of Dependencies

| Project | Key Technologies | Use Case |
| :--- | :--- | :--- |
| **ML Model** | Scikit-Learn, Pandas, Jupyter | Data Science & Training |
| **Endpoint** | FastAPI, Streamlit, Requests | Rapid Prototyping & UI |
| **Clean API** | FastAPI (Modular), Pydantic | Production-ready Service |

## 🔒 Security Note
All projects include a `.gitignore` to ensure that virtual environments (`venv/`) and local Python caches are not tracked by Git.
