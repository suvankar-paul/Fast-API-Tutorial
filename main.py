from fastapi import FastAPI , Path , HTTPException, Query
from pydantic import BaseModel, Field, computed_field
import json
from typing import Annotated, Literal, Optional
from fastapi.responses import JSONResponse


app = FastAPI()



class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property   
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= self.bmi < 24.9:
            return 'Normal weight'
        elif 25 <= self.bmi < 29.9:
            return 'Overweight'
        else:
            return 'Obesity'
        
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data,f)
        
@app.post('/create')
def create_patient(patient: Patient):
    # load existing patients from a JSON file
    data= load_data()

    #check if patient with same ID already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient with this ID already exists')

    #new patient, add to list
    data[patient.id] = patient.model_dump(exclude={'id'})

    #save updated list back to JSON file
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Patient created successfully', 'patient_id': patient.id})

