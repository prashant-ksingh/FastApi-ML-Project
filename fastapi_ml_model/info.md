
## Serving ML model using fast API

     model.pkl <----------> API<--------->Frontend

      ^                        ^                ^
      |                        |                |
      model               Fast Api     frontend (streamlit)
     Building


Step 1 - Building & Exporting the ml model

### based on the two tables (feature Engg):
 -> using the age we calculate d the age group

 -> using weight and height to make bmi in second table

 -> using BMI and Smoker field to create lifestyle_risk

 -> using city to create its city_tier

 -> rest income_pa and occupation are same


The second table is passed to ml models - 