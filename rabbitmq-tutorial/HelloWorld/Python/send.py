import pika

credentials = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters('localhost', 5673, '/', credentials)


connection = pika.BlockingConnection(params)

channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()