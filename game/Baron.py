"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Baron(Card):
    role = "Baron"
    value = 3

    def perform(self, action, players, game, card_pile):
