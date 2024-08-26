import pygame

from random import randint


class Strawberry():
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect() 
        
        #load image of star
        self.image = pygame.image.load('images/strawberry.bmp')
        self.rect = self.image.get_rect()
    
        self.rect.x = randint(15, self.settings.screen_width-15)
        self.rect.y = randint(15, self.settings.screen_height-15)
        
    def blitme(self):
        """ Draw the strawberry """
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.rect.x = randint(20, self.settings.screen_width-20)
        self.rect.y = randint(20, self.settings.screen_height-20)