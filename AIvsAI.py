from player.AIRandom import AIRandom
from game.GameEngine import GameEngine
from player.AIIntelligent import AIIntelligent


def main():
    wins = [0, 0, 0, 0]
    totalRounds = 10000

    for i in range(totalRounds):
        game = GameEngine()
        p1 = AIIntelligent()
        p2 = AIIntelligent()
        p3 = AIRandom()
        p4 = AIRandom()
        game.addPlayer(p1)
        game.addPlayer(p2)
        game.addPlayer(p3)
        game.addPlayer(p4)
        winner = game.runGame()
        print("The winner of the game " + str(i) + " is " + str(winner))
        if winner == p1:
            wins[0] += 1
        elif winner == p2:
            wins[1] += 1
        elif winner == p3:
            wins[2] += 1
        elif winner == p4:
            wins[3] += 1
    tieRound = totalRounds-wins[0]-wins[1]-wins[2]-wins[3]
    intelligentWinningRate = (wins[0] + wins[1])/totalRounds*100
    randomWinningRate = (wins[2] + wins[3])/totalRounds*100

    print('IntelligentAI1 wins: ', wins[0])
    print('IntelligentAI2 wins: ', wins[1])
    print('RandomAI1 wins: ', wins[2])
    print('RandomAI2 wins: ', wins[3])
    print('Tie round:', tieRound)
    print('Winning rate of the intelligent AI is:', intelligentWinningRate, '%')
    print('Winning rate of the random AI is:', randomWinningRate, '%')


if __name__ == '__main__':
    main()
