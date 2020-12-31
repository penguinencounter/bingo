import random
import typing
import copy


class BingoCard:
    def __init__(self, words: typing.List[str], hasFreeSpace: bool=True):
        self.created_word_set = copy.deepcopy(words)
        self.using_words = []
        self.hasFreeSpace = hasFreeSpace
        random.shuffle(self.created_word_set)
        self.using_words = self.created_word_set[0:25]
        self.card = [self.using_words[0:5], self.using_words[5:10], self.using_words[10:15], self.using_words[15:20], self.using_words[20:25]]
        self.card_items = []
        for row in self.card:
            for item in row:
                self.card_items.append(item)
        card_lengths = []
        for i in self.card_items:
            card_lengths.append(len(i))
        self.width = max(card_lengths) +2
        if self.hasFreeSpace:
            self.card[2][2] = 'FREE SPACE'
    
    def stdout_display(self):
        for row in self.card:
            print(f'+{"-"*self.width}+{"-"*self.width}+{"-"*self.width}+{"-"*self.width}+{"-"*self.width}+')
            print(f'|', end='')
            for item in row:
                print(f'{item.center(self.width)}|', end='')
            print()
        print(f'+{"-"*self.width}+{"-"*self.width}+{"-"*self.width}+{"-"*self.width}+{"-"*self.width}+')