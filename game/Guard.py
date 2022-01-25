"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Guard(Card):
    role = "Guard"
    value = 1

    def perform(self, action, players, game, card_pile):
