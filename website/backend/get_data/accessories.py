import json
import requests

url = 'https://api.hypixel.net/v2/resources/skyblock/items'


accessories = []

result = requests.get(url).json()['items']

for res in result:
    if 'category' in res:
        if res['category'] == 'ACCESSORY':
            accessories.append(
                {
                    'ID': str(res['id']),
                    'name': res['name']
                }
            )

with open('../json_data/accessories_all.json', 'w') as f:
    json.dump(accessories, f)
