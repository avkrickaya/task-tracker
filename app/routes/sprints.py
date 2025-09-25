# app/routes/sprints.py
# Эндпоинты для спринтов

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.sprint import SprintCreate, SprintOut
from app.crud.sprint import get_sprints, get_sprint, create_sprint

router = APIRouter(prefix="/sprints", tags=["sprints"])

@router.get("/", response_model=List[SprintOut])
def read_sprints(db: Session = Depends(get_db)):
    """Вернуть все спринты."""
    return get_sprints(db)

@router.get("/{sprint_id}", response_model=SprintOut)
def read_sprint(sprint_id: int, db: Session = Depends(get_db)):
    sprint = get_sprint(db, sprint_id)
    if not sprint:
        raise HTTPException(status_code=404, detail="Sprint not found")
    return sprint

@router.post("/", response_model=SprintOut)
def create_new_sprint(sprint_in: SprintCreate, db: Session = Depends(get_db)):
    """Создать новый спринт."""
    return create_sprint(db, sprint_in)

