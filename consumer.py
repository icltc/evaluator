import time

from kafka import TopicPartition, KafkaConsumer
consumer = KafkaConsumer(
    'evaluator',
    group_id='local_group',
    bootstrap_servers='localhost:9092')

while True:
    print consumer.assignment()
    print next(consumer)