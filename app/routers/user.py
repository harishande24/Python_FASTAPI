

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from passlib.context import CryptContext
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session 
from app import models
from app import schemas, utils
import email_validator
from app.database import engine,get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/", status_code= status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):


    #Hash password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model= schemas.UserOut)
def get_user(id:int , db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist")

    return user

