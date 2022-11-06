from nexiona.receiverMQ import threaded_AMQP
from nexiona.receiverREST import threaded_REST
from nexiona.config import THREADS, RABBIT_URL, ROUTING_KEY, QUEUE_NAME, EXCHANGE, API_URL, API_DATA, USER, PASSWORD, SELF_API_HOST, SELF_API_PORT, MODE
from selfAPI import app

# PUESTA EN MARCHA DE LOS RECEPTORES DE MENSAJES 
for i in range(THREADS):
    if(MODE != 2):
        print('Launching thread', i+1)
        td = threaded_AMQP(RABBIT_URL, ROUTING_KEY, QUEUE_NAME, EXCHANGE, THREADS)
        td.start()
    if(MODE != 1):
        api = threaded_REST(API_URL, API_DATA, USER, PASSWORD)
        api.run()

#PUESTA EN MARCHA DE LA API PROPIA
app.run(debug=True, use_reloader=False, host=SELF_API_HOST, port=SELF_API_PORT)
