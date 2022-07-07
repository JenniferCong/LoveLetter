"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Priest(Card):
    role = "Priest"
    value = 2

    def perform(self, action, players, game, deck):
        action.doer.priestKnowledge(action.target, action.target.hand)
