from kafka import KafkaProducer
import json
from data import get_registered_user
import time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

'''def get_partition(key, all, available):
    return 0
'''
#producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer = json_serializer, partitioner=get_partition)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer = json_serializer)

if __name__=="__main__":
    while True:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
        time.sleep(4)

