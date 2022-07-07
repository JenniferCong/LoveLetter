"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Handmaid(Card):
    role = "Handmaid"
    value = 4

    def perform(self, action, players, game, deck):
        # TODO: refactor engine to work handmaid
        # action.doer.handmaidenFlag = True
        pass