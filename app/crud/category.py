# app/crud/category.py

from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate

def get_categories(db: Session):
    """Вернуть все категории."""
    return db.query(Category).all()

def get_category(db: Session, category_id: int):
    """Вернуть категорию по id."""
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db: Session, cat_in: CategoryCreate):
    """Создать категорию."""
    db_cat = Category(**cat_in.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat
