from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import user
from routers import user_router
from routers import task_router
from database import engine

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow these origins
    allow_credentials=True,
    allow_methods=["*"],    # Allow all HTTP methods
    allow_headers=["*"],    # Allow all headers
)


# Create tables in the database
user.Base.metadata.create_all(bind=engine)


# Include API routers
app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(task_router.router, prefix="/tasks", tags=["Tasks"])


