from interface.Interface import Interface
from game.GameEngine import GameEngine
from player.AIRandom import AIRandom
from player.AIIntelligent import AIIntelligent


def main():
    game = GameEngine()
    playerNo = False
    while not playerNo:
        player = Interface().humanPlayer
        print("Number of RandomAI")
        numRand = int(input("> "))
        print("Number of IntelligentAI")
        numIntelligent = int(input("> "))
        if numRand+numIntelligent > 5:
            print('Max player number is 6. Please choose the number again.')
        else:
            playerNo = True
            game.addPlayer(player)
            for i in range(numRand):
                game.addPlayer(AIRandom())
            for i in range(numIntelligent):
                game.addPlayer(AIIntelligent())
            winner = game.runGame()
            print("The winner is " + str(winner))


if __name__ == '__main__':
    main()
