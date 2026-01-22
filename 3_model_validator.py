from pydantic import BaseModel, Field , model_validator
from typing import Dict, List, Optional , Annotated

class Patient(BaseModel):
    name: str
    age: int 
    weight: float
    married: bool
    allergies: Optional[List[str]] = Field(default=None)
    contact_details: dict[str, str]


    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency_contact' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60 years old.")
        return model

def insert_patient(patient1: Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.allergies)
    print("Inserting patient into the database")

patient_info = {'name': 'John Doe', 'age': 59, 'weight': 70.5, 'married': False, 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@example.com'}}
 
patient1 = Patient(**patient_info)

insert_patient(patient1)