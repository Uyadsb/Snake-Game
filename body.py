import pygame

class Body:
    def __init__(self, main, x, y):
        
        self.screen = main.screen
        self.settings = main.settings
        self.color = self.settings.color
        
        # Create a snake rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(x, y, self.settings.snake_width,
        self.settings.snake_height)

        # Store the snake position as a decimal value.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
        
    def draw_snake(self):
        pygame.draw.rect(self.screen , self.color, self.rect) 
        

class Snake:
    def __init__(self, main):
        self.settings = main.settings
        self.segments = [Body(main, main.screen.get_width() // 2, main.screen.get_height() // 2)]
        self.head = self.segments[0]
        self.direction = 'RIGHT'
        self.growth_pending = 0
        self.rect = self.segments[0].rect
        
    def update(self, main):
        # Update the body segments
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].x = self.segments[i - 1].x
            self.segments[i].y = self.segments[i - 1].y
            self.segments[i].rect.x = self.segments[i].x
            self.segments[i].rect.y = self.segments[i].y

        # Move the head segment based on the direction
        head = self.segments[0]
        if self.direction == 'RIGHT':
            head.x += self.settings.snake_speed
        elif self.direction == 'LEFT':
            head.x -= self.settings.snake_speed
        elif self.direction == 'UP':
            head.y -= self.settings.snake_speed
        elif self.direction == 'DOWN':
            head.y += self.settings.snake_speed

        # Update the rect position
        head.rect.x = head.x
        head.rect.y = head.y

        # Check for growth
        if self.growth_pending > 0:
            tail = self.segments[-1]
            self.segments.append(Body(main, tail.x, tail.y))
            self.growth_pending -= 1

        # Check for growth
        if self.growth_pending > 0:
            tail = self.segments[-1]
            self.segments.append(Body(main, tail.x, tail.y))
            self.growth_pending -= 1
            
            
    def draw(self):
        for segment in self.segments:
            segment.draw_snake()

    def change_direction(self, new_direction):
        # Prevent reversing direction
        if (self.direction == 'RIGHT' and new_direction != 'LEFT') or \
           (self.direction == 'LEFT' and new_direction != 'RIGHT') or \
           (self.direction == 'UP' and new_direction != 'DOWN') or \
           (self.direction == 'DOWN' and new_direction != 'UP'):
            self.direction = new_direction
    
    
    # grow snake     
    def grow(self):
        self.growth_pending += 1
        self.settings.color = self.settings.snake_color 
        

    