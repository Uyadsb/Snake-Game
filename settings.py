import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        
        # image of screen 
        self.bg_image = pygame.image.load('images/background.jpg')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))
        
        # snake paramaters
        self.head_color = (0, 0, 0)
        self.snake_color = (255, 255, 255)
        self.color = self.head_color
        self.snake_speed = 6
        self.snake_width = 15
        self.snake_height = 15
        
        self.initialize_dynamic_settings()
        
        
    # initial game settings
    def initialize_dynamic_settings(self):
        # snake paramaters
        self.head_color = (0, 0, 0)
        self.snake_color = (255, 255, 255)
        self.color = self.head_color
        self.snake_width = 15
        self.snake_height = 15
        