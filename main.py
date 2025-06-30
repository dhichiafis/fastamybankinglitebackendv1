from fastapi import FastAPI,APIRouter
from database import Base,engine
import uvicorn
from routes.users import user_router
Base.metadata.create_all(bind=engine)

app=FastAPI()



app.include_router(user_router)

@app.get('/')
async def home():
    return {'home':'this is the home page'}


if __name__=="__main__":
    uvicorn.run("main:app",reload=True,host='127.0.0.1',port=8000)