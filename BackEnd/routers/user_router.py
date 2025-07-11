from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user_schema import UserCreate
from service.user_service import create_user_service, get_all_users_service
from database import get_db

router = APIRouter()

@router.post("/create")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user_service(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get_all")
def get_all_users( db: Session = Depends(get_db)):
    return get_all_users_service(db)
