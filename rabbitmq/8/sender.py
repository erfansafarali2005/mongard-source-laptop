import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

# No need fo  queeue : fanout send request to all of the queues

channel.exchange_declare(exchange='logs' , exchange_type='fanout')

channel.basic_publish(exchange='logs' , routing_key='' , body='im a request coming from a fanout exchange fron sender')

print('Message Sent ...')

connection.close()