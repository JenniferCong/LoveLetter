# take https://github.com/matthewjwolff/LoveLetter as the reference
from player.Player import Player


class Human(Player):
    def __init__(self, actionCallback, notifyCallback, priestCallback, kingCallback, eliminateCallback,
                 assignHandCallback, name):
        self.actionCallback = actionCallback
        self.notifyCallback = notifyCallback
        self.priestCallback = priestCallback
        self.kingCallback = kingCallback
        self.eliminateCallback = eliminateCallback
        self.assignHandCallback = assignHandCallback
        self.name = name

    def assignHand(self, card, players):
        Player.assignHand(self, card, players)
        self.assignHandCallback(card, players)

    def getAction(self, dealtCard, deckSize, discardedState, players, chancellorCards):
        return self.actionCallback(dealtCard, deckSize, discardedState, players, chancellorCards)

    def notifyOfAction(self, action, discardedState):
        self.notifyCallback(action, discardedState)

    def priestKnowledge(self, player, card):
        self.priestCallback(player, card)

    def kingKnowledge(self, card):
        self.kingCallback(card)

    def notifyEliminate(self, player):
        self.eliminateCallback(player)

    def __str__(self):
        return self.name
