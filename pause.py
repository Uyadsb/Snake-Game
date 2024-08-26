import pygame


class Pause:
    def __init__(self, game):
        self.pause = -1
        self.screen = game.screen
        self.clock = pygame.time.Clock()        
        self.screen_rect = self.screen.get_rect()
        
        # attrb to main game
        self.main = game

    
    def pause_game(self):
        while self.pause == 1:
            self.font = pygame.font.SysFont('Arial', 40, bold=True)
            self.mgs_image = self.font.render("Game paused, Press p to resume..." , True, (255, 150, 0))
            self.msg_image_rect = self.mgs_image.get_rect()
            
            # Center the text on the screen
            self.msg_image_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
            self.screen.blit(self.mgs_image, self.msg_image_rect)
            pygame.display.flip()  # Update the display

            # Control the frame rate
            self.clock.tick(5) # Slow tick rate to reduce CPU usage while paused
            
            self.main._check_events()
    