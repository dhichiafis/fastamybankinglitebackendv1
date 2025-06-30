from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    environment:str 
    debug:bool=False 
    
    database_url:str 
    
    class Config:
        env_file=".env"
        
        
s=Settings()