import json
import streamlit as st
import time
from confluent_kafka import Producer


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
producer = Producer(kafka_config)

# By above, I will be able to login in Kafka and be able to send a data to my kafka topics

st.title("GlobeFT Big Data Customer Click Analytics")
user_id = st.number_input("user id", min_value = 1, max_value = 100000, step = 1)
activity = st.selectbox("activity",["view_product", "add_to_cart", "checkout", "search", "wishlist"])
product = st.selectbox("product",["Laptop", "mobile", "headphone", "smartwatch", "camera", "tablet"])

# I have to send all this data to my KAFKA_TOPIC

def send_event():
    event = {
        "user_id":user_id,
        "activity":activity,
        "product":product,
        "timestamp":int(time.time())
    }
    
    producer.produce(KAFKA_TOPIC, key=str(user_id), value = json.dumps(event))
    producer.flush()
    st.success(f"send this event:{event}")

# This function will be called once I am going to click the button

if st.button("send data"):
    send_event()


