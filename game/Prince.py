# take https://github.com/matthewjwolff/LoveLetter as the reference
from .Card import Card


class Prince(Card):
    role = "Prince ♔"
    value = 5

    def perform(self, action, players, game, deck):
        game.princeAction(action.target, action.target.hand)
