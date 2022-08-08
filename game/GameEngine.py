from .Deck import Deck
from .Princess import Princess
from .Spy import Spy
from .Action import Action


class GameEngine(object):

    def __init__(self):
        self.original_players = []
        self.players = []
        self.deck = Deck()
        self.running = False
        self.discarded = []
        self.asideCard = None
        self.eliminatedPlayer = None
        self.chancellorFlag = False
        self.chancellorCards = []

    def addPlayer(self, player):
        self.original_players.append(player)

    def runGame(self):
        self.players = list(self.original_players)
        self.asideCard = self.deck.getCard()
        for player in self.players:
            player.assignHand(self.deck.getCard(), self.players)
            player.handmaidFlag = False
        self.drawChancellorCards()

        self.running = True

        while self.running:
            if self.asideCard is None:
                self.running = False
                break

            if len(self.chancellorCards) == 0:
                self.running = False
                break

            for player in self.players:
                self.eliminatedPlayer = None
                player.handmaidFlag = False
                card = self.deck.getCard()
                if card is None:
                    self.running = False
                    break

                nonHandmaid = self.handmaidAction()

                action = player.getAction(card, len(self.deck.shuffledDeck),
                                          self.discarded, nonHandmaid, self.chancellorCards)

                if action.playedCard is None:
                    self.running = False
                    break

                self.replaceCard(action, player, card)

                self.notifyOtherPlayers(action, player)

                self.chancellorAction(action, player)

                # End the game if there is only one player or the deck is empty
                if len(self.players) == 1 or self.deck.size() == 0:
                    self.running = False
                    break

        winner = self.players[0]

        if len(self.players) > 1:
            for discardedAction in self.discarded:
                if type(discardedAction.playedCard) == Spy:
                    break
                else:
                    for player in self.players:
                        if type(player.hand) == Spy:
                            player.hand.value += 1

            for player in self.players:
                if player.hand is not None and player.hand.value == winner.hand.value and player != winner:
                    print('There is a tie. No winner.')
                    return None
                if player.hand is not None and player.hand.value > winner.hand.value:
                    winner = player
        return winner

    def eliminate(self, player):
        assert (self.eliminatedPlayer is None)
        self.discarded.append(Action(player, player.hand, None, None, None, None))
        self.players.remove(player)
        self.eliminatedPlayer = player

    def notifyAllEliminate(self, eliminated):
        for player in self.players:
            player.notifyEliminate(eliminated)
        self.eliminatedPlayer = None

    def drawChancellorCards(self):
        newCard1 = self.deck.getCard()
        newCard2 = self.deck.getCard()
        if newCard1 is not None and newCard2 is not None:
            self.chancellorCards = [newCard1, newCard2]

    def replaceCard(self, action, player, card):
        if action.playedCard == player.hand:
            player.hand = card
        action.playedCard.perform(action, self.players, self, self.deck)

    def notifyOtherPlayers(self, action, player):
        for original_player in self.original_players:
            if original_player != player:
                original_player.notifyOfAction(action, self.discarded)

        if self.eliminatedPlayer is not None:
            self.notifyAllEliminate(self.eliminatedPlayer)
        self.discarded += [action]

    def handmaidAction(self):
        non_handmaid = list(self.players)
        for handmaid_player in non_handmaid:
            if handmaid_player.handmaidFlag:
                non_handmaid.remove(handmaid_player)
                handmaid_player.handmaidFlag = False
        return non_handmaid

    def princeAction(self, player, card):
        self.discarded.append(Action(player, card, None, None, None, None))
        if isinstance(card, Princess):
            self.eliminate(player)
        else:
            newCard = self.deck.getCard()
            assert (self.asideCard is not None)
            if newCard is not None:
                player.hand = newCard
            else:
                # The deck is out of cards. Give the player the asideCard card
                # This only ever happens if the last card played is Prince
                player.hand = self.asideCard
                self.asideCard = None

    def chancellorAction(self, action, player):
        if self.chancellorCards and self.chancellorFlag:
            cardsToReturn = [action.returnCard1, action.returnCard2]
            self.deck.putCard(action.returnCard1)
            self.deck.putCard(action.returnCard2)
            if player.hand in cardsToReturn and self.chancellorCards[0] in cardsToReturn:
                player.hand = self.chancellorCards[1]
            elif player.hand in cardsToReturn and self.chancellorCards[1] in cardsToReturn:
                player.hand = self.chancellorCards[0]
            self.chancellorCards.clear()
            self.drawChancellorCards()
            self.chancellorFlag = False
