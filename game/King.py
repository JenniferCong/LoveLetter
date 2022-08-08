# take https://github.com/matthewjwolff/LoveLetter as the reference
from .Card import Card


class King(Card):
    role = "King ♕"
    value = 7

    def perform(self, action, players, game, deck):
        action.doer.kingKnowledge(action.target.hand)
        doerHand = action.doer.hand
        targetHand = action.target.hand
        action.target.hand = doerHand
        action.doer.hand = targetHand
