import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError, RequestException

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