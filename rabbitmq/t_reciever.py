import pika

credentials = pika.PlainCredentials(username='amir' ,password= 'amir')

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

result = channel.queue_declare(queue='' , exclusive=True)

channel.exchange_declare(exchange='logs' , exchange_type='topic')

channel.queue_bind(queue=result.method.queue , exchange='logs' , routing_key='*.*.important')

def callback(ch , method , properties , body):
    print(f"{body} from queue {result.method.queue} queue")
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=result.method.queu , on_message_callback=callback)    

channel.start_consuming()