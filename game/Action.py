class Action(object):
    def __init__(self, doer, playedCard, target, guess, returnCard1, returnCard2):
        """
        :param doer: the player who play a card
        :param playedCard: the card the player chooses to play
        :param target: the target of playedCard; the target can be other players or the player himself/herself
        :param guess: the card type that the player guesses when the player use Guard
        :param returnCard1: the first card to return when the player use Chancellor
        :param returnCard2: the second card to return when the player use Chancellor
        """
        self.doer = doer
        self.playedCard = playedCard
        self.target = target
        self.guess = guess
        self.returnCard1 = returnCard1
        self.returnCard2 = returnCard2
