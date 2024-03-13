import requests
import dotenv
import os
import json


def username(uname):
    response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{uname}").json()
    if 'id' in response:
        return response['id']
    else:
        return "ERROR"


def stranded(uuid):
    dotenv.load_dotenv()

    headers = {'API-Key': os.getenv('API_KEY')}
    params = {'uuid': uuid}

    url = 'https://api.hypixel.net/v2/skyblock/profiles'

    response = requests.get(url, headers=headers, params=params).json()

    profiles = []

    if response['success']:
        for profile_info in response['profiles']:
            if 'game_mode' in profile_info:
                if profile_info['game_mode'] == 'island':
                    profiles.append((profile_info['profile_id'], profile_info['cute_name']))

    return profiles


def profileID(uuid, pid):
    dotenv.load_dotenv()

    headers = {'API-Key': os.getenv('API_KEY')}
    params = {'uuid': uuid}

    url = 'https://api.hypixel.net/v2/skyblock/profiles'

    response = requests.get(url, headers=headers, params=params).json()

    if response['success']:
        for profile_info in response['profiles']:
            if profile_info['profile_id'] == pid:
                return profile_info

    return 'ERROR'


def missing_accessories(bag):
    with open("accessories.txt") as accessories:
        all_accessories_read = accessories.readlines()

    all_accessories = []

    for accessory in all_accessories_read:
        all_accessories.append(accessory[:-1])

    print(all_accessories)


if __name__ == "__main__":
    uuid = username('Loidza')
    pid = stranded(uuid)[0][0]
    profile = profileID(uuid, pid)['members'][uuid]

    with open('get_data/LoidzaProfile.json', 'w') as f:
        json.dump(profile, f)
