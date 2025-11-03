from datetime import datetime
from pydantic import BaseModel


class KafkaTaskCreatedMessage(BaseModel):
    task_id: int
    task: str
    description: str | None = None
    user_id: int
    status: str
    deadline: datetime.datetime | None = None