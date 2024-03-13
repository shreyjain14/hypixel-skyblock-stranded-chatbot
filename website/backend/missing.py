import json


def accessories():

    with open('website/backend/json_data/accessories_all_stranded.json') as f:
        all_accessories = json.load(f)

    with open('website/backend/json_data/user_accessories.json') as f:
        user_accessories = json.load(f)

    all_accessories_ids = []
    duplicates = []
    missing_accessories = []
    duplicate_accessories = []

    accessories_hashmap = {}

    for accessory in all_accessories:
        all_accessories_ids.append(accessory['ID'])
        accessories_hashmap[accessory['ID']] = accessory['name']

    for accessory in user_accessories:
        try:
            all_accessories_ids.remove(accessory['ID'])
        except ValueError:
            duplicates.append(accessory['ID'])

    for accessory in all_accessories_ids:
        missing_accessories.append(accessories_hashmap[accessory])

    for accessory in duplicate_accessories:
        duplicate_accessories.append(accessories_hashmap[accessory])

    with open('website/backend/json_data/user_accessories_data.json', 'w') as f:
        json.dump({
            "Missing Accessories": missing_accessories,
            "Duplicate Accessories": duplicate_accessories
        }, f)


if __name__ == '__main__':
    accessories()
