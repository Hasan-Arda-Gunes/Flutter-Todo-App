from passlib.context import CryptContext
from sqlalchemy.orm import Session
from repository import user_repository
from schemas.user_schema import UserCreate
from models import User
from auth import hash_password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user_data: UserCreate) -> User:
    existing_user = user_repository.get_user_by_username(db, user_data.username)
    if existing_user:
        raise ValueError("Username already taken")
    
    hashed_pwd = hash_password(user_data.password)

    new_user = User(
        username=user_data.username,
        password=hashed_pwd
    )

    created_user = user_repository.create_user(db, new_user)
    return created_user

def get_all_users_service(db: Session):
    return db.query(User).all()