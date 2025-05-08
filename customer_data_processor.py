from confluent_kafka import Consumer
from pymongo import MongoClient
from pymongo.server_api import ServerApi  # This is the correct import
import json
from datetime import datetime
import logging

kafka_config = {
    'bootstrap.servers': 'pkc-619z3.us-east1.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'UMTPRKQ7VS73G3PC',
    'sasl.password': 'nleugewnSmii4NqfxIzy/ChOP1HUxoGZzS+sKpzryV8yNnT00snbbPeldNiGwtm6',
    'group.id': 'sentiment_analysis_group',
    'auto.offset.reset': 'earliest'
}


KAFKA_TOPIC = "customer_click_data"

# Connecting Mongodb
uri = "mongodb+srv://saurabhkamal:1235dfg@sudhanshu.lbqhjqm.mongodb.net/?retryWrites=true&w=majority&appName=Sudhanshu"


def connect_mongo():
    client = MongoClient(uri,server_api=ServerApi('1'))
    return client

# Consuming the message and process it
def process_message():
    consumer = Consumer(kafka_config) # Consumer will establish the communication
    consumer.subscribe([KAFKA_TOPIC]) # will subscribe the topic "customer_click_data"

    # Read the data from Kafka and send it directly to the MongoDB
    mongo_client = connect_mongo()
    db = mongo_client["cutomer_click_behaviour"]
    event_collection = db["click_data"]
    # See all my data in respective collection

    # We have run this entire thing into infinite loop, so that my producer will keep on producing it and consumer will keep on consuming this data
    # it is going to be live

    try:
        while True :
            msg = consumer.poll(1.0)   
            if msg is None :
                continue
            if msg.error():
                continue
            try :
                value = json.loads(msg.value().decode('utf-8'))
                value["kafka_metadata"] = {
                    'topic':msg.topic(),
                    "partition" : msg.partition(),
                    "offset" : msg.offset(),
                    "timestamp":datetime.now().isoformat()
                }
                
                result = event_collection.insert_one(value)
                print(result)
            except Exception as e :
                print(e)
                
    except Exception as e :
        print(e)
            
if __name__ == "__main__":
    process_message()