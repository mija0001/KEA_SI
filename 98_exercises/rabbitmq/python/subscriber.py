import pika
from threading import Thread

class Subscriber:
    """Class for subscribing to messages from RabbitMQ"""
    def __init__(self):
        """Initialize the subscriber, load credentials and set up connection parameters"""
        import credentials
        self.subscriber_credentials = pika.PlainCredentials(credentials.subscriber_user, credentials.subscriber_password)
        self.subscriber_parameters = pika.ConnectionParameters(host=credentials.host, credentials=self.subscriber_credentials)


    def create_connection(self):
        """Create a connection to the RabbitMQ server"""
        self.connection = pika.BlockingConnection(self.subscriber_parameters)
        self.channel = self.connection.channel()


    def close_connection(self):
        """Close the connection to the RabbitMQ server"""
        self.channel.close()
        self.connection.close()
    

    def callbackFunctionForQueueA(self, ch, method, properties, body):
        """Callback function for queue A
        Prints the message received from queue A
        :param ch: The channel the message was received on
        :param method: The method used to deliver the message
        :param properties: The properties of the message
        :param body: The message body
        """
        print("Received message from queue A: %r" % body)
    

    def callbackFunctionForQueueB(self, ch, method, properties, body):
        """Callback function for queue B
        Prints the message received from queue B
        :param ch: The channel the message was received on
        :param method: The method used to deliver the message
        :param properties: The properties of the message
        :param body: The message body
        """
        print("Received message from queue B: %r" % body)
    

    def callbackFunctionForQueueC(self, ch, method, properties, body):
        """Callback function for queue C
        Prints the message received from queue C
        :param ch: The channel the message was received on
        :param method: The method used to deliver the message
        :param properties: The properties of the message
        :param body: The message body
        """
        print("Received message from queue C: %r" % body)
    

    def startConsumers(self):
        """Connects to the RabbitMQ server and starts a thread for consuming messages for each queue
        """
        self.create_connection()
        self.channel.basic_consume(queue='A', on_message_callback=self.callbackFunctionForQueueA, auto_ack=True)
        self.channel.basic_consume(queue='B', on_message_callback=self.callbackFunctionForQueueB, auto_ack=True)
        self.channel.basic_consume(queue='C', on_message_callback=self.callbackFunctionForQueueC, auto_ack=True)
        Thread(target= self.channel.start_consuming()).start()


    def startConsuming(self):
        """Starts consuming messages from the RabbitMQ server,
        tries to reconnect if the connection is lost"""
        while True:
            try:
                self.startConsumers()
            except KeyboardInterrupt: # Catch Ctrl + C and exit cleanly, so that the program can be terminated from the terminal
                print("Keyboard interrupt - shutting down")
                self.channel.stop_consuming()
                self.close_connection()
                break
            except:
                continue
