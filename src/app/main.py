from faststream import FastStream
from app.kafka.kafka_broker import broker


app = FastStream(broker)
