import pygame

from Controller import Controller
from Drawer import Drawer
from Model import Model


class Main(object):

    def __init__(self):
        pygame.init() # Initializes the pygame class.

        self.isRunning = True

        self.model = Model() #3
        self.controller = Controller(self.model) #5
        self.drawer = Drawer(self.model) #7
        self.clock = pygame.time.Clock()

    # Gameloop
    def runGame(self):
        while self.isRunning:
            self.controller.execute()
            self.drawer.draw()

        #Number of frames per secong e.g. 60
        #self.clock.tick(60)


main = Main()
main.runGame()
