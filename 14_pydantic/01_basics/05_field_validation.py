from pydantic import BaseModel, field_Validator, model_validator

class user(BaseModel):
    username: str

    @field_Validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters long")
        return v
    

class SignupData(BaseModel):
    password: str
    comfirm_password: str

    @model_validator(mode='after')
    def passwords_match(cls, values):
        if values.password != values.comfirm_password:
            raise ValueError("Passwords do not match")
        return values