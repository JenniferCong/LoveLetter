"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""

from .Card import Card

class King(Card):
    role = "King"
    value = 7

    def perform(self, action, players, game, deck):
        action.doer.kingKnowledge(action.target.hand)
        doerHand = action.doer.hand
        targetHand = action.target.hand
        action.target.hand = doerHand
        action.doer.hand = targetHand
