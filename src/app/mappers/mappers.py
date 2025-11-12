from collections.abc import Iterable
from app.sqlalchemy_orm_models.sqlalchemy_orm_task_deadlines_models import (
    TaskDeadlineOrm,
)
from app.task_schemas.task_schemas import (
    FullTaskDeadline,
    GetTaskDeadlineResponse,
    KafkaDeadlineMessage,
    KafkaTaskCreatedMessage,
)


def build_task_orm_model(task_data: KafkaTaskCreatedMessage) -> TaskDeadlineOrm:  # noqa: E501
    payload = task_data.model_dump(include={"task_id", "user_id", "deadline"})
    return TaskDeadlineOrm(**payload)


def build_task_schema_from_orm(
    task_models: Iterable[TaskDeadlineOrm],
) -> GetTaskDeadlineResponse:
    task_schemas = [
        FullTaskDeadline.model_validate(task_model, from_attributes=True)
        for task_model in task_models
    ]
    return GetTaskDeadlineResponse(tasks=task_schemas)


def build_kafka_deadline_message(task_data: FullTaskDeadline) -> KafkaDeadlineMessage:  # noqa: E501
    kafka_task_created_message = KafkaDeadlineMessage(
        task_id=task_data.task_id, user_id=task_data.user_id
    )  # noqa: E501
    return kafka_task_created_message
