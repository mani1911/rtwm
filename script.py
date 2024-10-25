import os
from dotenv import load_dotenv
import json
from pymongo import MongoClient

from helpers import fetch_data

load_dotenv()

api_key = os.getenv('API_KEY')
api_url = f'{os.getenv('API_URL')}?lat={13.0843}&lon={80.2705}&appid={api_key}'
mongo_uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(os.getenv('MONGO_INITDB_ROOT_USERNAME'), os.getenv('MONGO_INITDB_ROOT_PASSWORD'), "localhost", os.getenv('ME_CONFIG_MONGODB_PORT'), os.getenv('DATABASE'))

client = MongoClient(mongo_uri)

print(f'mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@localhost:{os.getenv('ME_CONFIG_MONGODB_PORT')}/{os.getenv('DATABASE')}?retryWrites=true&w=majority')

db = client[os.getenv('DATABASE')]
collection = db["test"]

# # print(collection)
# print([row for row in collection.find()])

weather_data = fetch_data(api_url)
print(weather_data)
if weather_data is not None:
    main = weather_data["weather"][0]["main"]
    feels_like = weather_data["main"]["feels_like"] - 273.15
    temp = weather_data["main"]["temp"] - 273.15
    dt = weather_data["dt"]
    
    print(main, feels_like, temp, dt)
    
