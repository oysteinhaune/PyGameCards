import pygame
import sys
from CardFactory import CardFactory


class Controller():
    #6 Initializes the controller given the model.
    # E.g. cardFactory for generating cards and handling card switches and more.
    def __init__(self, model):
        self.main_model = model
        self.cardFactory = CardFactory()
        self.main_model.setCards(self.cardFactory.generate4Cards())
        self.gamestarted = 1

    def execute(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT: sys.exit()

            if self.gamestarted == 0:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN and self.gamestarted == 1:
                pos = event.pos
                self.main_model.background.set_scaled_image(pygame.image.load('./card_blue.png'))
                #pos = pygame.mouse.get_pos()
                for model in self.main_model.getAllModels():
                    if(model.checkCollissionOnPoint(pos)):
                        #If you hit the blue card:
                        if(model.color == 1):
                            self.new_score = self.main_model.score + 1
                            self.main_model.setScore(self.new_score)
                            self.main_model.setCards(self.cardFactory.generate4Cards())
                        if(model.color == 0 and self.main_model.score >= 5):
                            self.new_score = self.main_model.score - 5
                            self.main_model.setScore(self.new_score)

