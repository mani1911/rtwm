import os
from dotenv import load_dotenv
from pymongo import MongoClient
from rq import Queue
from rq.job import Job
import redis

from helpers import fetch_data, insert_weather_info

load_dotenv()
redis_connection = redis.Redis(host='localhost', port=6379, db=0)

api_key = os.getenv('API_KEY')
api_url = f'{os.getenv('API_URL')}?lat={13.0843}&lon={80.2705}&appid={api_key}'

# collection = db["weather-data"]

q = Queue('add_weather_entry', connection=redis_connection)

weather_data = fetch_data(api_url)
if weather_data is not None:
    main = weather_data["weather"][0]["main"]
    feels_like = weather_data["main"]["feels_like"] - 273.15
    temp = weather_data["main"]["temp"] - 273.15
    dt = weather_data["dt"]
    
    # main = "hellp"
    # feels_like = "warm"
    # temp = 32
    # dt = 100
    print(main, feels_like, temp, dt)
    job = q.enqueue(insert_weather_info, main, feels_like, temp, dt)

    
