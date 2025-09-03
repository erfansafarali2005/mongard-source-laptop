import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='logs' , exchange_type='fanout')
result = channel.queue_declare(queue='one' , exclusive=True)
channel.queue_bind(queue='one' , exchange='logs')

def callback(ch , method , body , properties):
    print(f'your message recieved {body}')
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=result.method.queue , on_message_callback=callback )

channel.start_consuming()