import random
from .Spy import Spy
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
    initialDeck = [
        Spy, Spy,
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
        # self.shuffledDeck = Deck.initialDeck
        # random.shuffle(self.shuffledDeck)
        self.shuffledDeck = []
        for clazz in Deck.initialDeck:
            self.shuffledDeck.append(clazz())
        # now shuffle
        random.shuffle(self.shuffledDeck)

    def size(self):
        return len(self.shuffledDeck)

    def getCard(self):
        if len(self.shuffledDeck) == 0:
            return None
        else:
            top = self.shuffledDeck[0]
            self.shuffledDeck = self.shuffledDeck[1:]
            return top

    def putCard(self, card):
        self.shuffledDeck.append(card)
