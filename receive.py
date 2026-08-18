import pika
import sys

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='test_queue', durable=True)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        # Acknowledge message processing
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Fair dispatch: don't give more than 1 message to a worker at a time
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='test_queue', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)