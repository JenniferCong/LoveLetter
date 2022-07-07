'''
Created on Nov 3, 2016

The game loop runner

@author: mjw
'''

import random

from .Deck import Deck
from game.Princess import Princess
from game.Action import Action


class GameEngine(object):
    '''
    The engine registers players, instantiates the game, runs the gameplay
    loop, and executes actions that transition the game from state to state.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.origplayers = []
        self.deck = Deck()
        self.running = False
        self.grave = []
        self.discarded = None
        self.eliminatedThisRound = None
        self.ChancellorFlag = False
        self.chancellorCards = []

    def addPlayer(self, player):
        self.origplayers.append(player)

    def drawTwoNew(self):
        newCard1 = self.deck.get_card()
        newCard2 = self.deck.get_card()
        if newCard1 is not None and newCard2 is not None:
            self.chancellorCards = [newCard1, newCard2]

    def runGame(self):
        # make a NEW list
        self.players = list(self.origplayers)
        assert len(self.players) >= 2
        for player in self.players:
            player.assignHand(self.deck.get_card(), self.players)
        # discard one
        self.discarded = self.deck.get_card()
        self.running = True
        # initialize handmaid flag
        for player in self.players:
            player.handmaidenFlag = False
        while self.running == True:
            for player in self.players:
                self.eliminatedThisRound = None
                player.handmaidenFlag = False
                card = self.deck.get_card()
                # I changed my mind, no deep copying

                # Note, API change. Player is notified of the card dealt,
                # remaining cards in the deck, the graveyard, and the
                # list of players

                nonHandmaid = list(self.players)
                for hplayer in nonHandmaid:
                    if hplayer.handmaidenFlag == True:
                        nonHandmaid.remove(hplayer)

                self.drawTwoNew()

                action = player.getAction(card, len(self.deck.shuffled_deck),
                                          self.grave, nonHandmaid, self.chancellorCards)
                # update the player's hand
                if action.playedCard == player.hand:
                    # If the player chose to play the card he had kept,
                    # then replace the card in his hand with the card from
                    # the deck
                    player.hand = card
                action.playedCard.perform(action, self.players, self, self.deck)
                # Tell other players that a play occurred
                for oplayer in self.origplayers:
                    if oplayer != player:
                        oplayer.notifyOfAction(action, self.grave)
                # Then tell players if someone was eliminated
                if self.eliminatedThisRound != None:
                    self.notifyAllEliminate(self.eliminatedThisRound)
                self.grave += [action]
                # End the game if nobody remains or the deck is empty
                if len(self.players) == 1 or self.deck.size() == 0:
                    # kick out of the loop immediately
                    self.running = False
                    break

                print(self.ChancellorFlag)
                if not self.ChancellorFlag:
                    self.deck.put_card(self.chancellorCards[0])
                    self.deck.put_card(self.chancellorCards[1])
                    self.chancellorCards.clear()
                elif self.ChancellorFlag:
                    cardsToReturn = [action.returnCard1, action.returnCard2]
                    self.deck.put_card(action.returnCard1)
                    self.deck.put_card(action.returnCard2)
                    if player.hand in cardsToReturn and self.chancellorCards[0] in cardsToReturn:
                        print("replace by 1")
                        player.hand = self.chancellorCards[1]
                    elif player.hand in cardsToReturn and self.chancellorCards[1] in cardsToReturn:
                        print("replace by 0")
                        player.hand = self.chancellorCards[0]
                    self.chancellorCards.clear()
                    self.ChancellorFlag = False
        winner = self.players[0]
        # TODO: handle ties?
        for player in self.players:
            if player.hand.value > winner.hand.value:
                winner = player
        return winner

    def eliminate(self, player):
        assert (self.eliminatedThisRound == None)
        self.grave.append(Action(player, player.hand, None, None, None, None))
        self.players.remove(player)
        self.eliminatedThisRound = player

    def notifyAllEliminate(self, eliminated):
        for player in self.players:
            player.notifyEliminate(eliminated)
        self.eliminatedThisRound = None

    def abnormalDiscard(self, player, card):
        '''
        Safely force a player to discard a card, and apply any effects if necessary.
        ex: the prince forces a princess discard, that player should lose

        This should only ever be called by the prince...
        '''
        self.grave.append(Action(player, card, None, None, None, None))
        if type(card) == Princess:
            self.eliminate(player)
        else:
            # the player must be given another card
            newCard = self.deck.get_card()
            assert (self.discarded != None)
            if newCard != None:
                # if the deck gave us a new card
                player.hand = newCard
            else:
                # the deck is out of cards. Give the player the discarded card
                # This only ever happens if the last card played is the prince
                player.hand = self.discarded
                self.discarded = None
