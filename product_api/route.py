from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from product_api.schemas import Product,ProductBase,ProductCreate
from product_api.database import SessionLocal, engine
from product_api.crud import get_product as get_product_serv,get_products as get_products_serv,create_product as create_product_serv,update_product as update_product_serv,delete_product as delete_product_serv
# modal.Product.metadata.create_all(bind=engine)
# from product_api.modal import products
# from product_api import modal, schemas

print("JDhJDHjkshdjkhajkdhja")
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/products/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product_serv( product,db)


@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product_serv(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/products/", response_model=list[Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products_serv(db, skip=skip, limit=limit)
    return products

@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = update_product_serv(db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product_serv(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

