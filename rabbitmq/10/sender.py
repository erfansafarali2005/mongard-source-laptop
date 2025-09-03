import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='he' , exchange_type='headers')
message = 'hello world'

ch.basic_publish(exchange='he' , routing_key='' , body=message , properties=pika.BasicProperties(headers={'name':'mongard'}))

print('message sent ...')

ch.close()