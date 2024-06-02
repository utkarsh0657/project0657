from sqlalchemy.orm import Session
from product_api import modal, schemas
# from product_api.modal import Product

def get_product(db: Session, product_id: int):
    return db.query(modal.Product).filter(modal.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(modal.Product).offset(skip).limit(limit).all()

def create_product( product: schemas.ProductCreate,db: Session):
    db_product = modal.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = db.query(modal.Product).filter(modal.Product.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.category = product.category
        db_product.price = product.price
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(modal.Product).filter(modal.Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

