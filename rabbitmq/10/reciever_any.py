import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='he' , exchange_type='headers')

result = channel.queue_declare(queue='hq-any' , exclusive=True)

bind_args = {'x-match':'any' , 'name':'mongard' , 'age':'5'}


channel.queue_bind(queue=result.method.queue , exchange='he' , arguments=bind_args) # binding of headers are not password so its not routing key


def callback(ch , method , properties , body):
    print(f'message recieved .. {body}')
    print(f'the queue is {result.method.queue}')
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=result.method.queue , on_message_callback=callback)  

print('wating for messages ..')

channel.start_consuming()
    