# This is readme file to run this demo.

## Kafka using Python

- **All these commands are to be run in the directory where your Kafka server is saved. *kafka_server* in my case**

- starting zookeeper
  - sh ./bin/zookeeper-server-start.sh config/zookeeper.properties

- starting brokers
  - ./bin/kafka-server-start.sh config/server.properties

- creating topic
  - ./bin/kafka-topics.sh --create --topic kafka-spark  --bootstrap-server localhost:9092 --replication-factor 2 --partitions 2
  - here kafka-spark is the topic i have created replication factor is 2 because there are 2 brokers

- listing topics
  - ./bin/kafka-topics.sh --list --bootstrap-server localhost:9092 localhost:2181

- describing a topic
  - ./bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic kafka-spark

- creating prodcer for sending messages
  - ./bin/kafka-console-producer.sh  --broker-list localhost:9092 --topic kafka-spark

- listening to a producer as a consumer
  - ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic kafka-spark --from-beginning

- deleting a topic
  - ./bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic kafka-spark
