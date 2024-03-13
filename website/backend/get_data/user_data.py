import nbt
import json
import io
import base64

from website.backend import clear, check


def user_accessories(username, pid, save=False):

    uuid = check.username(username)
    profile = check.profileID(uuid, pid)['members'][uuid]

    with open('website/backend/json_data/user_profile.json', 'w') as f:
        json.dump(profile, f)

    accessories = profile['inventory']['bag_contents']['talisman_bag']['data']
    data = nbt.nbt.NBTFile(fileobj=io.BytesIO(base64.b64decode(accessories)))[0]

    bag = []

    for i in data:
        if 'tag' in i:
            bag.append(
                {
                    'ID': str(i['tag']['ExtraAttributes']['id']),
                    'name': clear.item_name(i['tag']['display']['Name'])
                }
            )

    u_data = {
        'level': profile['leveling']['experience']/100,
        'jacob': profile['jacobs_contest'],
        'coins': profile['currencies']['coin_purse'],
    }

    if save:
        with open('website/backend/json_data/user_accessories.json', 'w') as f:
            json.dump(bag, f)

        with open('website/backend/json_data/user_skills.json', 'w') as f:
            json.dump(profile['player_data']['experience'], f)

    else:
        return u_data


if __name__ == '__main__':
    uuid = check.username('DarkDash')
    pid = check.stranded(uuid)[0][0]

    user_accessories('DarkDash', pid, save=True)

