import json

with open('accessories_all_stranded.json') as f:
    accessories_json = json.load(f)['accessories']

hashmap = {}
accessories = []
for accessory in accessories_json:
    hashmap[accessory['ID']] = accessory['name']
    accessories.append(accessory['ID'])

accessories.sort()

acc_f = []

for accessory in accessories:
    acc_f.append(
        {
            'ID': accessory,
            'Name': hashmap[accessory],
            'Upgradable': True,
            'FinalUpgrade': True,
            'Upgrades': []
        }
    )

with open('accessories_stranded.json', 'w') as f:
    json.dump(acc_f, f)