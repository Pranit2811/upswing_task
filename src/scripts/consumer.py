import sys
import os
from pymongo import MongoClient
import json
import paho.mqtt.client as mqtt
import traceback

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import get_config

CONFIG = get_config(os.getenv("ENV", "development"))

client = MongoClient(CONFIG['MONGO_CLIENT'])
db = client[CONFIG['MONGO_DB']]
collection = db[CONFIG['MONGO_COLLECTION']]

client = mqtt.Client()
client.connect(CONFIG['MQTT_HOST'], CONFIG['MQTT_PORT'])

def insert_status(payload):
    result = collection.insert_one(payload)
    print(f"Inserted message with ID: {result.inserted_id}")

def subscribe_topic(client: mqtt, topic):
    try:
        def on_message(client, userdata, msg):
            decoded_msg = json.loads(msg.payload.decode())
            print(f"Received {decoded_msg} from {msg.topic} topic","\n")
            insert_status(decoded_msg)
        client.subscribe(topic)
        client.on_message = on_message
    except Exception as e:
        traceback.print_exc()

subscribe_topic(client, CONFIG['MQTT_TOPIC'])
client.loop_forever()