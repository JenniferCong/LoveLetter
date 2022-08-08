from .Card import Card


class Spy(Card):
    role = "Spy 🕶️"
    value = 0

    def perform(self, action, players, game, deck):
        pass
