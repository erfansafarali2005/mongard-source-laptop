import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

queue = channel.queue_declare(queue='one')

def callback(ch , method , properties , body):
    print(f'hello i got your message {body}')

channel.basic_consume(queue='one' , on_message_callback=callback ,auto_ack=True)

channel.start_consuming()