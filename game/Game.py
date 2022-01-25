"""
Created on Jan 25, 2022

@author: Jennifer Chun
"""


from .Deck import Deck
from .Action import Action
from .Princess import Princess


class Game(object):

    def __init__(self):
        self.deck = Deck()
        self.side_card = None
        self.init_players = []
        self.players = []
        self.eliminated_player = None
        self.out = []
        self.running = False

    def add_players(self, player):
        self.init_players.append(player)

    def eliminate_players(self, player):
        assert self.eliminated_player is None
        self.out.append(Action(player, player.hand, None, None))
        self.init_players.remove(player)
        self.eliminated_player = player

    def run_game(self):
        self.players = self.init_players
        # make sure the number of people is enough to begin a game
        assert len(self.players) > 1
        # put the top card to the side
        self.side_card = self.deck.get_card()
        self.running = True
        # while self.running:


