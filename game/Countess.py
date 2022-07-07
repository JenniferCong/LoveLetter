"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Countess(Card):
    role = "Countess"
    value = 8

    def perform(self, action, players, game, deck):
        pass
