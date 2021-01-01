import random
from bingo_card import BingoCard
from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True
)
template = env.get_template('card.jinja')
import json
import os
import sys


with open('bingo_words.txt') as f:
    words = f.read().split('\n')


card = BingoCard(words)

print('New card created.')
set_id = sys.argv[1]

if os.path.exists(f'stored_cards/{set_id}.json'):
    with open(f'stored_cards/{set_id}.json') as f:
        set_data = json.load(f)
else:
    set_data = []

card_id = len(set_data)
card_encode = {'card_id': card_id, 'card': card.card}
set_data.append(card_encode)
with open(f'stored_cards/{set_id}.json', 'w') as f:
    json.dump(set_data, f)


render = template.render(card=card.card, set_id=set_id, card_id=card_id)
with open('result.html', 'w') as f:
    f.write(render)