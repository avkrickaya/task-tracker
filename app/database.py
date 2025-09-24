# Отвечает за подключение к базе данных и создание сессий
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base #базовый класс моделей
from sqlalchemy.orm import sessionmaker # фабрика сесий

# URL базы данных. Для SQLite можно просто указать путь к файлу
SQLALCHEMY_DATABASE_URL = "sqlite:///./task_tracker.db"

# Создаем движок (engine) - объект, который управляет соединением с БД
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} # нужно только для SQLite
)

# Создаем "фабрику" сессий - объект, который будет выдавать соединения
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей (все модели будут от него наследоваться)
Base = declarative_base()

# Функция-зависимость для FastAPI - возвращает сессию, закрывается после запроса
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()