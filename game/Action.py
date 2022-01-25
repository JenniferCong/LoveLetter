"""
Created on Jan 24, 2022

@author: Jennifer Chun
"""


class Action(object):
    """
    Return information of a round
    """

    def __init__(self, doer, used_card, target, guess):
        """
        :param doer: the player
        :param used_card: the card the player wants to use
        :param target: the target of used_card; the target can be others or the player who uses the card
        :param guess: the card type that the player guesses (in the case of Guard)
        """
        self.doer = doer
        self.playedCard = used_card
        self.target = target
        self.guess = guess
