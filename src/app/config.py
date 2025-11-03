from pydantic_settings import BaseSettings


class KafkaSettings(BaseSettings):
    socket: str
    topic: str
