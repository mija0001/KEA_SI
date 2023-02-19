from configurator import Configurator
from publisher import Publisher
from subscriber import Subscriber


"""Test script for Configurator, Publisher and Subscriber"""


### Create exchange, queues and bindings, if they don't already exist ###
Configurator().create_exchange('TestExchange', 'topic') # Create an exchange with the name 'TestExchange' and the type 'topic'
Configurator().create_queue('A') # Create a queue with the name 'A'
Configurator().create_queue('B') # Create a queue with the name 'B'
Configurator().create_queue('C') # Create a queue with the name 'C'
Configurator().bind_queue_to_exchange('A', 'TestExchange', 'KeyA') # Bind the queue 'A' to the exchange 'TestExchange' with the routing key 'KeyA'
Configurator().bind_queue_to_exchange('B', 'TestExchange', 'KeyB') # Bind the queue 'B' to the exchange 'TestExchange' with the routing key 'KeyB'
Configurator().bind_queue_to_exchange('C', 'TestExchange', 'KeyC') # Bind the queue 'C' to the exchange 'TestExchange' with the routing key 'KeyC'


### Publish messages to the exchange ###
Publisher().publish_message('TestExchange', 'KeyA', 'The quick, brown fox jumps over a lazy dog.')
Publisher().publish_message('TestExchange', 'KeyB', 'DJs flock by when MTV ax quiz prog.')
Publisher().publish_message('TestExchange', 'KeyC', 'Junk MTV quiz graced by fox whelps.')
Publisher().publish_message('TestExchange', 'KeyA', 'Bawds jog, flick quartz, vex nymphs.')
Publisher().publish_message('TestExchange', 'KeyB', 'Waltz, bad nymph, for quick jigs vex!')
Publisher().publish_message('TestExchange', 'KeyC', 'Fox nymphs grab quick-jived waltz.')


### Start subscriber ###
subscriber = Subscriber()
subscriber.startConsuming()
