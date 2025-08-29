import pika

credentials = pika.PlainCredentials(username='amir' , password='amir')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs' , exchange_type='topic')

message = {
    'error.warning.important' : 'this is an important message',
    'info.debug.notimportant' : 'this is an info not important message',
}

for k , v in message.items():
    channel.basic_publish(exchange='topic_logs' ,routing_key=k , body=v)
print('message send ...')

channel.close()