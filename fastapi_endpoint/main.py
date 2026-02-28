from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd


# import the ml model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

tier_1_cities = [
    "Delhi", "Mumbai", "Bangalore", "Hyderabad",
    "Chennai", "Kolkata", "Pune", "Ahmedabad"
]

tier_2_cities = [
    "Jaipur", "Lucknow", "Chandigarh", "Indore",
    "Bhopal", "Surat", "Vadodara", "Coimbatore",
    "Kochi", "Patna", "Nagpur", "Visakhapatnam",
    "Guwahati", "Bhubaneswar"
]

# pydantic model to validate in coming data
class UserInput(BaseModel):

    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user")]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description="Height of the user")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Annual Salary of the User in LPA")]
    smoker: Annotated[bool, Field(..., description="Is smoker")]
    city: Annotated[str, Field(..., description="City of the user")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job', 'buisness_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the user")]

    @computed_field
    @property
    def bmi(self)-> float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi > 30:
            return "heigh"
        elif self.smoker and self.bmi >27:
            return "medium"
        else: 
            return "low"
        

    @computed_field
    @property
    def age_group(self)-> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        else:
            # Model only supports [1, 2]. Defaulting anything else to 2.
            return 2
        



@app.post('/predict')
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
        'heigh': 'medium', # Model only knows ['low', 'medium']
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

    input_df = pd.DataFrame([{
        'bmi' : data.bmi,
        'age_group' : age_mapping.get(data.age_group, 'adult'),
        'lifestyle_risk' : lifestyle_mapping.get(data.lifestyle_risk, 'low'),
        'city_tier' : data.city_tier,
        'income_lpa' : data.income_lpa,
        'income_lap' : data.income_lpa, # Keeping both as requested
        'occupation' : occupation_mapping.get(data.occupation, 'private_job')
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code = 200, content= {'predicted_cotegory' : prediction})


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