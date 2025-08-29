import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='one')


def callback(ch , method , properties , body):
    print(f'i got your message {body}')

channel.basic_consume(queue='one' , on_message_callback=callback , auto_ack=True)

print('Im ready for receieving , press ctrl + C to Exit ...')

channel.start_consuming()