import time
import sys

import pygame
import pygame.font 

from settings import Settings
from body import Snake
from eat import Strawberry
from button import Button
from game_stats import GameStats


class SnakeGame:
    def __init__(self):
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.stats = GameStats(self)
        
        # if you  want to make screen with your own size just make the three lines later comment and rewrite this line, go to settings.py and modify it ! 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 
        
        # self.screen = pygame.display.set_mode( (0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width 
        
        # name of screen 
        pygame.display.set_caption("Snake Game")
        
        self.strawberry = Strawberry(self)
        self.snake = Snake(self)
        self.play_button = Button(self, "Play")
    
    
    def _reset_game(self):
        # Reset game statistics and settings
        self.stats.reset_stats()
        self.settings.initialize_dynamic_settings()
        
        # Reset the snake and strawberry
        self.snake = Snake(self)
        self.strawberry = Strawberry(self)
        
        # Make the play button visible and reset game state
        self.stats.game_active = True
        pygame.mouse.set_visible(False)
    
    
    def _check_button_mouse_pos(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            return True
        
    
    def _game_over(self, msg):
        self.font = pygame.font.SysFont('Arial', 120, bold=True)
        self.mgs_image = self.font.render(msg, True, (255, 150, 0))
        self.msg_image_rect = self.mgs_image.get_rect()
        # Center the text on the screen
        self.msg_image_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
        self.screen.blit(self.mgs_image, self.msg_image_rect)
        pygame.display.flip()  # Update the display
        pygame.mouse.set_visible(True)
        self.stats.game_active = False
        self.settings.initialize_dynamic_settings()
          
    
    def _check_play_button(self):
        if not self.stats.game_active:
            self._reset_game()
            # reset the game statistics
            self.stats.reset_stats()
            # to move screen into next image
            pygame.display.flip()
            
            self.stats.game_active = True
        
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            

    def _check_border(self):
        if (self.snake.head.rect.left < 0 or
            self.snake.head.rect.right > self.settings.screen_width or
            self.snake.head.rect.top < 0 or
            self.snake.head.rect.bottom > self.settings.screen_height):
            self._game_over("Game Over !!!")
            time.sleep(2)  # Wait for 2 seconds
            self._check_events()

          

    def _eat(self):
        if self.snake.rect.colliderect(self.strawberry.rect):
            self.snake.grow()
            self.strawberry.update()
            
    def _check_events(self):
        #watch the keyboard and mouse function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('RIGHT')
                elif event.key == pygame.K_RETURN:
                    self._check_play_button()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self._check_button_mouse_pos(mouse_pos) :
                    self._check_play_button()


    #redraw the background each loop
    def _update_screen(self):
        self.screen.blit(self.settings.bg_image, (0,0))
        
        # draw eat (strawberry)
        self.strawberry.blitme()
        
        # draw snake 
        self.snake.draw()
        
        # draw play button in inactive game state
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        # to move screen into next image
        pygame.display.flip()
        self.clock.tick(self.settings.snake_speed * 10) # Control the speed of the snake
        
    
    # the main function
    def _run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self._check_border()
                self.snake.update(self)
                self._eat()
                
            self._update_screen()
            

if __name__ == "__main__":
    snake = SnakeGame()
    snake._run_game()