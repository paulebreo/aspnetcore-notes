
import pika
import time

credentials = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters('localhost', 5673, '/', credentials)

start_time = time.time()
while True:
    try:
        conn = pika.BlockingConnection(params)
        break

    except pika.exceptions.AMQPConnectionError:
        print("error connection")
        time.sleep(2)
    if time.time() - start_time > 5:
        print("couldnt connection after 30 seconds")
        exit(1)