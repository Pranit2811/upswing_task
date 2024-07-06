import pika
import sys
from pymongo import MongoClient
import json
from datetime import datetime

client = MongoClient('mongodb+srv://pranitraut8625:VMraAerXKOwFa179@cluster0.386qnbl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['upswing_report']
collection = db['upswing']


def consume_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', virtual_host='/'))
    channel = connection.channel()

    channel.queue_declare(queue='MQTT_MESSAGE', durable=True)

    def callback(ch, method, properties, body):
        insert_status(json.loads(body))

    channel.basic_consume(queue='MQTT_MESSAGE', on_message_callback=callback, auto_ack=True)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print(" [!] Exiting...")
        connection.close()
        sys.exit(0)

def insert_status(body):
    body["timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    result = collection.insert_one(body)
    print(f"Inserted message with ID: {result.inserted_id}")

if __name__ == '__main__':
    consume_message()


# VMraAerXKOwFa179