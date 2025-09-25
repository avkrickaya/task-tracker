# app/routes/categories.py
# Эндпоинты для категорий

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.category import CategoryCreate, CategoryOut
from app.crud.category import get_categories, get_category, create_category

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=List[CategoryOut])
def read_categories(db: Session = Depends(get_db)):
    """Вернуть все категории."""
    return get_categories(db)

@router.get("/{category_id}", response_model=CategoryOut)
def read_category(category_id: int, db: Session = Depends(get_db)):
    cat = get_category(db, category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    return cat

@router.post("/", response_model=CategoryOut)
def create_new_category(category_in: CategoryCreate, db: Session = Depends(get_db)):
    """Создать новую категорию."""
    return create_category(db, category_in)
