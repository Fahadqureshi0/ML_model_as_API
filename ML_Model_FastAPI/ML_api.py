from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Create FastAPI app
app = FastAPI()

# Load the trained model
diabetes_model = pickle.load(open("diabetes_model.sav" , "rb"))

# Input schema
class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to Diabetes Prediction API"
    }


# Prediction Route
@app.post("/diabetes_prediction")
def diabetes_prediction(input_parameters: ModelInput):

    input_data = np.asarray([
        input_parameters.Pregnancies,
        input_parameters.Glucose,
        input_parameters.BloodPressure,
        input_parameters.SkinThickness,
        input_parameters.Insulin,
        input_parameters.BMI,
        input_parameters.DiabetesPedigreeFunction,
        input_parameters.Age
    ]).reshape(1, -1)

    prediction = diabetes_model.predict(input_data)

    if prediction[0] == 0:
        result = "The person is not diabetic."
    else:
        result = "The person is diabetic."

    return {
        "prediction": result
    }