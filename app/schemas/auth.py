from pydantic import BaseModel,field_validator,Field,EmailStr
class SignUp(BaseModel):
    full_name:str=Field(max_length=30)
    email:EmailStr
    age:int=Field(gt=18,ls=100)
    password:str=Field(min_length=8)

    @field_validator('full_name')
    @classmethod
    def name_validator(cls,value):
        for char in value:
            if char>="0" and char<="9":
                raise ValueError("name must not contains numbers ")
        return value.strip()
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        return value.lower()
    
    @field_validator('password')
    @classmethod
    def password_validator(cls,value):
        invalid_password=["password","12345678"]
        if value.lower() in invalid_password:
            raise ValueError(" Password is too common")
        return value

class Login(BaseModel):
    email:str
    password:str=Field(min_length=8)
