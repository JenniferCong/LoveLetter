# take https://github.com/matthewjwolff/LoveLetter as the reference
from .Card import Card


class Guard(Card):
    role = "Guard 🛡️"
    value = 1

    def perform(self, action, players, game, deck):
        if type(action.target.hand) == action.guess:
            game.eliminate(action.target)
