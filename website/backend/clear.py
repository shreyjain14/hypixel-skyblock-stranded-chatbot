def item_name(item):
    name = ""
    for index, letter in enumerate(item):
        if letter != '§':
            if item[index-1] != '§':
                name += letter
    return name


def mayor_perks(perks_response):
    perks = []
    for perk in perks_response:
        fixed_perk = {
            'name': perk['name'],
            'description': item_name(perk['description'])
        }
        perks.append(fixed_perk)

    return perks


def candidates_perks(candidates):
    res = []

    for candidate in candidates:
        candidate_data = {
            'name': candidate['name'],
            # 'key': candidate['key'],
            'votes': candidate['votes'],
            'perks': mayor_perks(candidate['perks'])
        }
        res.append(candidate_data)

    return res


if __name__ == '__main__':
    print(item_name('§6Personal Compactor 7000'))
