import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

queue = channel.queue_declare(queue='one')

channel.basic_publish(exchange='' , routing_key='one' , body='Hi from a randome sender in one queue')

channel.close()