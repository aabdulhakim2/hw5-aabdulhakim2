import requests
import os
import json
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.themoviedb.org/3/trending/movie/day"


params = {
    "api-key": os.getenv('API_KEY')
}


response = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}"
    ##BASE_URL
 ## API_KEY
  )

response_json = response.json()

try:
    trending = response_json["results"]
    for article in trending[0:10]:
        print(article["original_title"])
except KeyError:
    print("Couldn't fetch trending movies!")
