from sqlmodel import SQLModel, create_engine, Session
from .models import User,Product,ProductCart
DATABASE_URL = "postgresql://postgres:230902@localhost/dairy-store"
 
engine = create_engine(DATABASE_URL)
 
 
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
 
 
def get_session():
    with Session(engine) as session:
        yield session
