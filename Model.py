# Model part of the MVC contains all the games models. The models are altered by the Controller and drawn by the Drawer
from Card import Card


class Model(object):
    def __init__(self):
        self.cards = []
        self.score = 0

    def getAllModels(self):
        return self.cards

    def setCards(self, cards):
        self.cards = cards

    def setScore(self, score):
        self.score = score