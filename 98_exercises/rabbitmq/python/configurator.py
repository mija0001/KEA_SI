import pika # Module for RabbitMQ


class Configurator:
    """Class for configuring exchanges, queues and bindings in RabbitMQ"""
    
    def __init__(self):
        """Initialize the configurator, load credentials and set up connection parameters"""
        import credentials # Local credentials file to prevent publishing credentials to GitHub
        self.config_credentials = pika.PlainCredentials(credentials.config_user, credentials.config_password)
        self.config_parameters = pika.ConnectionParameters(host=credentials.host, credentials=self.config_credentials)

    
    # Establish connection to RabbitMQ server
    def create_connection(self):
        """Create a connection to the RabbitMQ server"""
        self.connection = pika.BlockingConnection(self.config_parameters)
        self.channel = self.connection.channel()


    def create_exchange(self, exchange_name, exchange_type):
        """Create an exchange with the given name and type
        :param exchange_name: The name of the exchange to create
        :param exchange_type: The type of the exchange to create (direct, topic, fanout or headers)
            direct: The exchange will route messages to queues based on a routing key, without wildcards
            topic: The exchange will route messages to queues based on a routing key, with wildcards
            fanout: The exchange will route messages to all queues
            headers: The exchange will route messages to queues based on message headers
        """
        self.create_connection()
        self.channel.exchange_declare(exchange_name, durable=True, exchange_type=exchange_type)
        self.close_connection()


    def create_queue(self, queue_name):
        """Create a queue with the given name
        :param queue_name: The name of the queue to create
        """
        self.create_connection()
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.close_connection()


    def bind_queue_to_exchange(self, queue_name, exchange_name, routing_key):
        """Bind a queue to an exchange with the given routing key
        :param queue_name: The name of the queue to bind
        :param exchange_name: The name of the exchange to bind to
        :param routing_key: The routing key to use when binding the queue to the exchange
        """
        self.create_connection()
        self.channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)
        self.close_connection()


    def close_connection(self):
        """Close the connection to the RabbitMQ server"""
        self.channel.close()
        self.connection.close()
