import json
import requests
import random

#api stuffs
YGO_API_ENDPOINT = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
ID_QUERY = '?id='
CARDSET_QUERY = '?cardset='
YGO_PHOTOCLOUD_ENDPOINT = 'https://storage.googleapis.com/ygoprodeck.com/pics/'
IOC_URI = 'invasion%20of%20chaos'

#ydk file format
RANDOMIZER_TAG = '#created by db-randomizer\n'
MAIN_DECK = '#main\n'
EXTRA_DECK = '#extra\n'
SIDE_DECK = '!side\n'

with open('banlist.json') as f:
    banlist = json.load(f)

#print(banlist["18144506"]) #test some random banned card (harpie's feather duster)
response = requests.get(YGO_API_ENDPOINT + CARDSET_QUERY + IOC_URI)
cardSet = response.json()["data"]
deck = []

f = open("outputdeck.ydk", "w")
f.write(RANDOMIZER_TAG)
f.write(MAIN_DECK)
for iteration in range(40):
    f.write(str(random.choice(cardSet)["id"]) + '\n')
f.write(EXTRA_DECK)
f.write(SIDE_DECK)
for iteration in range(15):
    f.write(str(random.choice(cardSet)["id"]) + '\n')
f.close()

