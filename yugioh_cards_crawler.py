#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, urllib.request, urllib.parse
from tqdm import tqdm

def get_all_cards():
    req = urllib.request.urlopen('https://www.ygohub.com/api/all_cards')
    cont = req.read().decode('utf-8')
    json_obj = json.loads(cont)
    if json_obj['status'] != 'success':
        return None
    else:
        return json_obj['cards']

def get_card_info(card_name):
    escaped_card_name = urllib.parse.quote(card_name)
    req = urllib.request.urlopen(
        'https://www.ygohub.com/api/card_info?name=' + escaped_card_name)
    cont = req.read().decode('utf-8')
    json_obj = json.loads(cont)
    if json_obj['status'] != 'success':
        return None
    else:
        return json_obj['card']

def get_merged_cards(card_names):
    all_cards = dict()
    for card_name in tqdm(card_names):
        card_info = get_card_info(card_name)
        all_cards[card_name] = card_info
    return all_cards

if __name__ == '__main__':
    card_names = get_all_cards()
    cards = get_merged_cards(card_names)
    json.dump(cards, open("cards.json", "w"), indent=4)
