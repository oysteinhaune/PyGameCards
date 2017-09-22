import pygame
import sys

from Card import Card
from CardFactory import CardFactory


class Controller():
    def __init__(self, model):
        self.main_model = model
        self.cardFactory = CardFactory()
        self.main_model.setCards(self.cardFactory.generate4Cards())

    def execute(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                #pos = pygame.mouse.get_pos()
                for model in self.main_model.getAllModels():
                    if(model.checkCollissionOnPoint(pos)):
                        #If you hit the blue card:
                        if(model.color == 1):
                            self.new_score = self.main_model.score + 1
                            self.main_model.setScore(self.new_score)
                            self.main_model.setCards(self.cardFactory.generate4Cards())
