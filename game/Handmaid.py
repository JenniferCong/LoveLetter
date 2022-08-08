# take https://github.com/matthewjwolff/LoveLetter as the reference
from .Card import Card


class Handmaid(Card):
    role = "Handmaid 👗"
    value = 4

    def perform(self, action, players, game, deck):
        action.doer.handmaidFlag = True
