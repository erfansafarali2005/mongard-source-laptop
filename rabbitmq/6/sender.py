# https://www.rabbitmq.com/docs/publishers

import pika
import time

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localahost' , credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='one')

channel.basic_publish(exchange='' , routing_key='one' , body='Hello world im from sender' , properties=pika.BasicProperties(
    content_type='text/plain',
    content_encoding='gzip',
    timestamp=10000000000,
    expiration=str(time.time()) # notice : we must give a feature time this is now time
    delivery_mode=2, # 1 : in ram , 2 : in disk . !!! it may lower your speed . if you want to save queues on disk choose 2 . like in payment queues . but in logs or etc no need for 1
    user_id='10' # User.user_id
    app_id='2' # Account.AccountConfig.id ! -> this is wrong just get the case
    type='exchange.queue'
    headers={'name':'amir' , 'age':'30'}
))

channel.close()