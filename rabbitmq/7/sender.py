import pika
import time

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localahost' , credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='one')

channel.basic_publish(exchange='' , routing_key='one' , body='Hello world im from sender' , properties=pika.BasicProperties(
                                                                                                            headers={'name':'amir' , 'age':'30'}
                                                                                                            ))

channel.close()