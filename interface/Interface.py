'''
Created on Feb 20, 2022

@author: Jennifer Chun
'''
from player.Human import Human
from game.util import cardTypes
from game.Action import Action
from game.Guard import Guard
from game.Priest import Priest
from game.Baron import Baron
from game.King import King
from game.Handmaid import Handmaid
from game.Chancellor import Chancellor


class Interface(object):
    '''
   A rather poor implementation of CLI user input using print statements
    '''

    def priestCallback(self, player, card):
        print("Player " + str(player) + " has a " + card.__class__.__name__)

    def kingCallback(self, card):
        print("Now you have a " + card.__class__.__name__)

    def notifyCallback(self, action, graveState):
        print("Player " + str(action.doer) + " has played " + action.playedCard.__class__.__name__ + " on " + str(
            action.target))
        if action.playedCard == Guard:
            print("They guessed " + action.guess.__class__.__name__)

    def actionCallback(self, dealtcard, deckSize, gravestate, players, chancellorCards):
        print("You have been dealt a " + dealtcard.__class__.__name__)
        chosen = False
        chosenCard = None
        playerChoice = 0
        guessChoice = 0
        returnChoice1 = 0
        returnChoice2 = 0
        playOnSb = [Guard, Priest, Baron, King]

        while not chosen:
            print("What will you play?")
            print("1. " + self.proxy.hand.__class__.__name__)
            print("2. " + dealtcard.__class__.__name__)
            cardChoice = int(input("> "))
            if cardChoice > 2 or cardChoice < 1:
                print("Bad choice")
            else:
                chosen = True
                chosenCard = self.proxy.hand if cardChoice == 1 else dealtcard

        chosen = False
        for i in playOnSb:
            if type(chosenCard) == i:
                while not chosen:
                    print("On whom will you play that?")
                    for i in range(len(players)):
                        print(str(i) + ". " + str(players[i]))
                    playerChoice = int(input("> "))
                    if playerChoice < 0 or playerChoice > (len(players)-1):
                        print("Bad choice")
                    else:
                        chosen = True

        if type(chosenCard) == Guard:
            # they chose a guard, better see what they want to guess
            chosen = False
            while not chosen:
                print("What card do you guess?")
                for i in range(len(cardTypes)):
                    print(str(i) + ". " + cardTypes[i].__name__)
                guessChoice = int(input("> "))
                if guessChoice < 0 or guessChoice >= len(cardTypes):
                    print("Bad choice")
                else:
                    chosen = True

        if type(chosenCard) == Chancellor:
            chosen = False
            if chosenCard == self.proxy.hand:
                self.proxy.hand = dealtcard
            while not chosen:
                print("What cards do you want to return?")
                print(chancellorCards)
                print("0. " + chancellorCards[0].__class__.__name__)
                print("1. " + chancellorCards[1].__class__.__name__)
                print("2. " + self.proxy.hand.__class__.__name__)
                print("The first card is:")
                returnChoice1 = int(input("> "))
                if returnChoice1 < 0 or returnChoice1 >= 3:
                    print("Bad choice")
                else:
                    print("The second card is:")
                    returnChoice2 = int(input("> "))
                    if returnChoice2 < 0 or returnChoice2 >= 3 or returnChoice1 == returnChoice2:
                        print("Bad choice")
                    else:
                        chosen = True
                if returnChoice1 < 2:
                    returnChoice1 = chancellorCards[returnChoice1]
                else:
                    returnChoice1 = self.proxy.hand
                if returnChoice2 < 2:
                    returnChoice2 = chancellorCards[returnChoice2]
                else:
                    returnChoice2 = self.proxy.hand


        if type(chosenCard) == Handmaid:
            print("You cannot be the target in the next round")

        return Action(self.proxy, chosenCard, players[playerChoice], cardTypes[guessChoice], returnChoice1, returnChoice2)

    def eliminateCallback(self, player):
        print("Player " + str(player) + " has been eliminated")

    def assignHandCallback(self, card, players):
        print("The game has begun. " + str(players) + " are playing.")
        print("Your initial card is " + card.__class__.__name__)

    def __init__(self, name=None):
        if name == None:
            print("What is your name?")
            name = input("> ")
        self.proxy = Human(self.actionCallback, self.notifyCallback, self.priestCallback, self.kingCallback, self.eliminateCallback,
                                self.assignHandCallback, name)
