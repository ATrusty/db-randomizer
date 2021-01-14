import json
import requests
import random

#api stuffs
YGO_API_ENDPOINT = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
ID_QUERY = '?id='
CARDSET_QUERY = '?cardset='
YGO_PHOTOCLOUD_ENDPOINT = 'https://storage.googleapis.com/ygoprodeck.com/pics/'
IOC_URI = 'invasion%20of%20chaos'
DATE_QUERY = '?&startdate=01/01/2000&enddate=8/05/2005&dateregion=tcg_date'

#ydk file format
RANDOMIZER_TAG = '#created by db-randomizer\n'
MAIN_DECK = '#main\n'
EXTRA_DECK = '#extra\n'
SIDE_DECK = '!side\n'

#while conditions
MD_ITERS = 40 #command arg?
SD_ITERS = 15
ED_ITERS = 15

with open('banlist.json') as banFile:
    banlist = json.load(banFile)

mainDeck = []
sideDeck = []
extraDeck = []

response = requests.get(YGO_API_ENDPOINT + DATE_QUERY)
cardSet = response.json()["data"]

#filter lists so we can fit the cards in the proper spot
deckCandidates = [card for card in cardSet if card["type"] != "Fusion Monster"]
extraDeckCandidates = [card for card in cardSet if card["type"] == "Fusion Monster"]
f = open("outputdeck.ydk", "w")
f.write(RANDOMIZER_TAG)
#let's generate the main deck
f.write(MAIN_DECK)
while(len(mainDeck) < 40):
    currentCardID = str(random.choice(deckCandidates)["id"])
    if(not currentCardID in banlist.keys()):
        if(mainDeck.count(currentCardID) < 3):
            mainDeck.append(currentCardID)
            f.write(currentCardID + '\n')
        else:
            #we already have 3 of this card, we cannot add it
            pass
    else:
        if(banlist[currentCardID] > 0):
            banlist[currentCardID] = banlist[currentCardID]-1
            mainDeck.append(currentCardID)
            f.write(currentCardID + '\n')
        else:
            pass

#let's generate the extra deck
f.write(EXTRA_DECK)
while(len(extraDeck) < 15):
    currentCardID = str(random.choice(extraDeckCandidates)["id"])
    if(not currentCardID in banlist.keys()):
        if(extraDeck.count(currentCardID) < 3):
            extraDeck.append(currentCardID)
            f.write(currentCardID + '\n')
        else:
            #we have 3 already in our extra deck, so dont add this in
            pass
    else:
        #we shouldnt need the secondary check here for the 3 card limit because the banlist implementation
        #should handle that for us
        if(banlist[currentCardID] > 0):
            banlist[currentCardID] = banlist[currentCardID]-1
            extraDeck.append(currentCardID)
            f.write(currentCardID + '\n')
        else:
            pass

#let's generate the side deck
f.write(SIDE_DECK)
while(len(sideDeck) < 15):
    currentCardID = str(random.choice(deckCandidates)["id"])
    if(not currentCardID in banlist.keys()):
        if(mainDeck.count(currentCardID) + sideDeck.count(currentCardID) < 3):
            sideDeck.append(currentCardID)
            f.write(currentCardID + '\n')
        else:
            #we have 3 already in our side+main deck, so dont add this in
            pass
    else:
        if(banlist[currentCardID] > 0):
            banlist[currentCardID] = banlist[currentCardID]-1
            sideDeck.append(currentCardID)
            f.write(currentCardID + '\n')
        else:
            pass

#done
f.close()