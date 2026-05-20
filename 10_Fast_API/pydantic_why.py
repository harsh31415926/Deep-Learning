from pydantic import BaseModel, EmailStr , AnyUrl , Field , field_validator , computed_field
from typing import Dict, List , Optional,Annotated

# Basics
# class Patient(BaseModel):
#     name : str
#     age : int
#     email: EmailStr
#     linked_in: AnyUrl=None
#     allergy : Optional[List[str]] = None
#     contact : Dict[str , str]

class Patient(BaseModel):

    name : Annotated[str , Field(max_length = 50 , description = 'This tells the name of th user' , title = 'Name of the Patient' , examples = ['Aman', 'Harsh'])]

    age : Annotated[int , Field(gt = 0 , description = '')]

    email: Annotated[str , Field(title = 'Email' , description = 'Give the mail of the user')]

    height : Annotated[float , Field(gt = 1 , description = 'This is the height of the user' , title='height of the user')]

    weight : Annotated[int , Field(gt= 20 , description = 'Weight of the user ' , title= 'Height of the user')]


    # This will check whether the given mail is in the array or not

    @field_validator('email')
    @classmethod
    def email_validator(cls , value):

        valid_mail = ['hdfc.com' , 'icici.com']
        mail = value.split('@')[-1]

        if mail not in valid_mail:
            raise ValueError('Not a valid Domain')
        else : return value
    
    
    
    # This will convert the name in UpperCase

    @field_validator('name')
    @classmethod
    def capital_name(cls , value):
        return value.upper()
    

    

    # This will calculate bmi in real time 
    
    @computed_field
    @property
    def bmi(self)-> float:

        bmi = round(self.weight/(self.height**2),2)
        return bmi


def add_patient(p : Patient):

    print('Name -->' , p.name)
    print('Age -->',p.age)
    print('BMI -> ',p.bmi)
    print('Email -> ' , p.email)
    print('added successfully ')
    print(p.bmi)

p1_info = {'name' : 'Harsh' , 'age' : 22 , 'email' : 'harsh@hdfc.com', 'weight' :72 , 'height' : 1.71 }


p1 = Patient(**p1_info)

add_patient(p1)
