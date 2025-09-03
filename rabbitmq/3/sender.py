import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.queue_declare(queue='one')

ch.basic_publish(exchange='' , routing_key='one' , body='Hello World from sender in quqe on with direct exchange')
#                    ^-> empty means direct |  ^-> routingkey is the name of the queeu (its password of the destination)
print("sending message")

ch.close()


# rounting key is the passowrd of the destination  : one -> direct exchange needs a password | fanout dosnt need password | topic needs a topic password *.*.important : the password is the last one important