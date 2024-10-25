import redis
from rq import Worker, Queue, Connection

# Create a Redis connection
conn = redis.Redis()

# Define the queues to listen to
listen = ['add_weather_entry']

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()