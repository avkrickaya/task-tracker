# app/crud/sprint.py

from sqlalchemy.orm import Session
from app.models.sprint import Sprint
from app.schemas.sprint import SprintCreate

def get_sprints(db: Session):
    """Вернуть все спринты."""
    return db.query(Sprint).all()

def get_sprint(db: Session, sprint_id: int):
    """Вернуть спринт по id."""
    return db.query(Sprint).filter(Sprint.id == sprint_id).first()

def create_sprint(db: Session, sprint_in: SprintCreate):
    """Создать спринт."""
    db_sprint = Sprint(**sprint_in.dict())
    db.add(db_sprint)
    db.commit()
    db.refresh(db_sprint)
    return db_sprint
