from fastapi import FastAPI
import json
from fastapi.params import Path
from fastapi.exceptions import HTTPException
from fastapi.params import Query

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data
    


@app.get("/")
def read_root():
    return {"Welcome to doctor app."}


@app.get("/about")
def read_about():
    return {"A fully functional doctor appointment scheduling API built with FastAPI."}

@app.get("/view")
def view_patients():
    data = load_data()
    return data


@app.get("/view/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    data= load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(sort_by: str = Query(...,description="Field is sorting by weight,height or bmi" ), order_by: str = Query('asc',description="Order is sorting by ascending or descending")):
    valid_sort_fields = ['weight', 'height', 'bmi']
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by field. Must be one of {valid_sort_fields}")
    if order_by not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order_by value. Must be 'asc' or 'desc'")
    
    data = load_data()
    sort_order = False if order_by == 'asc' else True
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data
    

