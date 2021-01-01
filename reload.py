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

codes = input('card code? ').split('.')
set_name = codes[0]
if not os.path.exists(f'stored_cards/{set_name}.json'):
    raise FileNotFoundError('No such set')
else:
    print('found set')
    with open(f'stored_cards/{set_name}.json') as f:
        data = json.load(f)
card_index = codes[1]
try:
    card = data[int(card_index)]
    print('found card')
except ValueError:
    raise ValueError('Card id must be number')

render = template.render(card=card['card'], set_id=set_name, card_id=card['card_id'])
with open('result.html', 'w') as f:
    f.write(render)


print(f'Updated webpage with {set_name}.{card["card_id"]}')

