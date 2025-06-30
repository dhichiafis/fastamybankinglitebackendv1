from fastapi import FastAPI,APIRouter
from database import Base,engine
import uvicorn
from mangum import Mangum
from routes.users import user_router
Base.metadata.create_all(bind=engine)

app=FastAPI()



app.include_router(user_router)

@app.get('/')
async def home():
    return {'home':'this is the home page'}


handler=Mangum(app)