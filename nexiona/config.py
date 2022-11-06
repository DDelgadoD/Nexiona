# APP CONFIG
DATA = []           # Almacén de datos no persistente
MODE = 3            # Selector de modo: [ 1: Solo AMQP - 2: Solo API REST - 3: Ambos ]
THREADS = 5         # Número de hilos de ejecución a lanzar

# Información relacionada con el host de mensajes
HOST = "localhost"
VHOST = "%2f"
USER = 'nexiona'
PASSWORD = 'nexiona22'

# Información relacionada con AMQP
RABBIT_URL = F"amqp://{USER}:{PASSWORD}@{HOST}"
ROUTING_KEY = "nexiona"
QUEUE_NAME = "test.nexiona"
EXCHANGE = "surveillance"

# Información relacionada con API REST
PORT_REST = 15672
API_URL = F"http://{HOST}:{PORT_REST}/api/queues/{VHOST}/{QUEUE_NAME}/get"
API_DATA = {"count": 1, "ackmode": "ack_requeue_false", "encoding": "auto"}  #Necesario para API de RabbitMQ
 
# Información relacionada con el API propio
SELF_API_HOST = "localhost"
SELF_API_PORT = 5000