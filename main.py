import json

#api stuffs
YGO_API_ENDPOINT = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
ID_QUERY = '?id='
YGO_PHOTOCLOUD_ENDPOINT = 'https://storage.googleapis.com/ygoprodeck.com/pics/'

#ydk file format
RANDOMIZER_TAG = '#created by db-randomizer'
MAIN_DECK = '#main'
EXTRA_DECK = '#extra'
SIDE_DECK = '!side'

import json

with open('banlist.json') as f:
    banlist = json.load(f)

print(banlist["18144506"]) #test some random banned card (harpie's feather duster)