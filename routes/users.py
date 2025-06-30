from fastapi import APIRouter,Depends,HTTPException
from schemas import UserCreate,UserBase
from models import User,Profile
from security import *
from database import connect
from sqlalchemy.orm  import Session
user_router=APIRouter(tags=['users'],prefix='/users')


@user_router.post('/new',response_model=UserBase)
async def new(req:UserCreate,db:Session=Depends(connect)):
    user=db.query(User).filter(User.username==req.username).first()
    if user:
        raise HTTPException(status_code=400,detail='username already exist')
    password=get_password_hash(req.password)
    user=User(**req.dict())
    user.password=password
    db.add(user)
    db.commit()
    db.refresh(user)
    return user 
    
@user_router.post('/token')
async def login(form_data:OAuth2PasswordRequestForm=Depends(),
    db:Session=Depends(connect))->Token:
    
    user=authenticate_user(username=form_data.username,password=form_data.password,db=db)
    if not user:
         raise HTTPException(
             status_code=status.HTTP_401_UNAUTHORIZED,
             detail='Incorrect username or password',
             headers={"WWW-Authenticate":'Bearer'}
         )
    access_token_expires=timedelta(minutes=30)
    access_token=create_access_token(
        data={"sub":user.username,'role':user.role},
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token,token_type='bearer')



@user_router.get('/me')
async def read_user_me(current:User=Depends(get_current_active_user)):
    return current 


@user_router.get('/all')
async def get_all(db:Session=Depends(connect)):
    return db.query(User).all()


@user_router.post('/profile')
async def create_profile(
    req:ProfileCreate,
    current:User=Depends(get_current_active_user)
    ,
    db:Session=Depends(connect)):
    profile=Profile(**req.dict())
    profile.user_id=current.id
    db.add(profile)
    db.commit()
    db.refresh(profile)
        
    return profile

@user_router.get('/myprofile')
async def get_profile(current:User=Depends(get_current_active_user)
    ,db:Session=Depends(connect)):
    return db.query(Profile).filter(Profile.user_id==current.id).first()
@user_router.get('/all')
async def get_profiles(
    db:Session=Depends(connect)):
    return db.query(Profile).all()