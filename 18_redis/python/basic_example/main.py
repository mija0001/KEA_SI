import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

redis_client.set('myKey', 'myValue')

value = redis_client.get('myKey')

# redis_client.setex('myKey', 10, 'myValue')

print(str(value, 'utf-8'))