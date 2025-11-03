from datetime import datetime
from app.kafka.kafka_broker import broker
from app.task_schemas.task_schemas import KafkaTaskCreatedMessage


@broker.subscriber("tasks_topic")
async def build_redis_message(task_data: KafkaTaskCreatedMessage):
    task_id = task_data.task_id
    deadline = task_data.deadline
    time_for_sleep = datetime.now() - deadline
