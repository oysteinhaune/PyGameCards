import pygame
from pygame.rect import Rect


class Card(pygame.sprite.Sprite):

    def __init__(self, x, y, image, colorInt):
        self.x = x
        self.y = y
        self.width = 134
        self.height = 188
        self.color = colorInt
        self.image = pygame.transform.scale(image,(self.width,self.height))

    def __repr__(self):
        return

    def setColor(self, color):
        self.color = color

    def get_pos(self):
        return (self.x, self.y)

    def get_rect(self):
        return Rect(self.x, self.y, self.width, self.height)

    def checkCollissionOnPoint(self, pos):
        return self.get_rect().collidepoint(pos)
