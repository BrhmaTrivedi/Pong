import pygame

class Bars:
    def __init__(self, game,screen, pos, size):
        self.game = game
        self.screen = screen
        self.screenrect = self.screen.get_rect()

        self.pos = pos
        self.size = size
        self.colour = (0,0,0)

        self.moving_up = False
        self.moving_down = False
        self.velocity = 0
        
        self.rect = pygame.Rect(self.pos,self.size)

        self.bar_invisible_rect = pygame.Rect(self.rect.x, self.rect.bottom, self.rect.width, 1)
        
    def update(self):
        if self.moving_up and self.rect.top >= self.screenrect.top:
            self.velocity -= 1
        
        self.rect.top = max(self.rect.top, self.screenrect.top)

        if self.moving_down and self.rect.bottom < self.screenrect.bottom:
            self.velocity += 1
        
        self.rect.bottom = min(self.rect.bottom, self.screenrect.bottom)


        self.rect.y += self.velocity
        self.bar_invisible_rect.y = self.rect.bottom

            
    def render(self):

        pygame.draw.rect(self.screen, self.colour, self.rect)
        pygame.draw.rect(self.screen, (255,0,0), self.bar_invisible_rect)

        
