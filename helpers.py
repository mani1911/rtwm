import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError, RequestException
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()
mongo_uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(os.getenv('MONGO_INITDB_ROOT_USERNAME'), os.getenv('MONGO_INITDB_ROOT_PASSWORD'), "localhost", os.getenv('ME_CONFIG_MONGODB_PORT'), os.getenv('DATABASE'))

client = MongoClient(mongo_uri)
db = client[os.getenv('DATABASE')]

def fetch_data(url: str):
    try:
        response = requests.get(url=url, timeout=10)
        response.raise_for_status()
        
        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Timeout:
        print("The request timed out")
    except ConnectionError:
        print("Connection error occurred")
    except RequestException as err:
        print(f"An error occurred: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def insert_weather_info(main, feels_like, temp, dt):
    try:
        collection = db["weather-data"]
        dict = {"main": main, "feels_like": feels_like, "temp": temp, "dt": dt}
        res = collection.insert_one(dict)
    except Exception as e:
        print(e)



    