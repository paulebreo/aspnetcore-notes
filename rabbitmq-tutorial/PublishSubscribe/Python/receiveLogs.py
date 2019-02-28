import pika
import sys



credentials = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters('localhost', 5673, '/', credentials)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

result = channel.queue_declare(exclusive=True)