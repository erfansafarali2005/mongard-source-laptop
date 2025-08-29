import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='one')

def callback(ch , method , properties , body):
    print(f"A message is recieved {body}")

channel.basic_consume(queue='one' , on_message_callback=callback , auto_ack=True)

channel.start_consuming()