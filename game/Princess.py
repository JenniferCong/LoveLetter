"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Princess(Card):
    role = "Princess"
    value = 9

    def perform(self, action, players, game, deck):
        players.remove(action.doer)
        game.eliminated_this_round = action.doer
