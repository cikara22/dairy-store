from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):    
    id: int | None = Field(default=None, primary_key=True)    
    username: str = Field(unique=True, nullable=False)    
    email: str = Field(unique=True, nullable=False)    
    password: str = Field(nullable=False)    
    is_admin: bool = Field(default=False)
    
class Product(SQLModel, table=True):    
    id: int | None = Field(default=None, primary_key=True)    
    name: str = Field(nullable=False)    
    price: int = Field(nullable=False)    
    image: str = Field(nullable=False)    
   