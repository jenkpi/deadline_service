from datetime import datetime
from typing import Protocol

from sqlalchemy import select
from app.mappers.mappers import build_task_schema_from_orm
from app.sqlalchemy_orm_models.sqlalchemy_orm_task_deadlines_models import (
    TaskDeadlineOrm,
)
from app.task_schemas.task_schemas import (
    GetTaskDeadlineResponse,
)
from app.database import new_session


class TaskDeadlineAbstractRepository(Protocol):
    async def add_task(self, task: TaskDeadlineOrm) -> int: ...

    async def get_overdue_tasks(self) -> GetTaskDeadlineResponse: ...


class TaskDeadlineRepository:
    async def add_task(self, task: TaskDeadlineOrm) -> int:
        async with new_session() as session:
            session.add(task)
            await session.flush()
            task_id = task.task_id
            await session.commit()

            return task_id

    async def get_overdue_tasks(self) -> GetTaskDeadlineResponse:
        async with new_session() as session:
            query = (
                select(TaskDeadlineOrm)
                .where(TaskDeadlineOrm.deadline <= datetime.now())
                .with_for_update(skip_locked=True)
            )
            task_models = (await session.execute(query)).scalars().all()

            task_schemas = build_task_schema_from_orm(task_models)
            return task_schemas
