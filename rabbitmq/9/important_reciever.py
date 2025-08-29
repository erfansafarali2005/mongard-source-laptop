import pika
import os

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs' , exchange_type='topic')

result = channel.queue_declare(queue='' , exclusive=True)

channel.queue_bind(queue=result.method.queue , exchange='topic_logs' , routing_key='#.important') # -> # means everything befoe is not important : #.important = *.*.important

print('wating for messages ...')

def callback(ch , method , properties , body):
    print(f"{body} from queue {result.method.queue} queue")
    with open('error_logs.log' , 'a') as el:
        el.write(f'{str(body)} \n')
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=result.method.queue , on_message_callback=callback )

channel.start_consuming()


# if i use no routing key in exchange : then it was a fanout so rabbitmq gives error : you declear a topic but no routing key provided