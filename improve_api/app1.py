from fastapi import FastAPI
from fastapi.responses import JSONResponse
from improve_api.schema.user_input import UserInput  
from typing import Literal, Annotated
import pickle
import pandas as pd
from improve_api.model.predict import model, MODEL_VERSION, predict_output
from improve_api.schema.prediction_response import PredictionResponse


app = FastAPI()

#human readble API endpoints       
@app.get('/')
def home():
    return {'message': 'Welcome to the Insurance Premium Prediction API'}


# machine readable endpoint
@app.get('/health')
def health_check():
    return {'status': 'API is healthy',
            'model_version': MODEL_VERSION}

@app.post('/predict', response_model= PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})




