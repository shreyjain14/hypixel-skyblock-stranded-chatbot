import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def news():
    url = 'https://api.hypixel.net/v2/skyblock/news'
    headers = {
        'API-Key': os.getenv('API_KEY')
    }

    response = requests.get(url, headers=headers).json()

    with open('website/backend/json_data/news.json', 'w') as f:
        json.dump(response, f)
