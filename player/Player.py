# take https://github.com/matthewjwolff/LoveLetter as the reference
class Player(object):

    def getAction(self, dealtCard, deckSize, discardedState, players, chancellorCards):
        raise NotImplementedError

    def assignHand(self, card, players):
        self.hand = card

    def notifyOfAction(self, action, discardedState):
        raise NotImplementedError

    def notifyEliminate(self, player):
        raise NotImplementedError

    def priestKnowledge(self, player, card):
        raise NotImplementedError

    def kingKnowledge(self, card):
        raise NotImplementedError
