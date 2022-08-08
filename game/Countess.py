# take https://github.com/matthewjwolff/LoveLetter as the reference
from .Card import Card


class Countess(Card):
    role = "Countess 👠"
    value = 8

    def perform(self, action, players, game, deck):
        pass
