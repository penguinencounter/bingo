import random
from bingo_card import BingoCard


with open('bingo_words.txt') as f:
    words = f.read().split('\n')


BingoCard(words).stdout_display()

