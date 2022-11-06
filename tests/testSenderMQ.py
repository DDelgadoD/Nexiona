import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel = connection.channel()
channel.exchange_declare(exchange='surveillance', exchange_type='fanout')

messages = [
            '{"PATH": "/home", "ID":"194.68.69.94"}',
            '{"PATH": "/page1", "ID":"194.68.69.94"}',
            '{"PAToH": "/page7", "ID":"194.68.69.94"}',
            '{"PATH": "/page3", "ID":"194.68.69.94"}',
            '{"PATH": "/page2", "IDo":"194.68.69.94"}',
            '{"PATH": "/page3", "ID":"194.68.69.94"}',
            '{"PATH": "/home", "ID":"194.68.69.95"}',
            '{"PATH": "/page1", "ID":"194.68.69.95"}',
            '{"PATH": "/page2", "ID":"194.68.69.95"}',
            '{"PATH": "/page3", "ID":"194.68.69.95"}',
            '{"PATH": "/home", "ID":"194.68.69.94"}',
            '{"PATH": "/home", "ID":"194.68.69.96"}',
            '{"PATH": "/page5", "ID":"194.68.69.96"}'
        ]

for message in messages: 
    channel.basic_publish(exchange='surveillance', routing_key='nexiona', body=message)
    print("Message Sent")

connection.close()
