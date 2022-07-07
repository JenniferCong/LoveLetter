'''
Created on Dec 17, 2016

@author: mjw
'''
from player.Player import Player
from game.Guard import Guard
from game.Baron import Baron
from game.Countess import Countess
from game.Chancellor import Chancellor

from random import choice


class AI(Player):
    '''
    Base class for all AI implementations.

    Contains some helpful bot functions
    '''

    def getHeuristic(self, card, otherCard, players):
        '''
        Switch statement for various heuristic methods
        '''
        if type(card) == Guard:
            return self.guard(card, otherCard, players)
        elif type(card) == Baron:
            return self.baron(card, otherCard, players)
        elif type(card) == Countess:
            return self.countess(card, otherCard, players)
        # elif type(card) == Chancellor:
        #     return self.chancellor(card, otherCard, players)
        # King, Priest, Handmaid all return same default
        else:
            return [otherCard.value, self.chooseRandom(players), None]

    # Choose a player that is not this bot
    def chooseRandom(self, players):
        player = self
        while player == self:
            player = choice(players)
        return player