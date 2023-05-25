### This doesn't work on Windows, but it works on Linux - due to the way the fork() system call works on Windows.

import redis
from rq import Queue, Worker

redis_client = redis.Redis(host='localhost', port=6379, db=0)

queue = Queue(connection=redis_client)

worker = Worker(queues=[queue], connection=redis_client)
worker.work(with_scheduler=True)