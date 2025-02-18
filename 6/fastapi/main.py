from fastapi import FastAPI
from database import Base, engine
from api import auth
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
