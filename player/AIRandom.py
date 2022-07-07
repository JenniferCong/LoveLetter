'''
Created on Nov 27, 2016

@author: mjw
'''
import random
from game.Action import Action
from game.Handmaid import Handmaid
from game.Countess import Countess
from game.King import King
from game.Prince import Prince
from game.Chancellor import Chancellor
import game.util
from player.AI import AI


class AIRandom(AI):
    '''
    An AI for engine testing that makes a random choice for all actions.

    Alternately, it is an AI that always takes a random choice.
    '''

    numBots = 0

    def __init__(self):
        self.number = AIRandom.numBots
        AIRandom.numBots += 1

    def getAction(self, dealtCard, deckSize, graveState, players, chancellorCards):
        # ok it's not totally random, but let's not have the bot be a total fool
        # and just play the handmaid on someone else
        choice = random.choice((self.hand, dealtCard))
        target = self

        # If we have to play the countess
        if isinstance(self.hand, Countess) and (isinstance(dealtCard, King) or isinstance(dealtCard, Prince)):
            return Action(self, self.hand, self, None, None, None)
        elif isinstance(dealtCard, Countess) and (isinstance(self.hand, King) or isinstance(self.hand, Prince)):
            return Action(self, dealtCard, self, None, None, None)

        if not isinstance(choice, Handmaid):
            while target is self:
                target = random.choice(players)

        if isinstance(self.hand, Chancellor):
            chancellorReturn = [self.hand, chancellorCards[0], chancellorCards[1]]
            returnChoice1 = random.choice(chancellorReturn)
            chancellorReturn.remove(returnChoice1)
            returnChoice2 = random.choice(chancellorReturn)
            return Action(self, self.hand, self, None, returnChoice1, returnChoice2)

        classIndex = random.randrange(1, len(game.util.cardTypes))
        return Action(self, choice, target, game.util.cardTypes[classIndex], None, None)

    def notifyOfAction(self, action, graveState):
        pass

    def priestKnowledge(self, player, card):
        pass

    def kingKnowledge(self, card):
        pass

    def notifyEliminate(self, player):
        pass

    def __str__(self):
        return "AIRandom" + str(self.number)
