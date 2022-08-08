# take https://github.com/matthewjwolff/LoveLetter as the reference
from .Card import Card


class Baron(Card):
    role = "Baron 🎩"
    value = 3

    def perform(self, action, players, game, deck):
        if action.target.hand and action.doer.hand:
            if action.target.hand.value > action.doer.hand.value:
                game.eliminate(action.doer)
            elif action.target.hand.value < action.doer.hand.value:
                game.eliminate(action.target)
