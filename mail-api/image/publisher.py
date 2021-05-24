from kafka import KafkaProducer
import json
import os


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=[os.environ['KAFKA_BROKER']],
                         value_serializer=json_serializer)
