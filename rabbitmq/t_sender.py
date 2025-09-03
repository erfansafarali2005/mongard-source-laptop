import pika

credentials = pika.PlainCredentials(username='amir' ,password= 'amir')

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host='localhost' , credentials=credentials))

ch = connection.channel()

messages = {
    'error.warning.important' : 'this is an important message',
    'info.debug.notimportant' : 'this is an info not important message',
}

#ch.queue_declare(queue='one')

ch.exchange_declare(exchange='logs' , exchange_type='topic')

for k,v in messages:
    ch.basic_publish(exchange='' , routing_key=k, body=v , properties=pika.BasicProperties(headers={'name':'erfan'}))

print('message sent . . .')

connection.close()