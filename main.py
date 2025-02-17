from fastapi import FastAPI, Depends
from .database import create_db_and_tables, get_session
from .models import Product
from sqlmodel import Session
app = FastAPI()

@app.on_event("startup")
def on_startup():    
    create_db_and_tables()
    
@app.get("/")
async def root():    
    return {"message": "Hello World"}

@app.get("/products")
async def get_users(session: Session = Depends(get_session)):
    products = session.query(Product).all()  # Query to get all users
    return products# Return list of users