import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='he' , exchange_type='headers')

bind_args = {'x_match':'all' , 'name':'mongard' , 'age':'15'}

result = channel.queue_declare(queue='hq-any' , exclusive=True)

channel.queue_bind(queue=result.method.queue , exchange='he')

def callback(ch , method , properties , body):
    print(f'message recieved .. {body}')
    print(f'the queue is {result.method.queue}')
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=result.method.queue , on_message_callback=callback)  

print('wating for messages ..')

channel.start_consuming()
    


# !!! Because we dont declear any queue for sender , we must firt start consumers then senders !!! we can't also declear a queue for header exchange !!!!    