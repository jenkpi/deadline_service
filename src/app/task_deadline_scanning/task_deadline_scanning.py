from app.mappers.mappers import build_kafka_deadline_message
from app.task_schemas.task_schemas import GetTaskDeadlineResponse
from faststream.confluent.publisher.usecase import DefaultPublisher


class TaskDeadlinePublisher:
    def __init__(self, publisher: DefaultPublisher):
        self.publisher = publisher

    async def kafka_publish_deadline_message(self, tasks: GetTaskDeadlineResponse):  # noqa: E501
        for task in tasks.tasks:
            await self.publisher.publish(message=build_kafka_deadline_message(task))  # noqa: E501
        return  # noqa: WPS324
