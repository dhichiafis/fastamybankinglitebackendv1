from pydantic import BaseModel


class UserCreate(BaseModel):
    username:str 
    password:str 
    role:str 
    
    
class UserBase(UserCreate):
    id:int 
    class Config:
        orm_mode=True


class ProfileCreate(BaseModel):
    user_id:int 
    email:str  
    firstname:str 
    lastname:str 
    middlename:str 
    idnumber:int 
    idfront:str 
    idback:str 
    signature:str 
    nextofkinname:str 
    location:str 
        
        
class ProfileBase(ProfileCreate):
    id:int 
    class Config:
        orm_mode=True
        
class Token(BaseModel):
    access_token:str 
    token_type:str 
    
class TokenData(BaseModel):
    username:str |None=None 
    

