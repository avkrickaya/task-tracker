# app/models/category.py
# Модель категории задач (Category)

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Category(Base):
    __tablename__ = "categories"  # имя таблицы

    id = Column(Integer, primary_key=True, index=True)  # id категории
    name = Column(String, unique=True, nullable=False)  # название категории (уникальное)

    # связь "один ко многим": категория -> задачи
    tasks = relationship("Task", back_populates="category")
