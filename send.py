import pika

# 1. Establish connection to local RabbitMQ broker
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# 2. Declare a queue (creates it if it doesn't exist)
channel.queue_declare(queue='test_queue', durable=True)

# 3. Publish a message
message = "Hello from VS Code!"
channel.basic_publish(
    exchange='',
    routing_key='test_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent  # Make message persistent
    )
)

print(f" [x] Sent '{message}'")
connection.close()