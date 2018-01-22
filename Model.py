# Model part of the MVC contains all the games models.
# The models are altered by the Controller and drawn by the Drawer
# from Card import Card
from Background import Background
import pygame

class Model(object):
    #4 Initialized the "model" e.g. cards. score.
    def __init__(self):
        self.cards = []
        self.score = 0
        self.screen_height = 600
        self.screen_width = 800
        self.background_image = "intro.jpg"
        self.background_color = 0, 0, 0
        self.background = Background(0, 0, self.screen_width, self.screen_height,
                                     pygame.image.load(self.background_image))
        self.text = 'Welcome to the card click game!'
        self.text_aliazed = False
        self.text_red = 30
        self.text_green = 150
        self.text_blue = 0
        self.text_xpos = 170
        self.text_ypos = 120
        self.text_size = 40

    def getAllModels(self):
        return self.cards

    def setCards(self, cards):
        self.cards = cards

    def setScore(self, score):
        self.score = score



