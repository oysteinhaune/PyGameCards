import pygame

from Controller import Controller
from Drawer import Drawer
from Model import Model




class Main(object):

    def __init__(self):
        pygame.init()

        self.isRunning = True

        self.model = Model()
        self.controller = Controller(self.model)
        self.drawer = Drawer(self.model)
        self.clock = pygame.time.Clock()

    def runGame(self):
        while self.isRunning:

            self.controller.execute()
            self.drawer.draw()

        #Number of frames per secong e.g. 60
        #self.clock.tick(60)


main = Main()
main.runGame()