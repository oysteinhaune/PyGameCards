import pygame

from Background import Background


class Drawer(object):
    def __init__(self, model):
        # The display
        size = width, height = 800, 600
        self.screen = pygame.display.set_mode(size)

        self.model = model
        self.black = 0, 0, 0

        self.background = Background(0,0, width, height, pygame.image.load("table.jpg"))

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

    def draw(self):
        #Fills the screen with a default black color
        self.screen.fill(self.black)

        #Draws the background
        self.screen.blit(self.background.scaled_image, self.background.get_pos())

        #Draws all objects to screen
        for model in self.model.getAllModels():
            self.screen.blit(model.image, model.get_pos())

        #Draw score
        textsurface = self.myfont.render('Score: '+ str(self.model.score), False, (0, 0, 0))
        self.screen.blit(textsurface, (300, 50))

        pygame.display.flip()


    def getBackground(self):
        return self.background
