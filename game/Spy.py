"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Spy(Card):
    role = "Spy"
    value = 0

    def perform(self, action, players, game, card_pile):
