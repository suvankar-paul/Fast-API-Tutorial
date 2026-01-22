from pydantic import BaseModel, Field
from typing import Dict, List, Optional , Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Full Name of the Patient", description="The patient's full name should not exceed 50 characters.", examples=["John Doe"])]
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="Indicates if the patient is married.")] 
    allergies: Optional[list[str]] = None
    contact_details: dict[str, str]

def insert_patient(patient1: Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.allergies)
    print("Inserting patient into the database")

patient_info = {'name': 'John Doe', 'age': 12, 'weight': 70.5, 'married': False, 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@example.com'}}
 
patient1 = Patient(**patient_info)

insert_patient(patient1)