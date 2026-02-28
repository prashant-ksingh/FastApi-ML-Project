import requests

data = {
    "age": 30,
    "weight": 70.0,
    "height": 1.75,
    "income_lpa": 5.0,
    "smoker": False,
    "city": "Mumbai",
    "occupation": "private_job"
}

try:
    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
