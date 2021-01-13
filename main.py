import json
import requests

#api stuffs
YGO_API_ENDPOINT = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
ID_QUERY = '?id='
CARDSET_QUERY = '?cardset='
YGO_PHOTOCLOUD_ENDPOINT = 'https://storage.googleapis.com/ygoprodeck.com/pics/'
IOC_URI = 'invasion%20of%20chaos'

#ydk file format
RANDOMIZER_TAG = '#created by db-randomizer'
MAIN_DECK = '#main'
EXTRA_DECK = '#extra'
SIDE_DECK = '!side'

with open('banlist.json') as f:
    banlist = json.load(f)

#print(banlist["18144506"]) #test some random banned card (harpie's feather duster)
response = requests.get(YGO_API_ENDPOINT + CARDSET_QUERY + IOC_URI)
cardSet = response.json()["data"]

for card in cardSet:
    print(str(card["name"]) + " " + str(card["id"]))
    print('\n')
