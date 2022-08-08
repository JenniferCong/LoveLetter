# Still under implementing
import threading
import tkinter as tk
import tkinter.messagebox

from game.GameEngine import GameEngine
from player.AIIntelligent import AIIntelligent
from player.AIRandom import AIRandom
from player.Human import Human
from game.util import cardTypes
from game.Action import Action
from game.Guard import Guard
from game.Priest import Priest
from game.Baron import Baron
from game.Prince import Prince
from game.King import King
from game.Chancellor import Chancellor
from game.Countess import Countess
from game.Princess import Princess


def main():
    threading.Thread(target=gui_thread).start()


def gui_thread():
    global root
    root = tk.Tk()
    app = GUI()
    root.mainloop()


class GUI:
    def __init__(self):
        frame = tk.Frame(root)
        frame.pack()
        global result
        result = tk.Label(frame, text="")
        result.pack()

        name = "Human Player"
        self.humanPlayer = Human(self.actionCallback, self.notifyCallback, self.priestCallback, self.kingCallback,
                                 self.eliminateCallback, self.assignHandCallback, name)

        random_no = tk.Label(frame, text="Number of Random AI: ")
        random_no.pack()
        random_no_entry = tk.Entry(frame)
        random_no_entry.pack()
        intelligent_no = tk.Label(frame, text="Number of Intelligent AI: ")
        intelligent_no.pack()
        intelligent_no_entry = tk.Entry(frame)
        intelligent_no_entry.pack()
        self.button = tk.Button(frame, text='Hello', command=lambda: start_game(self.humanPlayer,
                                                                                int(random_no_entry.get()),
                                                                                int(intelligent_no_entry.get())))
        self.button.pack(side=tk.LEFT)


    def actionCallback(self, dealtCard, deckSize, discardedState, players, chancellorCards):
        print("You have been dealt a " + dealtCard.role)
        chosen = False
        chosenCard = None
        playerChoice = 0
        guessChoice = 0
        returnChoice1 = 0
        returnChoice2 = 0
        playOnSb = [Guard, Priest, Baron, King]
        mustPlayCountess = [Prince, King]

        while not chosen:
            print("What will you play?")
            print("1. " + self.humanPlayer.hand.role)
            print("2. " + dealtCard.role)
            cardChoice = int(input("> "))
            if cardChoice > 2 or cardChoice < 1:
                print("Bad choice")
            elif type(self.humanPlayer.hand) in mustPlayCountess and type(dealtCard) == Countess and cardChoice == 1:
                print("You have to play Countess because you have a " + self.humanPlayer.hand.role)
            elif type(dealtCard) in mustPlayCountess and type(self.humanPlayer.hand) == Countess and cardChoice == 2:
                print("You have to play Countess because you have a " + dealtCard.role)
            else:
                chosen = True
                chosenCard = self.humanPlayer.hand if cardChoice == 1 else dealtCard

        chosen = False
        for i in playOnSb:
            if type(chosenCard) == i:
                while not chosen:
                    print("On whom will you play that?")
                    for i in range(len(players)):
                        print(str(i) + ". " + str(players[i]))
                    playerChoice = int(input("> "))
                    if playerChoice < 0 or playerChoice > (len(players) - 1):
                        print("Bad choice")
                    else:
                        chosen = True

        if type(chosenCard) == Princess:
            print("You are eliminated")

        if type(chosenCard) == Guard:
            chosen = False
            while not chosen:
                print("What card do you guess?")
                for i in range(len(cardTypes)):
                    print(str(i) + ". " + cardTypes[i].role)
                guessChoice = int(input("> "))
                if guessChoice < 0 or guessChoice >= len(cardTypes):
                    print("Bad choice")
                else:
                    chosen = True

        if type(chosenCard) == Chancellor:
            chosen = False
            if chosenCard == self.humanPlayer.hand:
                self.humanPlayer.hand = dealtCard
            while not chosen:
                print("What cards do you want to return?")
                print("0. " + chancellorCards[0].role)
                print("1. " + chancellorCards[1].role)
                print("2. " + self.humanPlayer.hand.role)
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
                    returnChoice1 = self.humanPlayer.hand
                if returnChoice2 < 2:
                    returnChoice2 = chancellorCards[returnChoice2]
                else:
                    returnChoice2 = self.humanPlayer.hand

        return Action(self.humanPlayer, chosenCard, players[playerChoice], cardTypes[guessChoice], returnChoice1,
                      returnChoice2)

    def notifyCallback(self, action, discardedState):
        print("Player " + str(action.doer) + " played " + action.playedCard.role + " on " + str(
            action.target))
        if type(action.playedCard) == Guard:
            print("It guessed " + action.guess.role)

    def priestCallback(self, player, card):
        print("Player " + str(player) + " has a " + card.role)

    def kingCallback(self, card):
        print("Now you have a " + card.role)

    def eliminateCallback(self, player):
        print("Player " + str(player) + " is eliminated")

    def assignHandCallback(self, card, players):
        print("The game begins. " + str(players) + " are playing.")
        frame = tk.Frame(root)
        frame.pack()
        assign_hand = tk.Label(frame, text="")
        assign_hand.pack()
        assign_hand['text'] = "The game begins. " + str(players) + " are playing."
        print("Your initial card is " + card.role)


def start_game(humanPlayer, numRand, numIntelligent):
    game = GameEngine()
    playerNo = False
    while not playerNo:
        player = humanPlayer
        if numRand + numIntelligent > 5:
            tk.messagebox.showwarning('Notification', 'Max player number is 6. Please choose the number again.')
            break
        else:
            playerNo = True
            game.addPlayer(player)
            for i in range(numRand):
                game.addPlayer(AIRandom())
            for i in range(numIntelligent):
                game.addPlayer(AIIntelligent())
            winner = game.runGame()
            result.pack()
            result['text'] = 'The winner is ' + str(winner)


if __name__ == '__main__':
    main()
