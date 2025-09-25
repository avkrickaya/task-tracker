# Настройка подключения к базе данных и зависимость get_db для FastAPI

from sqlalchemy import create_engine  # движок для подключения к БД
from sqlalchemy.orm import sessionmaker, declarative_base  # фабрика сессий и базовый класс для моделей

# URL подключения к SQLite — файл task_tracker.db в корне проекта
SQLALCHEMY_DATABASE_URL = "sqlite:///./task_tracker.db"

# Создаём движок SQLAlchemy; для SQLite нужно передать check_same_thread=False
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Создаём фабрику сессий; SessionLocal() будет выдавать объект сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс, от которого будут наследоваться модели SQLAlchemy
Base = declarative_base()

# Dependency для FastAPI — используем в маршрутах, чтобы получить сессию БД
def get_db():
    db = SessionLocal()     # создаём сессию
    try:
        yield db            # возвращаем её вызывающему коду (в эндпоинте)
    finally:
        db.close()          # закрываем сессию после обработки запроса
