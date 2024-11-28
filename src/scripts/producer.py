import sys
import os
import random
import json
import time
from datetime import datetime
import paho.mqtt.client as mqtt
import traceback

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import get_config

CONFIG = get_config(os.getenv("ENV", "development"))

client = mqtt.Client()
# client.username_pw_set(CONFIG['MQTT_USERNAME'], CONFIG['MQTT_PASSWORD'])
client.connect(CONFIG['MQTT_HOST'], CONFIG['MQTT_PORT'])

def publish_message(message, topic):
    try:
        message["timestamp"] = datetime.utcnow().strftime("%Y-%m-%d")
        while True:
            time.sleep(1)
            client.publish(topic, json.dumps(message))
    except Exception as e:
        traceback.print_exc()

message = {'field': 'status', 'value': random.randint(0, 6)}

publish_message(message, CONFIG['MQTT_TOPIC'])