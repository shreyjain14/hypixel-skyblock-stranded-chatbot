import json
import requests
from website.backend import clear


def mayor_json():
    url = 'https://api.hypixel.net/v2/resources/skyblock/election'

    response = requests.get(url).json()

    year = response['mayor']['election']['year']

    if 'current' in response:

        n_year = response['current']['year']

        elections = {
            'current_mayor': {
                'year': year,
                'name': response['mayor']['name'],
                # 'key': response['mayor']['key'],
                # 'perks': clear.mayor_perks(response['mayor']['perks'])
            },
            f'year_{year}_results': {
                'year': year,
                'candidates': clear.candidates_perks(response['mayor']['election']['candidates'])
            },
            f'year_{n_year}_elections': {
                'year': n_year,
                'candidates': clear.candidates_perks(response['current']['candidates'])
            }
        }

    else:

        elections = {
            'current_mayor': {
                'year': year,
                'name': response['mayor']['name'],
                # 'key': response['mayor']['key'],
                # 'perks': clear.mayor_perks(response['mayor']['perks'])
            },
            f'year_{year}_results': {
                'year': year,
                'candidates': clear.candidates_perks(response['mayor']['election']['candidates'])
            }
        }

    with open('website/backend/json_data/mayors.json', 'w') as f:
        json.dump(elections, f)


if __name__ == '__main__':
    mayor_json()
