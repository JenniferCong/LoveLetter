"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card


class Spy(Card):
    person = "Spy"
    value = 0

    def perform(self, action, players, game, deck):
        pass
