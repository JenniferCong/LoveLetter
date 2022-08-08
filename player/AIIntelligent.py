from game.Countess import Countess
from game.Baron import Baron
from game.Guard import Guard
from game.Spy import Spy
from game.King import King
from game.Prince import Prince
from game.Princess import Princess
from game.Chancellor import Chancellor
from game.Handmaid import Handmaid

from .Player import Player
from .Human import Human
from game.Action import Action
from player.AI import AI

import random
import game.util


class AIIntelligent(AI):
    numBots = 0

    def __init__(self):
        self.number = AIIntelligent.numBots
        AIIntelligent.numBots += 1
        self.cardsInPlay = [0, 5, 2, 2, 2, 2, 1, 1, 1, 1]
        self.playerRanges = {}
        self.priestKnown = None
        self.chancellorReturn = []

    def __str__(self):
        return "AIIntelligent" + str(self.number)

    def notifyEliminate(self, player):
        if player != self:
            self.playerRanges.pop(player)

    def assignHand(self, card, players):
        Player.assignHand(self, card, players)
        for player in players:
            if player != self:
                self.playerRanges[player] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def getHeuristic(self, card, otherCard, players, chancellorCards, discardedState):
        if type(card) == Spy:
            return self.spy(card, otherCard, discardedState)
        elif type(card) == Guard:
            return self.guard(otherCard)
        elif type(card) == Baron:
            return self.baron(card, otherCard, players)
        elif type(card) == Handmaid or type(card) == Prince:
            return [otherCard.value, self, None, None, None]
        elif type(card) == Chancellor:
            return self.chancellor(otherCard, chancellorCards)
        elif type(card) == Countess:
            return self.countess(otherCard, discardedState)
        else:
            return [otherCard.value, self.chooseRandom(players), None, None, None]

    def chooseRandom(self, players):
        player = self
        while player == self:
            player = random.choice(players)
        return player

    def getAction(self, dealtCard, deckSize, discardedState, players, chancellorCards):
        card1 = self.hand
        card2 = dealtCard

        classes = list(game.util.cardTypes)

        if len(players) == 1 and players[0] == self:
            playedCard = card1 if card1.value < card2.value else card2
            guess = None
            if isinstance(playedCard, Guard):
                if type(card1) != type(card2):
                    classes.remove(type(card1))
                    classes.remove(type(card2))
                    classes.append(Guard)
                else:
                    classes.remove(type(card1))
                guess = random.choice(classes)
            if len(classes) == 9 and type(card1) != type(card2):
                classes.remove(Guard)
                classes.append(type(card1))
                classes.append(type(card2))
            elif len(classes) == 9 and type(card1) == type(card2):
                classes.append(Guard)
            else:
                classes.append(type(card1))
                classes.append(type(card2))
            return Action(self, playedCard, self, guess, None, None)

        if isinstance(card1, Princess):
            param1 = self.getHeuristic(card2, card1, players, chancellorCards, discardedState)
            return Action(self, card2, param1[1], classes[param1[2]] if param1[2] is not None else None,
                          param1[3] if param1[3] is not None else None,
                          param1[4] if param1[4] is not None else None)
        elif isinstance(card2, Princess):
            param2 = self.getHeuristic(card1, card2, players, chancellorCards, discardedState)
            return Action(self, card1, param2[1], classes[param2[2]] if param2[2] is not None else None,
                          param2[3] if param2[3] is not None else None,
                          param2[4] if param2[4] is not None else None)

        if isinstance(card1, Countess):
            if isinstance(card2, King) or isinstance(card2, Prince):
                return Action(self, card1, None, None, None, None)
        elif isinstance(card2, Countess):
            if isinstance(card1, King) or isinstance(card1, Prince):
                return Action(self, card2, None, None, None, None)

        card1Heuristic = self.getHeuristic(card1, card2, players, chancellorCards, discardedState)
        card2Heuristic = self.getHeuristic(card2, card1, players, chancellorCards, discardedState)

        if card1Heuristic[0] > card2Heuristic[0]:
            return Action(self, card2, card2Heuristic[1],
                          classes[card2Heuristic[2]] if card2Heuristic[2] is not None else None,
                          card2Heuristic[3] if card2Heuristic[3] is not None else None,
                          card2Heuristic[4] if card2Heuristic[4] is not None else None)
        else:
            return Action(self, card1, card1Heuristic[1],
                          classes[card1Heuristic[2]] if card1Heuristic[2] is not None else None,
                          card1Heuristic[3] if card1Heuristic[3] is not None else None,
                          card1Heuristic[4] if card1Heuristic[4] is not None else None)

    def notifyOfAction(self, action, discardedState):
        if action.doer.__class__ is not Human:
            self.cardsInPlay[action.playedCard.value] -= 1

        self.narrowRanges(action, discardedState)

    def getMinRangePlayer(self):
        playerRangeLength = 11
        minPlayer = None
        for player in self.playerRanges:
            if player != self:
                if len(self.playerRanges[player]) < playerRangeLength:
                    minPlayer = player
        return minPlayer

    def priestKnowledge(self, player, card):
        self.playerRanges[player] = [card.value]

    def kingKnowledge(self, card):
        pass

    def narrowRanges(self, action, discardedState):
        if action.playedCard.value in self.playerRanges[action.doer]:
            self.playerRanges[action.doer] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        for cardType in range(0, 10):
            if self.cardsInPlay[cardType] == 0 and cardType in self.playerRanges[action.doer]:
                self.playerRanges[action.doer].remove(cardType)

        if isinstance(action.playedCard, Countess):
            self.playerRanges[action.doer] = [5, 7, 9]

        elif isinstance(action.playedCard, Baron):
            if len(discardedState) >= 2:
                loserAction = discardedState[len(discardedState) - 2]
                lower = loserAction.playedCard.value
                if action.doer == loserAction.doer:
                    self.playerRanges[action.target] = list(range(lower + 0, 10))
                else:
                    self.playerRanges[action.doer] = list(range(lower + 0, 10))

    def spy(self, card, otherCard, discardedState):
        dataToReturn = [card.value, self, None, None, None]
        if discardedState:
            for discardedAction in discardedState:
                if type(discardedAction.playedCard) == Spy:
                    dataToReturn = [otherCard.value, self, None, None, None]
                    break
        return dataToReturn

    def guard(self, otherCard):
        target = self.getMinRangePlayer()
        if len(self.playerRanges[target]) == 0 or\
                (len(self.playerRanges[target]) == 1 and self.playerRanges[target][0] == 1):
            guessChoice = 1
        else:
            if 1 in self.playerRanges[target]:
                guessChoice = 1
            elif 0 in self.playerRanges[target]:
                guessChoice = 0
            elif 2 in self.playerRanges[target]:
                guessChoice = 2
            elif 3 in self.playerRanges[target]:
                guessChoice = 3
            elif 4 in self.playerRanges[target]:
                guessChoice = 4
            elif 5 in self.playerRanges[target]:
                guessChoice = 5
            elif 6 in self.playerRanges[target]:
                guessChoice = 6
            else:
                guessChoice = random.choice(self.playerRanges[target])
        return [otherCard.value, target, guessChoice, None, None]

    def baron(self, card, otherCard, players):
        for player in self.playerRanges:
            rangeEstimate = self.playerRanges[player]
            if len(rangeEstimate) == 0:
                return [otherCard.value, player, None, None, None]
            elif card.value > rangeEstimate[len(rangeEstimate) - 1]:
                return [otherCard.value, player, None, None, None]
            return [otherCard.value, self.chooseRandom(players), None, None, None]

    def chancellor(self, otherCard, chancellorCards):
        chancellorReturn = [otherCard, chancellorCards[0], chancellorCards[1]]
        chancellorReturnSorted = []
        for cardUnsorted in chancellorReturn:
            chancellorReturnSorted.append({"cardType": cardUnsorted, "cardValue": cardUnsorted.value})
        chancellorReturnSorted.sort(key=lambda my_card: my_card['cardValue'])
        chancellorReturnResult = []
        for cardSorted in chancellorReturnSorted:
            chancellorReturnResult.append(cardSorted['cardType'])
        return [otherCard.value, self, None, chancellorReturnResult[0], chancellorReturnResult[1]]

    def countess(self, otherCard, discardedState):
        if len(discardedState) < 2:
            return [0, self, None, None, None]
        else:
            return [otherCard.value, self, None, None, None]
