from sqlalchemy import Column,Integer,ForeignKey,String ,DATE
from sqlalchemy.orm import relationship

from database import Base  


class User(Base):
    __tablename__='users'
    id=Column('id',Integer,primary_key=True)
    username=Column('username',String,unique=True)
    password=Column('password',String)
    
    role=Column('role',String)
    profile=relationship('Profile',back_populates='user',uselist=False)
    
class Profile(Base):
    __tablename__='profile'
    id=Column('id',Integer,primary_key=True)
    user_id=Column('user_id',Integer,ForeignKey('users.id'))
    email=Column('email',String)
    firstname=Column('firstname',String)
    lastname=Column('lastname',String)
    middlename=Column('middlename',String)
    idnumber=Column('idnumber',Integer)
    idfront=Column('idfront',String)
    idback=Column('idback',String)
    signature=Column('signature',String)
    nextofkinname=Column('nextofkinname',String)
    location=Column('location',String)
    user=relationship('User',back_populates='profile',uselist=False)
    
    