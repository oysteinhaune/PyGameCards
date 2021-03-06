import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.image = image
        self.rect = pygame.Rect(x, y, w, h)
        self.scaled_image = pygame.transform.scale(self.image,(self.width,self.height))

    def get_pos(self):
        return (self.x, self.y)

    def set_background(self, new_background):
        self.image = new_background

    def set_scaled_image(self, newBackground):
        self.scaled_image = pygame.transform.scale(newBackground, (self.width, self.height))