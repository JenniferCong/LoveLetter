"""
Created on Jan 25, 2022

@author: Jennifer Chun
"""
import random

# from .Spy import Spy
from .Guard import Guard
from .Priest import Priest
from .Baron import Baron
from .Handmaid import Handmaid
from .Prince import Prince
from .Chancellor import Chancellor
from .King import King
from .Countess import Countess
from .Princess import Princess


class Deck(object):
    initial_deck = [
        # Spy, Spy,
        Guard, Guard, Guard, Guard, Guard, Guard,
        Priest, Priest,
        Baron, Baron,
        Handmaid, Handmaid,
        Prince, Prince,
        Chancellor, Chancellor,
        King,
        Countess,
        Princess]

    def __init__(self):
        # self.shuffled_deck = Deck.initial_deck
        # random.shuffle(self.shuffled_deck)
        self.shuffled_deck = []
        for clazz in Deck.initial_deck:
            self.shuffled_deck.append(clazz())
        # now shuffle
        random.shuffle(self.shuffled_deck)

    def size(self):
        return len(self.shuffled_deck)

    def get_card(self):
        if len(self.shuffled_deck) == 0:
            return None
        else:
            top = self.shuffled_deck[0]
            self.shuffled_deck = self.shuffled_deck[1:]
            return top

    def put_card(self, card):
        self.shuffled_deck.append(card)
