"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Chancellor(Card):
    role = "Chancellor"
    value = 6

    def perform(self, action, players, game, card_pile):
