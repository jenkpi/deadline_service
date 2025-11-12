import asyncio
from app.mappers.mappers import (
    build_kafka_deadline_message,
    build_task_orm_model,
)
from app.task_deadline_repository.task_deadline_repository import (
    TaskDeadlineAbstractRepository,
)
from app.task_schemas.task_schemas import (
    GetTaskDeadlineResponse,
    KafkaTaskCreatedMessage,
)
from faststream.confluent.publisher.usecase import DefaultPublisher
from faststream.confluent import KafkaBroker


class TaskDeadlineService:
    def __init__(
        self,
        task_repo: TaskDeadlineAbstractRepository,
        publisher: DefaultPublisher,
        sleep_time: int,
        broker: KafkaBroker,
        topic: str,
    ):
        self.task_repo = task_repo
        self.nearest_deadline = None
        self.nearest_task = None
        self.publisher = publisher
        self.sleep_time = sleep_time
        self.broker = broker
        subscriber_dec = self.broker.subscriber(topic)
        subscriber_dec(self.add_task)

    async def add_task(self, task_data: KafkaTaskCreatedMessage) -> int:
        task = build_task_orm_model(task_data)
        return await self.task_repo.add_task(task)

    async def kafka_publish_deadline_message(self, tasks: GetTaskDeadlineResponse):  # noqa: E501
        for task in tasks.tasks:
            await self.publisher.publish(message=build_kafka_deadline_message(task))  # noqa: E501
        return

    async def deadline_manager(self):
        while True:  # noqa: WPS457
            print("вызов дедлайн менеджера")  # noqa: WPS421
            tasks = await self.task_repo.get_overdue_tasks()
            await self.kafka_publish_deadline_message(tasks)
            asyncio.sleep(self.sleep_time)
