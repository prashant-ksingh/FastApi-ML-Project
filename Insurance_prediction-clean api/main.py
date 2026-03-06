from fastapi import FastAPI, HTTPException
from model.predict import predict_output, model, MODEL_VERSION
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse


app = FastAPI()


# human readable
@app.get('/') 
def home():
    return {'message': 'Insurance Premium Prediction API'}   


# machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    # mapping input occupation to match model categories
    occupation_mapping = {
        'retired': 'retired',
        'freelancer': 'self_employed',
        'student': 'self_employed',
        'government_job': 'government_job',
        'buisness_owner': 'business',
        'unemployed': 'self_employed',
        'private_job': 'private_job'
    }

    # mapping lifestyle_risk to match model categories
    lifestyle_mapping = {
        'high': 'medium', # Model only knows ['low', 'medium']
        'medium': 'medium',
        'low': 'low'
    }

    # mapping age_group to match model categories
    age_mapping = {
        'young': 'adult', # Model only knows ['adult', 'middle_aged', 'senior']
        'adult': 'adult',
        'middle_aged': 'middle_aged',
        'senior': 'senior'
    }

    user_input = {
        'bmi' : data.bmi,
        'age_group' : age_mapping.get(data.age_group, 'adult'),
        'lifestyle_risk' : lifestyle_mapping.get(data.lifestyle_risk, 'low'),
        'city_tier' : data.city_tier if data.city_tier in [1, 2] else 2,
        'income_lpa' : data.income_lpa,
        'occupation' : occupation_mapping.get(data.occupation, 'private_job')
    }

    try:
        prediction = predict_output(user_input)
        return prediction
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# Improvements in Api
# 1- create a new folder
# 2- field calidator for city + occupation feature
# 3- Add route : Home -> Healthcheck
# 4- Add model Version
# 5- Sepration of logic
#     a- pydantic model 
#     b- City Tier
#     c- ML logic
# 6- try catch 
# 7- Add confidence score
# 8- Response Model


# In FastAPI a response model defines the structure of the data that your API endpoint will return. it helps in :
# 1- Genrating clean api docs (/docs)
# 2- validating output (so your API dosent't return malformed responses)
# 3- Filtering Unnecessary data from the response