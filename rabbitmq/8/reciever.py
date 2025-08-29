import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='logs' , exchange_type='fanout')

# !!! we declear a queue between exchange and consumer not a queue between sender to exchange !!!

#  empty string : i want to create a queue with every new terminal so rabbitmq declears a unique name
result = channel.queue_declare(queue='' , exclusive=True) # exclusive is not unique to the consumer , when cosnumer is dead , the queue will be dead
channel.queue_bind(exchange='logs' , queue=result.method.queue) # the queu name ? we dont know . so i find it inside its variable
# why don't we declear exchange for consumer ? thats the binding job (:

print(result.method.queue)

def callback(ch , method , properties , body):
    print(f'your message recieved {body}')
    print(method)
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=result.method.queue , on_message_callback=callback)

print('Start taking logs ...')

channel.start_consuming()

# binding is for conection=g queues from : exchange to consumer , the sender to consumer no need for binding now !