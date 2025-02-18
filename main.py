from fastapi import FastAPI, Depends,HTTPException
from .database import create_db_and_tables, get_session
from .models import Product,ProductCart
from sqlmodel import Session, select
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

@app.get("/products/{product_id}")
async def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}")
async def update_product(product_id: int, updated_product: Product, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product.name = updated_product.name
    product.price = updated_product.price
    product.image = updated_product.image
    
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@app.delete("/products/{product_id}")
async def delete_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    session.delete(product)
    session.commit()
    return {"message": "Product deleted successfully"}

#@app.post("/cart/add")
#async def add_to_cart(product_id: int, session: Session = Depends(get_session)):
   # product = session.get(Product, product_id)
   # if not product:
       # raise HTTPException(status_code=404, detail="Product not found")
    
    # Ovde moze da se implementira model za kosnicka
   # return {"message": f"Product {product.name} added to cart"}
@app.post("/cart/add")
async def add_to_cart(product_id: int, quantity: int, owner_id: int, session: Session = Depends(get_session)):
    # Proveri dali produktot postoi
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Presmetaj final_price
    final_price = product.price * quantity

    # Kreiraj nov zapis vo koshnichkata
    cart_item = ProductCart(
        product_id=product.id,
        product_name=product.name,
        quantity=quantity,
        final_price=final_price,
        owner_id=owner_id
    )

    session.add(cart_item)
    session.commit()
    session.refresh(cart_item)
    return {"message": f"Added {product.name} {final_price} denars to cart", "cart_item": cart_item}
