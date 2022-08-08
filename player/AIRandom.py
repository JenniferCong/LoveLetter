import random
from game.Action import Action
from game.Guard import Guard
from game.Handmaid import Handmaid
from game.Countess import Countess
from game.King import King
from game.Prince import Prince
from game.Chancellor import Chancellor
import game.util
from player.AI import AI


class AIRandom(AI):

    numBots = 0

    def __init__(self):
        self.number = AIRandom.numBots
        AIRandom.numBots += 1

    def getAction(self, dealtCard, deckSize, discardedState, players, chancellorCards):
        choice = random.choice((self.hand, dealtCard))
        target = self
        if len(players) == 1 and players[0] == target:
            if isinstance(choice, Guard):
                classIndex = random.randrange(1, len(game.util.cardTypes))
                return Action(self, choice, target, game.util.cardTypes[classIndex], None, None)
            else:
                return Action(self, choice, target, None, None, None)

        if isinstance(self.hand, Countess) and (isinstance(dealtCard, King) or isinstance(dealtCard, Prince)):
            return Action(self, self.hand, self, None, None, None)
        elif isinstance(dealtCard, Countess) and (isinstance(self.hand, King) or isinstance(self.hand, Prince)):
            return Action(self, dealtCard, self, None, None, None)

        if isinstance(self.hand, Chancellor):
            chancellorReturn = [self.hand, chancellorCards[0], chancellorCards[1]]
            returnChoice1 = random.choice(chancellorReturn)
            chancellorReturn.remove(returnChoice1)
            returnChoice2 = random.choice(chancellorReturn)
            return Action(self, self.hand, self, None, returnChoice1, returnChoice2)

        if not isinstance(choice, Handmaid):
            while target is self:
                target = random.choice(players)

        classIndex = random.randrange(1, len(game.util.cardTypes))
        return Action(self, choice, target, game.util.cardTypes[classIndex], None, None)

    def notifyOfAction(self, action, discardedState):
        pass

    def priestKnowledge(self, player, card):
        pass

    def kingKnowledge(self, card):
        pass

    def notifyEliminate(self, player):
        pass

    def __str__(self):
        return "AIRandom" + str(self.number)
