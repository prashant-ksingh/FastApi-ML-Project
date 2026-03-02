# Insurance Premium Prediction Clean API

A structured and modular FastAPI service for predicting insurance premium categories.

## 🚀 Features
- **Modular Architecture:** Separation of concerns (models, schemas, config).
- **Data Validation:** Uses Pydantic for strict input validation and normalization.
- **Detailed Responses:** Returns predicted category, confidence score, and class probabilities.
- **Health Checks:** Endpoint to verify API and model status.

## 🛠️ Project Structure
- `main.py`: API entry point and routing.
- `model/`: ML model logic and binary.
- `schema/`: Pydantic models for request/response.
- `config/`: Configuration (e.g., city tier mappings).

## 🚀 Getting Started

### 1. Setup
```powershell
# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the API
```powershell
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

### 3. API Endpoints
- `GET /`: Home message.
- `GET /health`: Check model status and version.
- `POST /predict`: Submit user data for insurance category prediction.

## 🧪 Example Request
```json
{
    "age": 30,
    "weight": 70.0,
    "height": 1.75,
    "income_lpa": 5.0,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
}
```
