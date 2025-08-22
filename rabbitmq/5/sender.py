import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

queue = channel.queue_declare(queue='one')

channel.basic_publish(exchange='' , routing_key='one' , body='Hello i sent you message')

print('message sent ...')

channel.close()