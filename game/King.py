"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class King(Card):
    role = "King"
    value = 7

    def perform(self, action, players, game, card_pile):
