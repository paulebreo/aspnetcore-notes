import pika
import sys



credentials = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters('localhost', 5673, '/', credentials)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(exchange="logs", routing_key="", body=message)

print("[x] Sent %r" % message)
connection.close()