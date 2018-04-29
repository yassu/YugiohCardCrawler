#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, urllib.request, urllib.parse
from optparse import OptionParser
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

def getParser():
    parser = OptionParser()
    parser.add_option(
        "-o", "--output-file", dest="output_filename",
        default="cards.json",
        help="output filename")
    return parser

if __name__ == '__main__':
    parser = getParser()
    (options, args) = parser.parse_args()

    card_names = get_all_cards()
    cards = get_merged_cards(card_names)
    json.dump(cards, open(options.output_filename, "w"), indent=4)
