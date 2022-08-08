# take https://github.com/matthewjwolff/LoveLetter as the reference
from player.Player import Player


class AI(Player):
    def getAction(self, dealtCard, deckSize, discardedState, players, chancellorCards):
        pass

    def notifyOfAction(self, action, discardedState):
        pass

    def notifyEliminate(self, player):
        pass

    def priestKnowledge(self, player, card):
        pass

    def kingKnowledge(self, card):
        pass
