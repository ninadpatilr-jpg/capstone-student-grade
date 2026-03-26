"""
This FastAPI script serves as the primary entry point for a student performance prediction application. 
It functions by defining the necessary API endpoints that bridge the gap between user input and the underlying machine learning model. 
The application provides a simple GET endpoint to verify that the server is active and a POST endpoint `/predict` specifically designed to process student feature data and return real-time performance predictions.

Mr. Savio Saldanha shared this code during Office Hours for the UC Berkeley AI & ML Certification Course, on February 16, 2026.
On March 24, 2026 Mr. Ninad Patil modified it to for his capstone project Student Performance Factor.

Please ensure you have fastapi; otherwise run `%pip install fastapi` to resolve depndencies.

To run this FastAPI application, execute:
uvicorn main:app --reload

"""

from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

model = joblib.load("./ridge_spf_20260324_185422UTC.pkl")

class independentFeatures(BaseModel):
    attendance: int
    hours_studied: int
    access_to_resources: str
    previous_scores: int
    parental_involvement: str
    tutoring_sessions: int
    parental_education_level: str
    physical_activity: int
    peer_influence: str
    sleep_hours: int
    motivation_level: str
    internet_access: str
    family_income: str
    teacher_quality: str
    school_type: str
    learning_disabilities: str
    distance_from_home: str
    gender: str
    extracurricular_activities: str
 
app = FastAPI()

@app.get("/")
def hello():
    print("Hello from Student Performance Factor Portal")
    return "Hello from Student Performance Factor Portal"

@app.post("/predict")
def diabetes_prediction(variables: independentFeatures):
    print(variables.model_dump())
    data = pd.DataFrame(variables.model_dump(), index=[0])
    prediction = model.predict(data)
    print("predictions: ",prediction.item(), type(prediction.item()))

    return {"prediction": prediction.item()}
