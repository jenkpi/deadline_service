import datetime
from pydantic import BaseModel


class KafkaTaskCreatedMessage(BaseModel):
    task_id: int
    task: str
    description: str | None = None
    user_id: int
    status: str
    deadline: datetime.datetime


class FullTaskDeadline(BaseModel):
    task_id: int
    user_id: int
    deadline: datetime.datetime


class GetTaskDeadlineResponse(BaseModel):
    tasks: list[FullTaskDeadline]


class KafkaDeadlineMessage(BaseModel):
    task_id: int
    user_id: int
