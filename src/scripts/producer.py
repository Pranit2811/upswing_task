import pika
import random
import json
import schedule
import time

def publish_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', virtual_host='/'))
    channel = connection.channel()

    channel.queue_declare(queue='MQTT_MESSAGE', durable=True)

    body = json.dumps({'field': 'status', 'value': random.randint(0, 6)})

    channel.basic_publish(exchange='',routing_key='MQTT_MESSAGE', body=body)  


    connection.close()

schedule.every(1).seconds.do(publish_message)

while True:
    schedule.run_pending()
    time.sleep(0.1)