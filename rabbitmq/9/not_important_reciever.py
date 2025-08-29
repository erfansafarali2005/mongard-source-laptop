import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs' , exchange_type='topic')

result = channel.queue_declare(queue='' , exclusive=True) # queue between exchange and consumer

channel.queue_bind(queue=result.method.queue , exchange='topic_logs' , routing_key='*.*.notimportant') # if we add a normal string like : important then its a direct exchange

print('wating for messages ...')

def callback(ch , method , properties , body):
    print(f"{body} from queue {result.method.queue} queue")
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=result.method.queue , on_message_callback=callback )

channel.start_consuming()