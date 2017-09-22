from random import randint

import pygame

from Card import Card


class CardFactory():

    def __init__(self):
        pass

    def generate4Cards(self):
        self.cards = [0,0,0,0]
        self.blueCard = randint(0,3)
        for i in range (0,4):
            if i == self.blueCard:
                self.cards[i] = Card(110+150*i, 200, pygame.image.load("card_blue.png"), 1)
            else:
                self.cards[i] = Card(110+150*i, 200, pygame.image.load("card_red.png"), 0)
        return self.cards