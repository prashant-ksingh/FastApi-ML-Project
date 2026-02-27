#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, accuracy_score
import numpy as np


# In[4]:


df = pd.read_csv("insurance_data.csv")
df.head()


# In[5]:


df_feat = df.copy()


# In[6]:


#Feature 1 : BMI
df_feat["bmi"] = df_feat["weight"]/ (df_feat["height"]**2)


# In[7]:


#Feature 2: Age Group
def age_group(age):
    if age < 25:
        return "young"
    elif age < 45:
        return "adult"
    elif age < 60:
        return "middle_aged"
    return "senior"



# In[8]:


df_feat["age_group"] = df_feat["age"].apply(age_group)


# In[9]:


#Feature 3 : Lifestyle Risk
def lifestyle_risk(row):
    if row["smoker"] and row["bmi"] > 30:
        return "high"
    elif row["smoker"] or row["bmi"] > 27:
        return "medium"
    else:
        return "low"


# In[10]:


df_feat["lifestyle_risk"] = df_feat.apply(lifestyle_risk, axis=1)


# In[11]:


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


# In[12]:


#Feature 4 : City Tier
def city_tier(city):
    if city in tier_1_cities:
        return 1
    elif city in tier_2_cities:
        return 2
    else:
        return 3


# In[13]:


df_feat["city_tier"] = df_feat["city"].apply(city_tier)


# In[14]:


df_feat.drop(columns=['age','weight','height','smoker','city'])[['income_lpa','occupation','bmi','age_group','lifestyle_risk','city_tier','insurance_premium_category']].head()


# In[15]:


# Select features and target 
x = df_feat[["bmi","age_group","lifestyle_risk","city_tier","income_lpa","occupation"]]
y = df_feat["insurance_premium_category"]


# In[16]:


# Default categorical and numeric feature
categorical_features = ["age_group","lifestyle_risk","occupation","city_tier"]
numeric_features = ["bmi", "income_lpa"]


# In[17]:


# Create column transformer for OHE
preprocessor = ColumnTransformer(
    transformers = [
        ("cat", OneHotEncoder(), categorical_features),
        ("num", "passthrough", numeric_features)
    ]
)


# In[18]:


# create a pipeline with preprocessing and random forest classifier
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])


# In[19]:


# Split data and train model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
pipeline.fit(x_train, y_train)


# In[20]:


# Predict and evaluate
y_pred = pipeline.predict(x_test)
accuracy_score(y_test, y_pred)


# In[21]:


x_test.head()


# In[ ]:


import pickle

# save the trained pipeline using pickle
pickle_model_path = "model.pkl"
with open(pickle_model_path, "wb") as f:
    pickle.dump(pipeline, f)

