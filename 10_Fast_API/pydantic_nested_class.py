from pydantic import BaseModel

class Address(BaseModel):

    city:str
    state:str
    Pin:str

class Patient(BaseModel):

    name : str
    age : int
    address: Address

add = {'city' : 'Gwalior' , 'state' : 'MP' , 'Pin' :'123421' }

ad = Address(**add)


pat = {'name': 'Kaka' , 'age':43 , 'address': ad}

patient = Patient(**pat)

print(patient)
print(patient.address.city)

# Organised 
# Reusability 
# Readability
# Validation    

# Converting Pydantic Object to Python Dictionary

temp = patient.model_dump()
print(temp)
print(type(temp))  # Dictionary