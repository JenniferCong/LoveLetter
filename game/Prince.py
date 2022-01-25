"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Prince(Card):
    role = "Prince"
    value = 5

    def perform(self, action, players, game, card_pile):
