from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

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
   
    carts: list["ProductCart"] = Relationship(back_populates="product")  

class ProductCart(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id", nullable=False)
    product_name: str = Field(nullable=False)
    quantity: int = Field(nullable=False)
    final_price: int = Field(nullable=False)
    owner_id: int = Field(nullable=False)

    product: Optional[Product] = Relationship(back_populates="carts")