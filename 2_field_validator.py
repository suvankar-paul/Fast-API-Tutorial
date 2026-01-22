from pydantic import BaseModel, Field , field_validator, EmailStr
from typing import Dict, List, Optional , Annotated

class Patient(BaseModel):
    name: str
    age: int 
    email : EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: dict[str, str]

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError('Not a valid email domain')
        return value
    
    @field_validator('name', mode = 'after')
    @classmethod
    def transform_name(cls, value):
        return value.upper()




def insert_patient(patient1: Patient):
    print(patient1.name)
    print(patient1.age)
    print(patient1.allergies)
    print(patient1.email)
    print("Inserting patient into the database")

patient_info = {'name': 'John Doe', 'age': 12, 'email': 'john.doe@hdfc.com', 'weight': 70.5, 'married': False, 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@example.com'}}
 
patient1 = Patient(**patient_info)

insert_patient(patient1)