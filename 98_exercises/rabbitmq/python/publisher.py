import pika # Module for RabbitMQ


class Publisher:
    """Class for publishing messages to RabbitMQ"""

    def __init__(self):
        """Initialize the publisher, load credentials and set up connection parameters"""
        import credentials # Local credentials file to prevent publishing credentials to GitHub
        self.publisher_credentials = pika.PlainCredentials(credentials.publisher_user, credentials.publisher_password)
        self.publisher_parameters = pika.ConnectionParameters(host=credentials.host, credentials=self.publisher_credentials)

    
    # Establish connection to RabbitMQ server
    def create_connection(self):
        """Create a connection to the RabbitMQ server"""
        self.connection = pika.BlockingConnection(self.publisher_parameters)
        self.channel = self.connection.channel()

    
    def publish_message(self, exchange_name, routing_key, message):
        """Publish a message to the given exchange with the given routing key
        :param exchange_name: The name of the exchange to publish to
        :param routing_key: The routing key to use when publishing the message
        :param message: The message to publish
        """
        self.create_connection()
        self.channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)
        self.close_connection()

    
    def close_connection(self):
        """Close the connection to the RabbitMQ server"""
        self.channel.close()
        self.connection.close()
