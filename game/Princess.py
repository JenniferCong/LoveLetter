# take https://github.com/matthewjwolff/LoveLetter as the reference
from .Card import Card


class Princess(Card):
    role = "Princess 👸"
    value = 9

    def perform(self, action, players, game, deck):
        game.eliminate(action.doer)
