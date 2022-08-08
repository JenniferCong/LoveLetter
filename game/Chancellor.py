from .Card import Card


class Chancellor(Card):
    role = "Chancellor 🎓"
    value = 6

    def perform(self, action, players, game, deck):
        game.chancellorFlag = True
