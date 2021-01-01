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


with open('bingo_words.txt') as f:
    words = f.read().split('\n')


card = BingoCard(words)
render = template.render(card=card.card)
with open('result.html', 'w') as f:
    f.write(render)

