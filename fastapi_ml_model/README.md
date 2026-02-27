# Insurance Premium Prediction Model

This project contains a Machine Learning model to predict insurance premium categories based on various health and demographic features.

## Setup and Installation

Follow these steps to set up the project on your local machine:

### 1. Navigate to the Project Directory
Open your terminal or command prompt and go to the project folder:
```bash
cd D:\fastapi_additional
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to keep dependencies isolated:
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- **On Windows:**
  ```bash
  .\venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
Install the required Python libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Dataset

The model uses `insurance_data.csv`, which includes columns like `age`, `weight`, `height`, `income_lpa`, `smoker`, `city`, and `occupation`.

## Model Workflow: Step-by-Step Explanation

### 1. Data Loading and Preparation
The process begins by importing necessary libraries (Pandas for data handling, Scikit-Learn for ML) and loading the raw dataset from a CSV file into a DataFrame.
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

df = pd.read_csv("insurance_data.csv")
```

### 2. Feature Engineering
Raw data is transformed into more meaningful indicators for the model:
- **BMI Calculation:** Calculated using the formula `weight / (height^2)`.
  ```python
  df_feat["bmi"] = df_feat["weight"] / (df_feat["height"]**2)
  ```
- **Age Grouping:** Categorizes ages into labels like 'young', 'adult', 'middle_aged', and 'senior' to capture life-stage risks.
- **Lifestyle Risk Assessment:** Combines `smoker` status and `BMI` to determine if a person has a 'high', 'medium', or 'low' health risk.
  ```python
  def lifestyle_risk(row):
      if row["smoker"] and row["bmi"] > 30:
          return "high"
      elif row["smoker"] or row["bmi"] > 27:
          return "medium"
      else:
          return "low"

  df_feat["lifestyle_risk"] = df_feat.apply(lifestyle_risk, axis=1)
  ```
- **City Categorization:** Maps cities to 'Tier 1' or 'Tier 2' based on their economic profile, which influences insurance costs.

### 3. Data Preprocessing
Before training, the data is cleaned and formatted:
- **Feature Selection:** Only the engineered features and relevant raw data (like income and occupation) are kept.
- **One-Hot Encoding:** Categorical variables (like occupation and age group) are converted into a numerical format that the ML algorithm can understand.
- **Column Transformation:** A preprocessor is built to apply different transformations to numerical and categorical columns simultaneously.
  ```python
  categorical_features = ["age_group","lifestyle_risk","occupation","city_tier"]
  numeric_features = ["bmi", "income_lpa"]

  preprocessor = ColumnTransformer(
      transformers = [
          ("cat", OneHotEncoder(), categorical_features),
          ("num", "passthrough", numeric_features)
      ]
  )
  ```

### 4. Model Building (The Pipeline)
A **Scikit-Learn Pipeline** is created to bundle the preprocessing steps and the model together. This ensures that any data fed into the model (during training or later in production) undergoes the exact same transformations. The model used is a **Random Forest Classifier**, which is excellent for handling complex relationships in data.
```python
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])
```

### 5. Training and Evaluation
- **Data Splitting:** The data is split into a **Training Set** (80%) to teach the model and a **Test Set** (20%) to evaluate its performance.
- **Model Training:** The model "learns" the patterns between the features and the target `insurance_premium_category`.
- **Accuracy Check:** The model's predictions are compared against actual values in the test set to determine its accuracy.
  ```python
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
  pipeline.fit(x_train, y_train)

  y_pred = pipeline.predict(x_test)
  ```

### 6. Model Export
The final trained pipeline (including the preprocessor and the classifier) is saved as **`model.pkl`** using the `pickle` library. This file can be loaded later into a web API (like FastAPI) to make real-time predictions without retraining.
```python
import pickle
with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)
```

## Usage

1. **Run via Jupyter Notebook:**
   Open `fastapi-ml-model.ipynb` in VS Code or Jupyter and run all cells.
   
2. **Run via Python Script:**
   If you have the converted script, you can run it directly:
   ```bash
   python fastapi-ml-model.py
   ```

The resulting `model.pkl` will be generated in the root directory.
