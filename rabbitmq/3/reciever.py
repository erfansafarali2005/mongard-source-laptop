import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='one') # we say that because : we dont know if the reciever is first or sender

def callback(ch , method , properties , body):
   print( f'hello i got your message , this was your message {body} \n' )

channel.basic_consume(queue='one' , on_message_callback=callback , auto_ack=True)
#                                                                     ^-> hey queue ! i got the message remove it from the queue
print('wating for message to exit press ctrl+c ...')
channel.start_consuming()

# if reciever is off : the messages will stay in queueu until its ran