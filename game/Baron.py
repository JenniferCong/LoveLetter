"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Baron(Card):
    role = "Baron"
    value = 3

    def perform(self, action, players, game, deck):
        if action.target.hand.value > action.doer.hand.value:
            game.eliminate(action.doer)
        elif action.target.hand.value < action.doer.hand.value:
            game.eliminate(action.target)
