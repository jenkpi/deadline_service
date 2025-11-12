from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import TIMESTAMP


class Base(DeclarativeBase):
    """
    Базовый класс для ORM-моделей SQLAlchemy.

    Используется как точка входа для декларативного стиля описания таблиц.
    Все ORM-модели приложения должны наследоваться от этого класса
    """


class TaskDeadlineOrm(Base):
    __tablename__ = "task_deadline"

    task_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    deadline: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True))
