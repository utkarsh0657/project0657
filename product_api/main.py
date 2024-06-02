# # app/main.py

# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from products.schemas import Product,ProductBase,ProductCreate
# from database import SessionLocal, engine
# from products.crud import get_product,get_products,create_product,update_product,delete_product
# # modal.Product.metadata.create_all(bind=engine)
# from modal import products
# from products import modal, schemas

# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# def create_product(db: Session, product: schemas.ProductCreate):
#     db_product = modal.Product(**product.dict())
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product

# @app.post("/products/", response_model=Product)
# def create_product(product: ProductCreate, db: Session = Depends(get_db)):
#     return create_product(db=db, product=product)



# # @app.get("/products/{product_id}", response_model=Product)
# # def read_product(product_id: int, db: Session = Depends(get_db)):
# #     db_product = get_product(db, product_id=product_id)
# #     if db_product is None:
# #         raise HTTPException(status_code=404, detail="Product not found")
# #     return db_product

# # @app.get("/products/", response_model=list[Product])
# # def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
# #     products = get_products(db, skip=skip, limit=limit)
# #     return products

# # @app.put("/products/{product_id}", response_model=Product)
# # def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
# #     db_product = update_product(db, product_id=product_id, product=product)
# #     if db_product is None:
# #         raise HTTPException(status_code=404, detail="Product not found")
# #     return db_product

# # @app.delete("/products/{product_id}", response_model=Product)
# # def delete_product(product_id: int, db: Session = Depends(get_db)):
# #     db_product = delete_product(db, product_id=product_id)
# #     if db_product is None:
# #         raise HTTPException(status_code=404, detail="Product not found")
# #     return db_product



from fastapi import FastAPI
# from book_management.routers import book_route
# from book_management.routers import user_route
# from book_management.routers import publisher_route
# from book_management.routers import author_route
# from product_api import route
import sys

from . import route

import uvicorn


app = FastAPI()

# @app.get("/")
# def func():
#     return {"hello"}

app.include_router(route.router)
# app.include_router(book_route.router)
# app.include_router(publisher_route.router)
# app.include_router(author_route.router)

if __name__ == "__main__":
  uvicorn.run(app=app,host= 'http://127.0.0.1',port=8000)