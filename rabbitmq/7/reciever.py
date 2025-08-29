import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='one')

def callback(ch , method , properties , body):
    print(f"A message is recieved {body}")
    print(f'properties are {properties}')
    print(properties.headers)
    print(method)
    channel.basic_ack(delivery_tag=method.delivery_tag) # this sends ack when the task is completed not immideitly after recieving . delivery_tag is a tag that is unique created by rabbitmq from 1 to etc ! we can know who was the first !

channel.basic_qos(prefetch_count=1) # it sends one and one and one request to servers
channel.basic_consume(queue='one' , on_message_callback=callback)

channel.start_consuming()