import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()


channel.exchange_declare(exchange='logs' , exchange_type='fanout') # no need for declearing queue , its fanout and sends reqs to all queues 

channel.basic_publish(exchange='logs' , routing_key='' , body='Hllo from sender' , properties=pika.BasicProperties(
    headers={'hello':'amir'},
    type='plain/text',
    content_encoding='gzip',
    user_id=12,
))

channel.close()