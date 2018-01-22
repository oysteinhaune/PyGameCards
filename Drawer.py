import pygame



class Drawer(object):
    #8 Creates the drawer for drawing all model objects (cards, background, etc)
    def __init__(self, model):
        self.model = model

        self.screen = pygame.display.set_mode([self.model.screen_width, self.model.screen_height])

        pygame.font.init()
        self.myfont = pygame.font.SysFont('Times New Roman', 50)

    def draw(self):

        # Black background color
        self.screen.fill(self.model.background_color)

        #Draws the background
        self.screen.blit(self.model.background.scaled_image, self.model.background.get_pos())

        #Draws all objects to screen
        for model in self.model.getAllModels():
            self.screen.blit(model.image, model.get_pos())

        #Draw text from model
        self.myfont = pygame.font.SysFont('Times New Roman', self.model.text_size)
        textsurface = self.myfont.render(self.model.text, self.model.text_aliazed, (self.model.text_blue, self.model.text_green, self.model.text_blue))
        self.screen.blit(textsurface, (self.model.text_xpos, self.model.text_ypos))

        pygame.display.flip()

    def get_background(self):
        return self.background

    def set_background(self, newBackground):
        self.background_image = newBackground


