import json
import pika
import threading
from nexiona.config import DATA

# CLASE QUE PERMITE RECOGER LOS MENSAJES CONCURRENTEMENTE PARA PODER RECOGER MENSAJES 
# QUE LLEGUEN AL MISMO TIEMPO EN TIEMPO REAL
class threaded_AMQP(threading.Thread):
    def __init__(self, RABBIT_URL, ROUTING_KEY, QUEUE_NAME, EXCHANGE, THREADS):
        threading.Thread.__init__(self)
        parameters = pika.URLParameters(RABBIT_URL)
        connection = pika.BlockingConnection(parameters)
        self.channel = connection.channel()
        self.channel.queue_declare(queue=QUEUE_NAME, auto_delete=False)
        self.channel.queue_bind(queue=QUEUE_NAME, exchange=EXCHANGE, routing_key=ROUTING_KEY)
        self.channel.basic_qos(prefetch_count=THREADS*10)
        self.channel.basic_consume(QUEUE_NAME, on_message_callback=self.callback)
        threading.Thread(target=self.channel.basic_consume(QUEUE_NAME, on_message_callback=self.callback))

    def callback(self, channel, method, properties, body):
        message = json.loads(body)
        DATA.append(message)
        print("New data income from AMQP")
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def run(self):
        print("Starting thread to consume from AMPQ")
        self.channel.start_consuming()


