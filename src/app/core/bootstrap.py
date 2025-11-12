from functools import cache
from app.config import ServiceSettings
from app.tasks_deadline_service.tasks_deadline_service import TaskDeadlineService  # noqa: E501
from app.task_deadline_repository.task_deadline_repository import TaskDeadlineRepository  # noqa: E501
from app.kafka.kafka_broker import kafka_publisher
from app.kafka.kafka_broker import broker
from faststream.confluent import KafkaBroker
from faststream.confluent.publisher.usecase import DefaultPublisher
from app.kafka.kafka_broker import kafka_settings


@cache
def get_task_deadline_repository() -> TaskDeadlineRepository:
    return TaskDeadlineRepository()


@cache
def get_kafka_publisher() -> DefaultPublisher:
    return kafka_publisher


@cache
def get_sleep_time() -> int:
    service_settings = ServiceSettings()  # type: ignore[call-arg]
    return service_settings.sleep_time


@cache
def get_broker() -> KafkaBroker:
    return broker


@cache
def get_topic() -> str:
    return kafka_settings.tasks_topic


@cache
def get_task_deadline_service() -> TaskDeadlineService:
    task_deadline_service = TaskDeadlineService(
        get_task_deadline_repository(),
        get_kafka_publisher(),
        get_sleep_time(),
        get_broker(),
        get_topic(),
    )
    return task_deadline_service
